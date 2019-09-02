# __author__: xws    
# time: 2019/9/2 15:05

from .s6 import celery_task


@celery_task.task
def my_func2_task_two(a,b):
    return f"my_func2_task_two_return{a}{b}"


