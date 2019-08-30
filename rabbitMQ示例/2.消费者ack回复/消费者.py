# @author: xws    time: 2019/8/29 17:41

import pika


connection=pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

# 通过管道声明一个队列 （创建一个队列）--有就用，没有就创建
channel.queue_declare(queue='xws')


# 回调函数
def callback(ch, method, properties, body):

    print("消费者接受到了任务: %r" % body)

    # 故意产生 bug 使得消费者死亡，说名字数据拿走后，不给回复数据不会被消费
    # int(sssss)

    # 告诉服务端消息已经被取走
    ch.basic_ack(delivery_tag = method.delivery_tag)


# 默认参数 auto_ack = False，表示需要手动消息确认，使用 basic_ack()  函数
# 若数据拿走但没有确认回复，则数据不会被消费
channel.basic_consume(queue='xws',auto_ack = False,on_message_callback=callback)


# 开始消费
channel.start_consuming()


