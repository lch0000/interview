create database company;
use company;
create table tb_dept(
    dno int not null primary key,
    dname varchar(10) not null,
    dloc varchar(10) not null
)

insert into tb_dept(dno, dname, dloc) values (10, '会计部', '北京');
insert into tb_dept(dno, dname, dloc) values (20, '研发部', '成都');
insert into tb_dept(dno, dname, dloc) values (30, '销售部', '重庆');
insert into tb_dept(dno, dname, dloc) values (40, '运维部', '深圳');
COMMIT;

create table tb_emp(
    eno int not null primary key,
    ename varchar(10) not null,
    job varchar(10) not null,
    mgr int,
    sal int,
    dno int
)

insert into tb_emp(eno, ename, job, mgr, sal, dno) values (1259, '胡一刀', '销售员', 3344, 1800, 30);
insert into tb_emp(eno, ename, job, mgr, sal, dno) values (2056, '乔峰', '分析师', 7800, 5000, 20);
insert into tb_emp(eno, ename, job, mgr, sal, dno) values (3088, '李莫愁', '设计师', 2056, 3500, 20);
insert into tb_emp(eno, ename, job, mgr, sal, dno) values (3211, '张无忌', '程序员', 2056, 3200, 20);
insert into tb_emp(eno, ename, job, mgr, sal, dno) values (3233, '丘处机', '程序员', 2056, 3400, 20);
insert into tb_emp(eno, ename, job, mgr, sal, dno) values (3244, '欧阳锋', '程序员', 3088, 3200, 20);
insert into tb_emp(eno, ename, job, mgr, sal, dno) values (3251, '张翠山', '程序员', 2056, 4000, 20);
insert into tb_emp(eno, ename, job, mgr, sal, dno) values (3344, '黄蓉', '销售主管', 7800, 3000, 30);
insert into tb_emp(eno, ename, job, mgr, sal, dno) values (3577, '杨过', '会计', 5566, 2200, 10);
insert into tb_emp(eno, ename, job, mgr, sal, dno) values (3588, '朱九真', '会计', 5566, 2500, 10);
insert into tb_emp(eno, ename, job, mgr, sal, dno) values (4466, '苗人凤', '销售员', 3344, 2500, 30);
insert into tb_emp(eno, ename, job, mgr, sal, dno) values (5234, '郭靖', '出纳', 5566, 2000, 10);
insert into tb_emp(eno, ename, job, mgr, sal, dno) values (5566, '宋远桥', '会计师', 7800, 4000, 10);
insert into tb_emp(eno, ename, job, mgr, sal, dno) values (7800, '张三丰', '总裁', NULL, 9000, 20);

create table new_tb_emp as select * from tb_emp;