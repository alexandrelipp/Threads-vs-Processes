from multiprocessing import Process
from info import number_cpu, hard
import time


def main():

    processes = []
    for _ in range(number_cpu):
        process = Process(target=hard)
        process.start()
        processes.append(process)

    for process in processes:
        process.join()


if __name__ == '__main__':
    start = time.perf_counter()
    main()
    print(time.perf_counter()-start)
