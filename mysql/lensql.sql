# 查询员工和他的主管的姓名
select t1.ename as 员工姓名
     , t2.ename as 主管姓名
  from tb_emp as t1
       left join tb_emp as t2
           on t1.mgr = t2.eno;

# 查询月薪最高的员工姓名和月薪
# 方法一：嵌套查询（先查出最高的月薪再拿它当条件筛选出对应员工）
# limit在生产环境下操作时用于保命
select ename as 员工姓名
     , sal as 员工月薪
  from tb_emp
  where sal = (select max(sal)
                 from tb_emp) limit 1;

# 方法二：ALL运算符（拿你的月薪和所有人比较，看看是否满足条件）
select ename as 员工姓名
     , sal as 员工月薪
  from tb_emp
  where sal >= all(select sal
                from tb_emp)

# 方法三：计数法（月薪比你更高的员工人数为0，你就是月薪最高的）
select ename as 员工姓名
     , sal as 员工月薪
  from tb_emp as t1
  where (select count(*)
         from tb_emp as t2
         where t2.sal > t1.sal) = 0

# 方法四：存在性判断（不存在有人比你月薪更高，那你就是月薪最高的）
select ename as 员工姓名
     , sal as 员工月薪
  from tb_emp as t1
  where not exist (select 'x'
                   from tb_emp as t2
                   where t2.sal > t1.sal);

# 查询月薪Top3的员工姓名和月薪
select ename, sal
  from tb_emp as t1
  where (select count(*)
         from tb_emp as t2
         where t2.sal > t1.sal) < 3
  order by sal desc;

# 查询部门人数超过5个人的部门的编号和人数
select dno as 部门编号
     , count(*) as 人数
  from tb_emp
  group by dno
  having count(*) > 5;


# 查询所有部门的名称和人数
select dname as 部门名称
     , COALESCE(total, 0) as 部门人数
  from tb_dept as t1
       left join (select dno
                       , count(*) as total
                    from tb_emp
                    group by dno) as t2
            on t1.dno = t2.dno;

# 查询月薪超过其所在部门平均月薪的员工的姓名、部门编号和月薪
select ename, mgr, sal
  from tb_emp as t1
    natural join (select dno
      , avg(sal) as avg_sal
      from tb_emp
      group by dno) as t2
  where sal > avg_sal;

# 查询部门中月薪最高的人姓名、月薪和所在部门名称
select ename, sal, dname
  from tb_dept as t1
    NATURAL JOIN tb_emp as t2
  where (dno, sal) in (select dno
      , max(sal)
      from tb_emp
      group by dno);

# 查询主管和普通员工的平均月薪
# 先通过一个嵌套查询，给原来员工表的数据加上主管或
# 普通员工的标签，然后根据标签分组数据再做聚合处理
select tag as 职级
  , round(avg(sal), 2) as '平均月薪'
  from (select sal
    , case when exists (select 'x'
      from tb_emp as t2
      where t1.eno = t2.mgr)
        then '主管'
        else '普通员工'
     end as tag
  from tb_emp as t1) as tmp
group by tag;

# 查询月薪排名4~6名的员工排名、姓名和月薪
select ename, sal
  from tb_emp
  order by sal DESC
  limit 3 offset 3;

# 方法一：不使用窗口函数
SELECT *
  FROM (SELECT @a := @a + 1 AS 排名
             , ename AS 姓名
             , sal AS 月薪
          FROM tb_emp, (SELECT @a := 0) AS tmp
         ORDER BY sal DESC) AS tmp
 WHERE 排名 BETWEEN 4 AND 6

 # 方法二：使用窗口函数
 # rank、dense_rank、row_number三个函数的区别
SELECT *
  FROM (SELECT ename AS 姓名
             , sal AS 月薪
             , ROW_NUMBER() OVER (ORDER BY sal DESC) AS 排名
          FROM tb_emp) AS tmp
 WHERE 排名 between 4 and 6;

# 查询每个部门月薪排前2名的员工姓名、月薪和部门编号
# 方法一
select ename, sal, dno
  from tb_emp as t1
  where (select count(*)
    from tb_emp as t2
    where t2.dno = t1.dno
      and t2.sal > t1.sal) < 2
  order by dno asc, sal desc;

# 方法二
# partition 分区功能， rn是分区的行数
# partition by 相比较于group by，能够在保留全部数据的基础上，
# 只对其某些字段做分组排序，而group by则保留参与分组的字段和聚
# 合函数的结果，类似excel中的透视表
select ename, sal, dno
  from (select ename
    , sal
    , dno
    , rank() over (partition by dno order by sal desc) as rn
    from tb_emp) as tmp
where rn <= 2;

------------------------------------------------------------------------
# 查出购买总金额不低于800的用户的总购买金额、总订单数和总购买商品数
# 分组后的筛选要用having子句
select user_id as '用户ID'
  , sum(price * quantity) as '购买总金额'
  , count(DISTINCT order_no) as '订单总数'
  , count(quantity) as '购买商品数量'
  from tb_order_detail
    inner join tb_product
      on product = prod_id
  group by user_id
having sum(price * quantity) >= 800;

# 查出购买过"catea"产品的用户的平均订单金额
# with的用法，mysql8中的CTE（公共表表达式语法）
# 平均订单金额不可以用avg函数来获取，因为订单号相同的只算做一个订单
with tmp as (
  select *
    from tb_order_detail
      inner join tb_product
        on product = prod_id
)
select user_id as 用户ID
  , sum(price * quantity) / count(DISTINCT order_no) as 平均订单金额
  from tmp
  where user_id in (select user_id
    from tmp
    where category = 'catea')
group by user_id;

explain select * from tb_order_detail;