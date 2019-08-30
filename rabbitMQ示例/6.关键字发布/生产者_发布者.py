# @author: xws    time: 2019/8/29 17:41

import pika

# 无密码连接 rabbitmq 服务器
connection=pika.BlockingConnection(pika.ConnectionParameters("localhost"))


# 生成管道
channel=connection.channel()


channel.exchange_declare(exchange = 'm2',exchange_type = 'direct')


# 发送消息到上面声明的 xws 队列
channel.basic_publish(exchange='m2', # exchange表示交换器，能精确指定消息应该发送到哪个队列
                      routing_key='alex', # 指定接受消息的匹配密钥
                      body='msg3' # 发送的内容
                      )

print("生产者创建任务成功")


# 关闭连接
connection.close()




