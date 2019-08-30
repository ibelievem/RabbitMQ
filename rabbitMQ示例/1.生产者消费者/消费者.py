# @author: xws    time: 2019/8/29 17:41

import pika


connection=pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

# 通过管道声明一个队列 （创建一个队列）--有就用，没有就创建
channel.queue_declare(queue='xws')


# 回调函数
def callback(ch, method, properties, body):
    print("消费者接受到了任务: %r" % body)


# 消费消息
channel.basic_consume(queue='xws',auto_ack = True,on_message_callback=callback)


# 开始消费
channel.start_consuming()


