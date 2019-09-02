# @author: xws    time: 2019/8/29 17:41

import pika

# 无密码连接 rabbitmq 服务器
connection=pika.BlockingConnection(pika.ConnectionParameters("localhost"))


# 有密码连接 rabbitmq 服务器
# credentials = pika.PlainCredentials("root","123")


# 生成管道
channel=connection.channel()


# 通过管道声明一个队列，支持持久化
# RabbitMQ不允许您使用不同的参数重新定义现有队列，因此需要重新声明不同名称的队列
# 1、异步任务、步骤一
channel.queue_declare(queue='xws1',durable=True)


# 发送消息到上面声明的 xws 队列
channel.basic_publish(exchange='', # exchange表示交换器，能精确指定消息应该发送到哪个队列
                      routing_key='xws1',  # 队列名称
                      body='msg2',  # 发送的内容

                      # 2、步骤二
                      properties=pika.BasicProperties(
                          delivery_mode=2,
                      ))


print("生产者创建任务成功")


# 关闭连接
connection.close()




