# __author__: xws    
# time: 2019/9/2 15:05

from Celery_task.celery import my_task


@my_task.task
def func1():
    return 456


@my_task.task
def func3():
    return 789
