import threading
import time
from info import hard,number_cpu

start=time.perf_counter()

threads=[]

for _ in range(number_cpu):
    t=threading.Thread(target=hard)
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

print(time.perf_counter()-start)