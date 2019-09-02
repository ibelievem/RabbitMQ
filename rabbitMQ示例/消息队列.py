# -*- coding: utf-8 -*-
# __author__ = "maple"
""""""

# 1、异步任务. 你了解的消息队列
"""
    - Queue,将数据存储当前服务器的内存.
    - redis 列表,
    - rabbitMQ/kafka/zeroMQ(专业做消息队列)
    
    补充:saltstack
        - ssh:安装方便,但执行效率慢.
        - agent:执行效率高(基于消息队列zeroMQ做的RPC).
"""

# 2. 公司在什么情况下会用消息队列?
"""
    任务处理,请求数量太多,需要把消息临时放到某个地方.
    发布订阅,一旦发布消息,所有订阅者都会收到一条相同的消息.
    
    应用场景:
        - 长轮询
        - 智能玩具调用百度AI接口时,celery + RabbitMQ
        - 生产者&消费者
"""

# 3. rabbitMQ安装
"""
    服务端: 192.168.19.14
        安装配置epel源
           $ rpm -ivh http://dl.fedoraproject.org/pub/epel/6/i386/epel-release-6-8.noarch.rpm
        安装erlang
           $ yum -y install erlang
        安装RabbitMQ
           $ yum -y install rabbitmq-server
        启动(无用户名密码):
            service rabbitmq-server start/stop
            
        设置用户密码:
            sudo rabbitmqctl add_user wupeiqi 123
            # 设置用户为administrator角色
            sudo rabbitmqctl set_user_tags wupeiqi administrator
            # 设置权限
            sudo rabbitmqctl set_permissions -p "/" root ".*" ".*" ".*"
            
            service rabbitmq-server start/stop
    客户端:
        pip3 install pika 
"""

# 4. 使用
"""
    a.生产者 消费者
        n VS 1、异步任务 
        n VS m
    b.发布订阅
        fanout,和exchange关联的所有队列都会接收到信息.
        direct,关键字精确匹配exchange关联的队列都会接收到信息.
        topic,关键字模糊匹配exchange关联的队列都会接收到信息.
"""

# 5. exchange是什么?
"""
    消息处理的重建建,可以帮助生成者将相关信息发送到指定相关队列.
"""


# 6. RPC  -远程过程调用协议
"""
    前戏:
        我   ->    去哪儿    ->      首都机场票务中心
    远程过程调用.
        我   ->    去哪儿    任务/结果      首都机场票务中心
    ...
"""











