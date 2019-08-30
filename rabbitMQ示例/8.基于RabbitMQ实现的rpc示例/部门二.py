# -*- coding: utf-8 -*-
# __author__ = "maple"


#!/usr/bin/env python

import pika
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

# 任务二监听任务队列
channel.queue_declare(queue='rpc_queue')


def on_request(ch, method, props, body):
    n = int(body)
    response = n + 100

    # props.reply_to  存放结果的队列.
    # props.correlation_id  任务
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id= props.correlation_id),
                     body=str(response))
    # 回复接收到消息后的确认
    ch.basic_ack(delivery_tag=method.delivery_tag)

# 谁空闲 谁处理
channel.basic_qos(prefetch_count=1)

# 消费消息
channel.basic_consume(queue='rpc_queue',on_message_callback=on_request,)

# 开始消费消息
channel.start_consuming()