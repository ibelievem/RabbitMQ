# 获取执行后的结果


from s6.result import AsyncResult
from .tasks import my_task

# 异步获取任务返回值
async_task = AsyncResult(id="4bc32858-9d13-440b-a2f1-20845677593f",app=my_task)

# 判断异步任务是否执行成功
if async_task.successful():
    #获取异步任务的返回值
    result = async_task.get()
    print(result)
else:
    print("任务还未执行完成")
