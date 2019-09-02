# __author__: xws    
# time: 2019/9/2 15:05

from celery import Celery

my_task = Celery("task",
                 broker="redis://192.168.0.124:6379",
                 backend="redis://192.168.0.124:6379",
                 include=["Celery_task.task_one","Celery_task.task_two"])







