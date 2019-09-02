# 1、异步任务、app任务 创建或者发布任务
# 2、broker backend
# 3、worker


# celery 流程：
# 创建任务 --> 启动worker --> 执行异步任务


# 当任务发生变更时，需要重启 worker


# 创建任务列表 app 是 my_task
from s6 import Celery

my_task=Celery("tasks",   # 对任务的称呼
               broker="redis://192.168.0.124:6379",   # 存放任务
               backend="redis://192.168.0.124:6379",  # 存放任务的反馈结果
               )


# 创建任务
@my_task.task
def my_func1(a,b):
    return f"my_func1 return{a}{b}"


# 创建任务
@my_task.task
def my_func2():
    return "my_func2"


# 创建任务
@my_task.task
def my_func3():
    return "my_func3"



# 启动 worker
# 在终端中输入：Celery worker -A tasks -l INFO

# 解决 ValueError 问题，windows不支持的解决方案
# 使用第三方模块 pip install eventlet
# 在终端中输入：Celery worker -A tasks -l INFO -P eventlet
