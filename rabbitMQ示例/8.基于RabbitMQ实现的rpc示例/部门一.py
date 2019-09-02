# -*- coding: utf-8 -*-
# __author__ = "maple"
import pika
import uuid


class FibonacciRpcClient(object):
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
        channel = self.connection.channel()
        self.channel = self.connection.channel()

        # 随机生成一个消息队列(用于接收结果)
        result = self.channel.queue_declare(queue="",exclusive=True)
        # 获取队列的名称
        self.callback_queue = result.method.queue

        # 监听消息队列中是否有值返回,如果有值则执行 on_response 函数(一旦有结果,则执行on_response)
        self.channel.basic_consume(on_message_callback=self.on_response, auto_ack=True,queue=self.callback_queue)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())

        # 任务一 给 任务二 发送一个任务: 1、异步任务、 任务id = corr_id ，2、 任务内容 = '30' ，3、 用于接收结果的队列名称
        self.channel.basic_publish(exchange='',
                                   routing_key='rpc_queue', # 任务二接收任务的队列名称
                                   properties=pika.BasicProperties(
                                         reply_to = self.callback_queue, # 用于接收结果的队列
                                         correlation_id = self.corr_id, # 任务ID
                                         ),

                                   # 传入的参数为消息发送的内容
                                   body=str(n))
        while self.response is None:
            # 监听返回任务的队列是否有结果
            self.connection.process_data_events()

        return self.response


fibonacci_rpc = FibonacciRpcClient()

response = fibonacci_rpc.call(50)

print('返回结果:',response)
