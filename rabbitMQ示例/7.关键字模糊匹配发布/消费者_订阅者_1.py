# @author: xws    time: 2019/8/29 17:41

import pika


connection=pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()


# exchange = 'm1', 秘书的名称
# exchange_type = 'topic'，秘书的工作方式：将消息发送给所匹配到的队列,模糊匹配
channel.exchange_declare(exchange = 'm3',exchange_type = 'topic')


# 随机生成并声明一个队列
result = channel.queue_declare(queue = '',exclusive = True)
# 获取队列的名称
queue_name = result.method.queue


# 让exchange和queue进行绑定，使得消息发送到此队列中
# routing_key ： 指明绑定的匹配密钥
# routing_key中  # * ： 模糊匹配
# * ：匹配一个单词  例如：xws.s
# # ：匹配多个单词  例如：xws.s.d.d.d
channel.queue_bind(exchange = 'm3',queue = queue_name,routing_key="xws.*")


# 回调函数
def callback(ch, method, properties, body):
    print("消费者接受到了任务: %r" % body)


# 消费消息
channel.basic_consume(queue=queue_name,auto_ack = True,on_message_callback=callback)


# 开始消费
channel.start_consuming()


