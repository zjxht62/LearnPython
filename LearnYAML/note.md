## 简介
YAML是一种高可读的序列化语言，可以被大多数编程语言支持和使用，主要用于数据序列化、配置文件。

数据序列化，就是可以高效地表示或是描述数据及数据关系，以便用于存储和传输。

优点：
+ 语法简单
+ 结构清晰，易于阅读
+ 功能丰富，可以描述比JSON更加复杂的结构
```yaml
name: 小程序员
age: 30
pet: #注释
  name: 臭猫
  age: 15
```
## 基本语法
+ 大小写敏感
+ 使用缩进表示层级关系
+ 缩进不允许使用Tab，只允许空格
+ 缩进的空格数量不重要，只要相同层级的元素对齐即可
+ #表示注释
```yaml
app:
  name: 网站名称
  server:
    host: 127.0.0.1
    port: 80
```
## 数据类型
YAML支持以下几种数据类型：
+ 对象： 键值对的集合，又称为映射（mapping），对应JSON中的属性
+ 数组： 一组有序的值，又称为列表
+ 纯量：单个的、不可再分的值，比如整数、浮点数、布尔值等基本数据类型，以及字符串

### 对象
```yaml
app:
  name: phub
  type: r18
  server:
    host: 127.0.0.1
    port: 80
```
### 数组
```yaml
job1:
  - Java开发
  - Python开发
  - 前端开发

# 两种数据的表示方法
job2: [ Java开发,Python开发,前端开发 ]
```

## 锚点和引用
原始配置文件
```yaml
prod: 
    driverClassName: com.mysql.cj.jdbc.Driver
    type: com.alibaba.druid.pool.DruidDataSource
    url: jdbc:mysql://localhost:3306/prod
    username: root
    password: 1
dev: 
    driverClassName: com.mysql.cj.jdbc.Driver
    type: com.alibaba.druid.pool.DruidDataSource
    url: jdbc:mysql://localhost:3306/dev	
    username: root
    password: 2
test: 
    driverClassName: com.mysql.cj.jdbc.Driver
    type: com.alibaba.druid.pool.DruidDataSource
    url: jdbc:mysql://localhost:3306/test
    username: root
    password: 3
```
定义锚点driverClass，并在别处使用  
定义使用`&`符号，引用时使用`*`符号
```yaml
prod: 
    driverClassName: &driverClass com.mysql.cj.jdbc.Driver
    type: &type com.alibaba.druid.pool.DruidDataSource
    url: jdbc:mysql://localhost:3306/prod
    username: root
    password: 1
dev: 
    driverClassName: *driverClass
    type: *type
    url: jdbc:mysql://localhost:3306/dev	
    username: root
    password: 2
test: 
    driverClassName: *driverClass
    type: *type
    url: jdbc:mysql://localhost:3306/test
    username: root
    password: 3
```
将配置抽取出为单独结构,使用`<<`将结构拼接过来
```yaml
common: &common
    driverClassName: com.mysql.cj.jdbc.Driver
    type: com.alibaba.druid.pool.DruidDataSource
prod: 
    <<: *common
    url: jdbc:mysql://localhost:3306/prod
    username: root
    password: 1
dev: 
    <<: *common
    url: jdbc:mysql://localhost:3306/dev	
    username: root
    password: 2
test: 
    <<: *common
    url: jdbc:mysql://localhost:3306/test
    username: root
    password: 3
```