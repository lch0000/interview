-- 创建数据库
CREATE DATABASE `Q2` DEFAULT CHARSET utf8mb4;

-- 切换数据库
USE `Q2`;

-- 创建订单明细表
CREATE TABLE `tb_order_detail`
(
`id` int NOT NULL COMMENT '流水号',
`order_no` varchar(20) NOT NULL COMMENT '订单编号',
`user_id` varchar(50) NOT NULL COMMENT '用户ID',
`order_date` date NOT NULL COMMENT '下单日期',
`store` varchar(50) NOT NULL COMMENT '店铺ID',
`product` varchar(50) NOT NULL COMMENT '商品ID',
`quantity` int NOT NULL COMMENT '购买数量',
PRIMARY KEY (`id`)
);

-- 插入订单明细数据
INSERT INTO `tb_order_detail` VALUES 
    (1, '001', 'customera', '2022-01-01', 'storea', 'proda', 1),
    (2, '001', 'customera', '2022-01-01', 'storea', 'prodb', 1),
    (3, '001', 'customera', '2022-01-01', 'storea', 'prodc', 1),
    (4, '002', 'customerb', '2022-01-12', 'storeb', 'prodb', 1),
    (5, '002', 'customerb', '2022-01-12', 'storeb', 'prodd', 1),
    (6, '003', 'customerc', '2022-01-12', 'storec', 'prodb', 1),
    (7, '003', 'customerc', '2022-01-12', 'storec', 'prodc', 1),
    (8, '003', 'customerc', '2022-01-12', 'storec', 'prodd', 1),
    (9, '004', 'customera', '2022-01-01', 'stored', 'prodd', 2),
    (10, '005', 'customerb', '2022-01-23', 'storeb', 'proda', 1);

-- 创建商品信息表
CREATE TABLE `tb_product` 
(
`prod_id` varchar(50) NOT NULL COMMENT '商品ID',
`category` varchar(50) NOT NULL COMMENT '种类',
`price` int NOT NULL COMMENT '价格',
PRIMARY KEY (`prod_id`)
);

-- 插入商品数据
INSERT INTO `tb_product` VALUES 
    ('proda', 'catea', 100),
    ('prodb', 'cateb', 200),
    ('prodc', 'catec', 300),
    ('prodd', 'cated', 400);

-- 创建店铺信息表
CREATE TABLE `tb_store`
(
`store_id` varchar(50) NOT NULL COMMENT '店铺ID',
`city` varchar(20) NOT NULL COMMENT '城市',
PRIMARY KEY (`store_id`)
);

-- 插入店铺数据
INSERT INTO `tb_store` VALUES 
    ('storea', 'citya'),
    ('storeb', 'citya'),
    ('storec', 'cityb'),
    ('stored', 'cityc'),
    ('storee', 'cityd'),
    ('storef', 'cityb');

-- 添加外键约束
ALTER TABLE `tb_order_detail` ADD CONSTRAINT FOREIGN KEY (`product`) REFERENCES `tb_product` (`prod_id`);
ALTER TABLE `tb_order_detail` ADD CONSTRAINT FOREIGN KEY (`store`) REFERENCES `tb_store` (`store_id`);