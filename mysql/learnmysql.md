### mysql

## 安装和环境搭建
1. 安装mysql
   下载地址：https://dev.mysql.com/downloads/mysql/
   下载了8.4版本
2. 创建数据库
   在安装的过程中会自动创建相应的库并配置好用户
3. 在vscode中安装管理插件和染色插件
   管理插件安装Weijan Chen的，Jun Han的比较旧了，不支持8.0以上版本的密码验证方式

## 基本概念
1. 什么是数据库？什么是DBMS?
2. 一些概念
   + 表
   + 主键（唯一、可联合）
   + 去重（distinct）
   + 控制行数（limit、offset、top）
   + 排序（order by默认升序ASC，反之DESC）
   + 数据过滤（where）
     - '=' 等于
     - '<>' 不等于
     - '<' 不等于
     - '<=' 小于等于
     - '!<' 不小于
     - '>' 大于
     - '>=' 大于等于
     - '!>' 不大于
     - 'BETWEEN' 在两值之间，左闭右开，左边值可以取到，右边取不到（也有说是mysql包含边界值）
     - 'IS NULL' 是null值
     - 'and' 两边条件都满足
     - 'or' 满足之一就可以，惰性运算，如果第一个条件满足了，就不会执行第二个（第一个优先级高）
     - 'in' 字面意思，后边可以跟select
     -  'not' 否定之后所有条件
     -  'like' 可以使用通配符('%', '_', '[]')
   + 计算字段
   + 过滤分组（HAVING 获取分组内大于两条数据的用户）
   + 子查询（由内向外处理，返回单列）
   + 联结表（使用where联结，必须使用完全列名，执行时是A表的每一条数据去匹配B表，没有条件会产生笛卡尔积）
     - 多表联结非常损耗性能，dbms可能会进行限制
     - inner join（将联结的条件提前，节省性能）
   + 高级联结
     - 表别名（as）
     - 自联结（self-join，比子查询要快）
     - 自然联结（natural join）多个相同列，自己决定显示哪些列
     - 外联结（outer join）使用外联结会有没有被选中的数据，类似于没有实际消费过的顾客，需要指定哪一侧是全量数据，使用right或者left指定，优化手段之一是小的表放在左侧
     - 全外联结（full outer join）（会显示除了关联的行，还有两个表中不关联的所有行）
   + 组合查询
     - UNION（将多条sql结果合并返回）
     - 对UNION返回的所有结果，可以用order by来进行排序，应处于最后一条sql后
   + 插入数据
     - INSERT INTO xx VALUES xx
     - 可以使用 create table xxx as select * from 快速建表
   + 更新和删除数据
     - UPDATE XX SET XX WHERE
     - DELETE FROM XX WHERE
     - TRUNCATE TABLE 直接删除表
   + 创建表和更新表
     - CREATE TABLE xxx (field xxx)
     - ALERT TABLE xxx ADD field
     - ALERT TABLE xxx DROP COLUMN xxx
   + 删除表
     - DROP TABLE xxx （会删除表结构和表中数据，而delete只删除表中数据不动表结构）
   + 视图（是一个虚拟的表，只定义过程没有实际的存储）
     - CREATE VIEW xxx AS SELECT
     - DROP VIEW TABLENAME
   + 存储过程（多条sql的批处理）
     - EXECUTE
     - CREATE PROCEDURE xxx BEGIN xxx END
   + 使用函数
     - 聚合函数（count(*)用于计算所有列的个数，group by 用于分组）
     - 文本处理函数（LTRIM、RTRIM、UPPER、LOWER）
     - 数值函数
     - 日期和时间函数（DATEPART、YEAR）
     - 系统函数
     - 窗口函数（PARTITION BY分析函数）
3. 基础架构
   + 分为server层和存储引擎层
     - server层负责建立连接、分析和执行sql（包括缓存）
     - 存储引擎层负责数据的存储和提取（InnoDB使用B+树索引（主键和二级索引）、MyISAM、Memory）
   + 连接器
     - mysql -h$ip -u$user -p
     - 三次握手(基于TCP协议)
     - 如果一个连接已经建立，即使中途修改了该用户的权限，也不会影响已经存在的连接权限，只有再新建连接才会使用新的权限设置
     - show processlist用于查看当前服务被多少个客户端连接了
     - mysql定义了最大空闲时长，由wait_timeout参数来控制，默认是8小时（28880秒），超过了会自动断开
     - 手动断开空闲连接kill connection + id
     - 被服务端断开后不会马上直到，下次请求时会收到Lost connection错误
     - mysql服务支持的最大连接数由max_connections控制，默认是151个，超过后系统会拒绝接下来的连接请求，报错Too many connections
     - 长连接和短连接，长连接方便但可能会占用内存增多，查询过程中使用内存管理来连接对象，只有在连接断开时才会释放。可以定期断开长连接，也可以客户端主动重置连接mysql_reset_connection()
   + server层查询缓存
     - key,value形式来进行存储，只要一个表有更新操作，这个表的查询缓存就会被清空
     - 8.0版本移除了server层的查询缓存，之前版本如果想关闭缓存可以通过query_cache_type配置成DEMAND来实现
   + 解析sql
     - 解析器（词法分析、语法分析构建语法树
   + 执行sql
     + prepare阶段，也就是预处理阶段（8.0版本在这里判断了表是否存在）
     + optimize阶段，也就是优化阶段（主要负责将sql查询语句的执行方案确定下来）
       + 在查询语句之前加上explain，可以输出这条sql语句的执行计划，key表示执行过程中使用了哪个索引，如果执行计划里的key为null说明没有进行索引，会进行全表扫描（type=ALL），效率低容易锁表
       + 择优选择合适的索引
     + execute阶段，也就是执行阶段
       + 主键索引查询
       + 全表扫描（执行器每查到一条记录后都会发给客户端，而客户端是等整个查询结束后才返回）
       + 索引下推（在存储引擎层解决联合索引的查询，节省很多回表操作的时间）
         + 执行计划里Extra部分如果显示了"Using index condition"，说明使用了索引下推
4. 存储引擎
   + mysql数据库文件存放位置
     + show variables like 'datadir'; 查看方式
     + 默认在/var/lib/mysql/下
     + 目录下有数据库名对应的文件夹，文件夹下db.opt用来存储当前数据库的默认字符集和字符校验规则
     + 文件夹下有表名对应的frm和ibd文件
       + frm存储表结构，包含表结构的定义
       + ibd保存表数据，在5.6.6版本之前可能会存储在ibdata1里，由参数innodb_file_per_table来控制，目前默认参数值是1
   + 表空间的文件结构
     + 表空间由段（segment）、区（extent）、页（page）、行（row）组成
     + ![表空间结构](/interview/mysql/img/表空间结构.drawio.png)
       + 每行记录根据不同的行格式，有不同的存储结构
       + InnoDB的数据是按照页为单位来读写的，当需要读一条记录的时候，先以页为单位，将其整体读进内存，每个页的默认大小为16KB，最多能保证16KB的存储空间
       + 表中数据量大时，为某个索引分配空间的时候按照区（extent）来分配。每个区的大小为1MB，对于16KB的页来说，连续的64个页会被划为一个区，这样就使得链表中相邻的页的物理位置也相邻，就能使用顺序I/O了
       + 多个区组成段（segment），段有多种类型
         + 索引段：存放B+树的非叶子节点的区的集合
         + 数据段：存放B+树的叶子节点的区的集合
         + 回滚段：存放的是回滚数据的区的集合，事务隔离中的MVCC利用了回滚段实现了多版本查询数据
     + InnoDB行格式
       + Redundant 没人用了，5.0版本之前
       + Compact 紧凑的行格式，为了让一个数据页中可以存放更多的行记录，5.1-5.7
       + Dynamic 基于Compact的改进，5.7版本之后默认Dynamic行格式
       + Compressed 基于Compact的改进
       + ![Compact紧凑格式](/interview/mysql/img/COMPACT.drawio.png)
         + 记录的额外信息
           + 变长字段长度列表 只出现在数据表有变长字段的时候，比如varchar
           + NULL值列表 每个列对应一个二进制为（bit），位按照列的顺序逆序排列，如果数据表字段都为非空，表里的行格式就不会有NULL值列表
             + ![null值表](/interview/mysql/img/null值列表4.png)
             + ![null值表](/interview/mysql/img/null值列表5.png)
             + 如果一个记录有9个字段值都可能是NULL，则会创建2个字节的NULL值列表空间
           + 记录头信息
             + delete_mask 执行delete删除记录的时候，并不会真正删除，知识将这个记录置1
             + next_record 下一条记录的位置
             + record_type 表示当前记录的类型，0表示普通记录，1表示B+树非叶子节点记录，2表示最小记录，3表示最大记录
         + 记录的真实数据
           + ![真实数据](/interview/mysql/img/记录的真实数据.png)
             + row_id 如果既没有指定主键，又没有唯一约束，那么InnoDB就会为记录添加该字段，占用6字节
             + trx_id 事务id，表示这个数据是由哪个事务生成的，必需，占用6字节
             + roll_pointer 这条记录上一个版本的指针，必需，7字节
     + varchar(n)中n的最大值
       + 一行记录除了TEXT、BLOBs类型，其他的限制最大为65535字节，一行的总长度
       + n代表的是最多存储的字符数量，并不是字节大小，这里需要看使用的是什么字符集（ascii字符集一个字符占用1字节，UTF-8字符集一个字符需要3字节，utf8mb4的字符是4字节）
     + 行溢出后，mysql如何处理
       + 一个数据页存不下一条记录的情况，将溢出的数据存放到溢出页中
       + 真实数据出只保存部分数据，用20字节存储指向溢出页，方便查找
       + Dynamic和Compressed结构真实数据处不存储部分数据，而是只有20字节的溢出页指针
5. 索引
   + 索引知识点图
     + ![索引脑图](/interview/mysql/img/索引提纲.png)
   + 索引的分类
     + 按照数据结构分类：B+树、Hash、Full-text
     + 按照物理存储分类：聚簇索引（主键索引）、二级索引（辅助索引）
     + 按照字段特性分类：主键索引、唯一索引、普通索引、前缀索引
     + 按字段个数分类：单列索引、联合索引
   + 按数据结构分类
     + 在创建表时，InnoDB存储引擎会根据不同的场景选择不同的列作为索引（都有索引）
       + 如果有主键，默认会使用主键作为聚簇索引的索引键（key）
       + 如果没有主键，就选择第一个不包含NULL值的为一列作为聚簇索引的索引键（key）
       + 在上面两个都没有的情况下，InnoDB将自动生成一个隐式自增id列作为聚簇索引的索引键（key）
     + B+树
       + 多叉树，叶子结点才存放数据，非叶子节点只存放索引
       + 每个节点的数据是按照主键顺序存放的
       + 每一层父节点的索引值都会出现在下层子节点的索引值中
       + 每一个叶子节点都有两个指针，分别指向下一个叶子节点和上一个叶子节点，形成一个双向链表
       + ![B+树存储结构](/interview/mysql/img/btree.drawio.png)
       + B+树存储千万级的数据只需要3-4层高度就可以满足，只需要3-4次磁盘IO
       + 主键索引B+树存放的是实际数据，所有用户记录完整的存储在叶子节点中
       + 二级索引B+树存放的是主键值，而不是实际数据
       + ![二级索引B+树](/interview/mysql/img/二级索引btree.drawio.png)
       + 使用二级索引来查找时，会有回表操作，需要查两个B+树才能查到数据
       + 与跳表的区别（redis使用跳表，不涉及磁盘IO，减少了旋转树结构的开销）
       + 与Hash的区别，hash在做等值查询时非常快，搜索复杂的为O(1)，但hash不适合做范围查询
       + 与二叉树区别，B+树的搜索复杂度为O(logdN)，实际应用中d的值大于100，数据千万级别时只需要3-4次IO操作，而二叉树复杂度为O(logN)，IO次数要多很多
       + 与B树区别，B树的非叶子节点也要存数据，B+树在相同的IO下能查询更多的节点，而且B+树是双链表结构，适合Mysql中的范围顺序查找
   + 按物理存储分类
     + 主键索引
     + 二级索引
   + 按字段特性分类
     + 主键索引（不允许有空值）
         ```
         CREATE TABLE table_name (
          ....
          PRIMARY KEY （index_column_1) USING BTREE
         );
         ```
     + 唯一索引
       + 建表时创建
       ```
       CREATE TABLE table_name (
        ....
        UNIQUE KEY(indwx_column_1, index_column_2, ...)
       );
       ```
       + 建表后创建
       ```
       CREATE UNIQUE INDEX index_name
       ON table_name(index_column_1, index_column_2, ...);
       ```
     + 普通索引
       + 建表时创建
       ```
       CREATE TABLE table_name (
        ....
        INDEX(index_column_1, index_column_2, ...)
       );
       ```
       + 建表后创建
       ```
       CREATE INDEX index_name
       ON table_name(index_column_1, index_column_2, ...);
       ```
     + 前缀索引
       + 针对字符类型字段的前几个字符建立索引，目的是为了减少索引占用的存储空间，提升查询效率
       + 建表时创建
       ```
       CREATE TABLE table_name(
        column_list,
        INDEX(column_name(length))
       );
       ```
       + 建表后创建
       ```
       CREATE INDEX index_name
       ON table_name(column_name(length));
       ```
   + 按字段个数分类
     + 单列索引
     + 联合索引
       + 将多个字段组合成一个索引，该索引就被称为联合索引
       + 创建索引的方式
       ```
       CREATE INDEX index_product_no_name ON product(product_no, name);
       ```
       + 联合索引的非叶子节点用两个字段的值作为B+树的key值，先按照第一个字段进行比较，再按照第二个字段进行比较
       + 遵循最左匹配原则，如果不按照该原则，那么联合索引会失效，因为有查询优化器，所以第一个字段在where子句的顺序并不重要，但如果没有第一个字段，则会失效
       + 范围查询的字段可以用到联合索引，但范围查询如(>,<)字段后边的字段无法用到联合索引，对于(>=,<=,BETWEEN,like)并不会停止，会部分用到联合索引
       + ![联合索引](/interview/mysql/img/联合索引.drawio.png)
     + 索引下推
       + mysql5.6引入了索引下推优化(index condition pushdown)，可以在联合索引遍历过程中对联合索引中包含的字段先做判断，直接过滤掉不满足条件的记录，减少回表次数
       + 查询语句的explain执行计划里，Extra为Using index condition，说明使用了索引下推的优化
     + 索引区分度
       + 区分度大的字段排在前边，更有可能被更多的查询使用到
       + 区分度是某个字段不同值的个数除以表的总行数
       + mysql的查询优化器，如果发现某个值出现在表的数据行中的百分比很高，这时一般会忽略索引，进行全表扫描，一般是30%
     + 联合索引中进行排序
       ```
       select * from order where status = 1 order by create_time asc
       ```
       + 给status和create_time列建立联合索引，可以避免MySQL数据库发生文件排序
       + 文件排序filesort在SQL的执行计划中，Extra列会出现Using filesort
       + 利用索引的有序性，在status和create_time列建立联合索引，避免使用文件排序，提高了查询效率
   + 何时使用索引
     + 特点
       + 优点
         + 提高查询速度
       + 缺点
         + 占用物理空间
         + 创建和维护索引需要耗费时间
         + 会降低表的增删改效率，B+树需要维护
     + 什么时候适合使用索引
       + 字段有唯一性限制，比如商品编码
       + 经常用于where查询条件的字段，可以提高整个表的查询速度，如果查询条件不是一个字段，可以建立联合索引
       + 经常用group by和order by的字段，这样在查询的时候就不需要再做一次排序了
     + 什么时候不需要创建索引
       + 起不到搜索定位效果的字段不需要建索引，会占用物理空间
       + 字段中存在大量的重复数据，例如性别字段
       + 表数据少，不需要创建索引
       + 需要经常更新的字段不需要索引，频繁修改时要维护B+树，频繁重建索引影响数据库性能
     + 索引优化
       + 前缀索引优化
       + 覆盖索引优化
       + 主键索引最好是自增的
       + 防止索引失效