### mysql日志
1. 执行一条update语句，期间发生了什么
    + update语句不需要经过查询缓存，而是会把整个表的查询缓存清空
    + 更新语句的流程会涉及到undo log（回滚日志）、redo log（重做日志）、binlog（归档日志）
      + undo log（回滚日志）：InnoDB存储引擎层生成的日志，实现了事务中的原子性，主要用于事务回滚和MVCC
        + ![回滚事务](/interview/mysql/img/回滚事务.webp.png)
        + trx_id表示该记录是被哪个事务修改的，roll_pointer指针可以将这些undo log串成一个链表，这个链表称为版本链
        + ![版本链](/interview/mysql/img/版本链.webp.png)
        + 通过ReadView + undo log实现MVCC（多版本并发控制），其中就包含快照读（普通select语句）
          + 读提交级别是在每个select都会生成一个新的Read View，也意味着事务期间多次读取同一条数据，前后两次可能会出现不一致
          + 可重复读级别是启动事务时生成一个Read View，然后整个事务期间都在用这个Read View，保证在事务期间读到的数据都是事务启动前的记录
        + undo log和数据页的刷盘策略是一样的，都需要通过redo log保证持久化
      + redo log（重做日志）：InnoDB存储引擎层生成的日志，实现了事务中的持久性，主要用于掉电等故障恢复，crash-safe崩溃恢复能力，而且顺序写开销也不大
        + 为了防止断电导致数据丢失，当一条记录需要更新的时候，InnoDB引擎会先更新内存（同时标记为脏页），然后将所做的修改以redo log的形式记录下来
        + 后台线程将在Buffer Pool的脏页刷新到磁盘里，称为WAL（Write-Ahead Logging）技术，写操作并不是立刻写到磁盘上，而是先写日志，然后再找合适的时间落盘
        + ![WAL](/interview/mysql/img/wal.webp.png)
        + 事务提交时，将redo log持久化到磁盘，不需要关心缓存在Buffer Pool里的脏数据页持久化到磁盘，redo log里记录了对xxx表空间中的YYY数据页ZZZ偏移量的地方做了AAA更新
        + 与undo log的区别
          + redo log记录了此次事务完成后的数据状态，记录的是更新后的值
          + undo log记录了此次事务完成前的数据状态，记录的是更新前的值
          + ![redo和undo区别](/interview/mysql/img/事务恢复.webp.png)
        + 写入redo log的方式使用的文件追加操作，磁盘上的处理是顺序写。而事务落盘到数据页需要先找到写入位置，然后才写入磁盘，所以磁盘操作是随机写。顺序写比随机写高效的多
        + redo log也有自己的缓存，名为redo log buffer，是innodb_log_buffer的一部分，可以通过innodb_log_Buffer_size参数动态调整大小，增大它可以让Mysql处理大事务而不必写盘，从而提升IO性能
          + ![redolog位置](/interview/mysql/img/redologbuf.webp.png)
        + redo log的刷盘时机
          + mysql正常关闭时
          + redo log buffer中记录的写入量大于redo log buffer内存空间的一半时
          + InnoDB的后台线程每隔1秒，将redo log buffer持久化到磁盘
          + 每次事务提交时都将缓存在redo log buffer里的redo log直接持久化到磁盘（这个策略可由innodb_flush_log_at_trx_commit参数控制，配置为1时不会丢数据，配置成0或2还是会有丢失的情况发生）
            + 配置为0时，每次事务提交，还是将redo log留在redo log buffer中，该模式下事务提交时不会主动触发写入磁盘的操作
            + 配置为1时，每次事务提交，都将缓存在redo log buffer里的redo log直接持久化到磁盘，这样可以保证mysql异常重启后数据不会丢失
            + 配置为2时，每次事务提交，都把redo log buffer里的缓存写入到redo log文件，待系统的Page Cache落盘时写入到磁盘，所以也有丢失的可能，mysql进程崩溃时不会丢失数据，只有操作系统崩溃或断电时才会丢数据
            + ![redologcommit](/interview/mysql/img/innodb_flush_log_at_trx_commit.drawio.webp.png)
          + redo log文件写满了怎么办
            + 重做日志文件组（redo log group），由2个redo log文件组成，分别叫做：ib_logfile0和ib_logfile1，类似于双buffer结构
            + 以循环写的方式工作，从头开始写，写完一个写另一个
            + InnoDB用write pos表示redo log当前记录写到的位置，用checkpoint表示当前要擦除的位置
            + ![logfile](/interview/mysql/img/checkpoint.png)
              + write pos和checkpoint的移动都是顺时针方向
              + write pos到checkpoint之间（图中的红色部分），用来记录新的更新操作
              + check point到write pos之间（图中蓝色部分），待落盘的脏数据页记录
              + 如果write pos追上了checkpoint就意味着redo log满了，这时mysql不能再执行新的更新操作，mysql此时会阻塞（所以针对并发量大的系统，适当设置redo log的文件大小很重要），此时会停下来将Buffer Pool中的脏页刷新到磁盘中，然后标记redo log哪些记录可以被擦除，接着对旧的redo log记录进行擦除，等擦除完旧记录腾出了空间，checkpoint就会往后移动，然后mysql恢复正常运行，继续执行新的更新操作
              + 一次checkpoint的过程，就是脏页刷新到磁盘中变成干净页，然后标记redo log哪些记录可以被覆盖的过程
      + binlog（归档日志）：Server层生成的日志，主要用于数据备份和主从复制
        + binlog文件是记录了所有数据库表结构变更和表数据修改的日志
        + redo log和binlog的区别
          + 适用对象不同
             + binlog是MySQL的Server层实现的日志，所有存储引擎都可以使用
             + redo log是InnoDB存储引擎实现的日志
          + 文件格式不同
             + binlog有3种格式类型
               + STATEMENT：每一条修改数据的SQL都会被记录到binlog中，批量update的语句只会记录一条，但动态函数比如uuid和now这种函数会造成恢复端与备份端的差异，数据会不一致
               + ROW：记录行数据最终被修改成什么样了（不算逻辑日志，只能算行拷贝），不会出现动态函数的问题，在执行批量update时，会将所有变更行都记录，使文件过大
               + MIXED：会根据不同的情况自动使用ROW和STATMENT模式
             + redo log是物理日志，记录在某个数据页做了什么修改
          + 写入方式不同
            + binlog是追加，写满一个文件就新创建一个文件继续写
            + redo log是循环写，满了会阻塞
          + 用途不同
            + binlog用于恢复和主从复制
            + redo log用于掉电或mysql崩溃恢复
    + mysql会隐式开启事务来执行“增删改”语句，执行完后自动提交事务。是否自动提交事务，是由autocommit来决定的，默认是开启的
    + 缓冲池buffer Pool
      + ![缓冲池](/interview/mysql/img/缓冲池.drawio.webp.png)
      + 当读取数据时，如果数据存在于Buffer Pool中，客户端就会直接读取其中的数据，没有的话再去磁盘中读取
      + 当修改数据时，如果数据存在于Buffer Pool中，那直接修改其中数据所在的页，然后将其页设置为脏页，为了减少磁盘I/O，不会立即将脏页写入磁盘，后续由后台线程选择一个合适的时机将脏页写入到磁盘
      + mysql启动时，InnoDB会为Buffer Pool申请一片连续的内存空间，然后按照默认的16KB的大小划分出一个个的页，Buffer Pool中的页就叫做缓存页，起初这些缓存页都是空闲的，之后随着程序的运行，才会有磁盘上的页被缓存到其中。虚拟内存被访问后，操作系统才会触发缺页中断，申请物理内存，接着将虚拟地址和物理地址建立映射关系
      + Buffer Pool里存了些啥
        + ![BufferPool内容](/interview/mysql/img/bufferpool内容.drawio.webp.png)
        + 查询一条记录时，InnoDB会把整个页的数据加载到Buffer Pool里，再通过页里的页目录去定位到某条具体的记录
    + 主从复制
      + 依赖于binlog