import os
import time


number_cpu = os.cpu_count()


def easy():
    time.sleep(5)

def hard():
    for i in range(30000000):
        i**2