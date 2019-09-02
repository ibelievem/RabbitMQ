# __author__: xws    
# time: 2019/9/2 15:05

from .s6 import celery_task


@celery_task.task
def my_func1_task_one(a,b):
    return f"my_func1_task_one_return{a}{b}"

