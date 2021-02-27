import time
from info import easy,number_cpu
import threading

start=time.perf_counter()

threads=[]

for _ in range(number_cpu):
    t=threading.Thread(target=easy)
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

print(time.perf_counter()-start)