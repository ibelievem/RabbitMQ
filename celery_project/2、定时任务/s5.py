# __author__: xws    
# time: 2019/9/2 14:51

# 定时任务

from .tasks import my_func1
import time,datetime

res=my_func1(2,3)

ctime=time.time()
# 将当前的东八区时间改为 UTC时间 注意这里一定是UTC时间,没有其他说法
utc_time = datetime.datetime.utcfromtimestamp(ctime)
# 为当前时间增加 10 秒
add_time = datetime.timedelta(seconds=10)
action_time = utc_time + add_time

my_func1.apply_async(args=(2,3),eta=action_time)
print(res)
