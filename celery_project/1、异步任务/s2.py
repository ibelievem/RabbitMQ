# __author__: xws    
# time: 2019/9/2 13:43

# 使用 delay 的方式来开始执行的异步任务
from .tasks import my_func1

res=my_func1.delay(2,3)
print(res)

#


