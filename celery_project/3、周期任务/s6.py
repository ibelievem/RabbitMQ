# __author__: xws    
# time: 2019/9/2 15:13

from celery import Celery
from celery.schedules import crontab

celery_task = Celery("task",
                     broker="redis://192.168.0.124:6379",
                     backend="redis://192.168.0.124:6379",
                     include=["task_one","task_two"])


# 我要对beat任务生产做一个配置,这个配置的意思就是每10秒执行一次my_func_task_one,任务参数是(10,10)
celery_task.conf.beat_schedule={
    "each10s_task":{
        "task":"task_one.my_func1_task_one",
        "schedule":10, # 每10秒钟执行一次
        "args":(10,20)
    },
    "each5s_task": {
        "task": "task_two.my_func2_task_two",
        "schedule": 5,  # 每5秒执行一次
        "args": (50, 60)
    },
    # "each1m_task": {
    #     "task": "Celery_task.task_one.one",
    #     "schedule": crontab(minute=1), # 每一分钟执行一次
    #     "args": (10, 10)
    # },
    # "each24hours_task": {
    #     "task": "Celery_task.task_one.one",
    #     "schedule": crontab(hour=24), # 每24小时执行一次
    #     "args": (10, 10)
    # }

}

#以上配置完成之后,还有一点非常重要
# 不能直接创建Worker了,因为我们要执行周期任务,所以首先要先有一个任务的生产方
# celery beat -A s6
# celery worker -A Celery_task -l INFO -P eventlet
