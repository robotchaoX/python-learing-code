# python-code

## python基础

- 基础
- 分支
- 循环
- 数据类型
- 函数
- 类
- 异常
- 模块
- 文件操作

## 网络

- UDP
- TCP

## 多任务

- 线程-threading
- 进程-multiprocessing
- 协程-gevent

## web服务器

- 单任务http服务器
- 多线程http服务器
- 多进程http服务器
- 协程http服务器
- 单线程非阻塞长连接http服务器
- epoll实现http服务器

```
$ tree 
.
├── 01_基础
│   ├── 01_hello.py
│   ├── 02_python关键字.py
│   ├── 03_注释.py
│   ├── 04_行与缩进.py
│   ├── 05_变量定义.py
│   ├── 06_数据类型.py
│   ├── 07_数据类型转换.py
│   ├── 08_input输入.py
│   ├── 09_print格式化输出.py
│   ├── 12_转义字符.py
│   ├── 13_算数运算符.py
│   ├── 14_关系运算符.py
│   ├── 15_逻辑运算符.py
│   ├── 16_赋值运算符.py
│   ├── 17_运算符优先级.py
│   ├── 18_del关键字.py
│   ├── 19_eval字符串转有效对象.py
│   └── 20_pass占位符.py
├── 02_分支
│   ├── 01_if:判断.py
│   ├── 02_if:else:判断.py
│   ├── 03_if:elif:else:完整判断.py
│   ├── 04_if嵌套.py
│   ├── 05_and与条件.py
│   ├── 06_or或条件.py
│   ├── 07_not非条件.py
│   ├── 08_石头剪刀布.py
│   └── 09_三目运算符.py
├── 03_循环
│   ├── 01_while循环.py
│   ├── 02_累加求和.py
│   ├── 03_break.py
│   ├── 04_continue.py
│   ├── 05_while:else:循环.py
│   ├── 06_while:else:含break.py
│   ├── 07_while:else:含continue.py
│   ├── 08_打印星三角.py
│   ├── 09_print函数的结尾.py
│   ├── 10_while嵌套.py
│   ├── 11_九九乘法表.py
│   ├── 12_for_in遍历.py
│   ├── 13_for_in:else:遍历.py
│   ├── 14_for_in:else:含break.py
│   └── 15_for_in:else:含continue.py
├── 04_数据类型
│   ├── 01_字符串str.py
│   ├── 02_字符串str常用操作.py
│   ├── 03_字符串str切片.py
│   ├── 04_字符串str判断方法.py
│   ├── 05_字符串str的查找和替换.py
│   ├── 06_字符串str去除空字符和对齐.py
│   ├── 07_字符串str拆分和拼接.py
│   ├── 08_遍历字符串str.py
│   ├── 09_列表list.py
│   ├── 10_列表list常用方法.py
│   ├── 11_列表list统计.py
│   ├── 12_列表list排序.py
│   ├── 13_遍历列表list.py
│   ├── 14_元组tuple.py
│   ├── 15_元组tuple常用方法.py
│   ├── 16_遍历元组tuple.py
│   ├── 17_字典dict.py
│   ├── 18_字典dict常用方法.py
│   ├── 19_遍历字典dict.py
│   ├── 20_集合set.py
│   ├── 21_集合set常用方法.py
│   ├── 22_遍历集合set.py
│   ├── 23_遍历字典列表嵌套.py
│   ├── 24_容器公共方法.py
│   ├── 25_容器相互转换.py
│   └── 26_推导式.py
├── 05_函数
│   ├── _00_打印分隔线函数模块.py
│   ├── 01_def定义函数.py
│   ├── 02_函数执行.py
│   ├── 03_函数重名覆盖.py
│   ├── 04_函数的参数.py
│   ├── 05_函数的返回值.py
│   ├── 06_函数多个返回值.py
│   ├── 07_拆包.py
│   ├── 08_函数的说明文档.py
│   ├── 09_函数的嵌套调用.py
│   ├── 10_局部变量.py
│   ├── 11_全局变量.py
│   ├── 12_引用.py
│   ├── 13_可变和不可变类型传参.py
│   ├── 14_交换两值.py
│   ├── 15_递归求和.py
│   ├── 16_lambda表达式.py
│   ├── 17_自定义sort排序.py
│   ├── 18_高阶函数.py
│   └── 19_函数模块.py
├── 06_名片管理
├── 07_面向对象基础
│   ├── 01_定义类.py
│   ├── 02_self指向当前对象.py
│   ├── 03_类外添加对象类属性.py
│   ├── 04___new__方法.py
│   ├── 05___init__初始化方法.py
│   ├── 07___init__带参数初始化方法.py
│   ├── 08___del__析构方法.py
│   ├── 09___str__自定义打印信息方法.py
│   ├── 10_类私有属性_私有方法.py
│   ├── 11_类私有属性和方法实现原理.py
├── 08_面向对象特性
│   ├── 01_类继承.py
│   ├── 02_继承的传递性.py
│   ├── 03_继承的传递性注意事项.py
│   ├── 04_子类重写父类同名属性和方法.py
│   ├── 05_子类调用父类同名属性和方法.py
│   ├── 06_super调用父类方法.py
│   ├── 07_继承父类的私有属性和私有方法.py
│   ├── 08_继承父类的公有属性和方法.py
│   ├── 09_多继承.py
│   ├── 10_python多态.py
│   ├── 11_类属性.py
│   ├── 12_修改类属性.py
│   ├── 13_类方法classmethod.py
│   ├── 14_静态方法staticmethod.py
│   ├── 15_类方法综合.py
│   └── 16_单例.py
├── 09_python高级
├── 10_异常
│   ├── 01_try:except:简单异常捕获.py
│   ├── 02_捕获指定异常类型.py
│   ├── 03_捕获多个指定异常类型.py
│   ├── 04_捕获异常描述信息.py
│   ├── 05_捕获未知异常类型.py
│   ├── 06_完整的异常语句.py
│   ├── 07_异常的传递.py
│   ├── 08_raise主动抛出异常1.py
│   ├── 08_raise主动抛出异常.py
│   └── 10_自定义异常类.py
├── 11_模块
│   ├── 01_import导入模块.py
│   ├── _01_测试模块1.py
│   ├── 02_import_as指定别名.py
│   ├── _02_测试模块2.py
│   ├── 03_from_import导入部分.py
│   ├── 04_from_import导入全部.py
│   ├── 05_from_import_重名覆盖问题.py
│   ├── 06___all__允许导入列表.py
│   ├── _06___all__模块.py
│   ├── 07___name__测试导入.py
│   ├── _07__name__的模块.py
│   ├── 08_模块的搜索顺序.py
│   ├── 09_导入立即执行.py
│   ├── _09_导入立即执行的模块.py
│   ├── 10_导入包.py
│   ├── 11_导入包_2.py
│   ├── message_pck
│   │   ├── __init__.py
│   │   ├── receive_message.py
│   │   └── send_message.py
├── 12_发布模块
│   ├── build
│   │   └── lib
│   │       └── message_pkg
│   │           ├── __init__.py
│   │           ├── receive_message.py
│   │           └── send_message.py
│   ├── dist
│   │   ├── message_pkg-1.0
│   │   │   ├── build
│   │   │   │   └── lib
│   │   │   │       └── message_pkg
│   │   │   │           ├── __init__.py
│   │   │   │           ├── receive_message.py
│   │   │   │           └── send_message.py
│   │   │   ├── PKG-INFO
│   │   │   └── setup.py
│   │   └── message_pkg-1.0.tar.gz
│   ├── MANIFEST
│   ├── message_pkg
│   │   ├── __init__.py
│   │   ├── receive_message.py
│   │   └── send_message.py
│   └── setup.py
├── 13_文件操作
│   ├── 01_文件打开模式.py
│   ├── 02_read读取文件.py
│   ├── 03_readline分行读取文件.py
│   ├── 03_seek移动文件指针.py
│   ├── 04_write写入文件.py
│   ├── 05_复制小文件.py
│   ├── 06_复制大文件.py
│   ├── 07_文件备份.py
│   ├── 08_python2字符串.py
│   ├── 09_os文件操作.py
│   ├── 10_os目录操作.py
│   ├── 11_批量输出名-谨慎操作.py
├── web服务器
│   ├── 01-简单的http服务器.py
│   ├── 02-返回固定html文件页面.py
│   ├── 03-返回请求的html页面.py
│   ├── 04-单任务http服务器.py
│   ├── 05-多线程http服务器.py
│   ├── 06-多进程http服务器.py
│   ├── 07-协程http服务器.py
│   ├── 08-单线程-非堵塞-长链接-http服务器.py
│   ├── 09-epoll实现http.py
├── 多任务
│   ├── 01-多任务-线程-threading
│   │   ├── 01-Thread创建线程.py
│   │   ├── 02-继承Thread类创建线程.py
│   │   ├── 03-延时让某些线程先执行.py
│   │   ├── 04-enumerate查看当前线程.py
│   │   ├── 05-start后创建执行子线程.py
│   │   ├── 06-线程间共享全局变量.py
│   │   ├── 07-子线程传参.py
│   │   ├── 08-共享全局变量竞争问题.py
│   │   ├── 09-Lock互斥锁.py
│   │   ├── 10-互斥锁粒度过小问题.py
│   │   └── 11-案例：多任务udp聊天.py
│   ├── 02-多任务-进程-multiprocessing
│   │   ├── 01-Process创建多进程.py
│   │   ├── 02-os获取进程的pid.py
│   │   ├── 03-join主线程阻塞等待子线程.py
│   │   ├── 04-子进程传参.py
│   │   ├── 05-进程间不共享全局变量.py
│   │   ├── 06-Queue进程间通信.py
│   │   ├── 07-Pool进程池.py
│   │   ├── 08-案例：多进程复制.py
│   │   └── 09-案例：多进程赋值-显示进度.py
│   └── 03-多任务-协程-gevent
│       ├── 01-yield实现多任务.py
│       ├── 02-greenlet协程多任务.py
│       ├── 03-gevent协程多任务.py
│       ├── 04-gevent打补丁.py
│       └── 05-案例：协程下载.py
└── 网络
    ├── 01-网络-udp
    │   ├── 01-udp发送数据.py
    │   ├── 02-udp接收数据.py
    │   ├── 03-udp-客户端client.py
    │   ├── 04-udp-服务端server.py
    │   └── 05-案例：udp聊天.py
    └── 02-网络-tcp
        ├── 01-tcp-客户端client.py
        ├── 02-tcp-服务器server.py
        ├── 03-案例：文件下载-client.py
        └── 04-案例：文件下载-server.py
```

