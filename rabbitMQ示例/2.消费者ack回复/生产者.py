# @author: xws    time: 2019/8/29 17:41

import pika

# 无密码连接 rabbitmq 服务器
connection=pika.BlockingConnection(pika.ConnectionParameters("localhost"))


# 有密码连接 rabbitmq 服务器
# credentials = pika.PlainCredentials("root","123")


# 生成管道
channel=connection.channel()


# 通过管道声明一个队列 （创建一个队列）  --有就用，没有就创建
channel.queue_declare(queue='xws')


# 发送消息到上面声明的 xws 队列
channel.basic_publish(exchange='', # exchange表示交换器，能精确指定消息应该发送到哪个队列
                      routing_key='xws',  # 队列名称
                      body='msg1!' # 发送的内容
                      )

print("生产者创建任务成功")


# 关闭连接
connection.close()




