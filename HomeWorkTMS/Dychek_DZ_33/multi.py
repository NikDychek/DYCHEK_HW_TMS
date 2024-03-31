from multiprocessing import Process
from time import time, sleep



def print_total(num):
    sleep(10)
    print(f"total:  {num + 10}")


if __name__ == "__main__":  # confirms that the code is under main function
    start = time() * 1000
    lengths = [10, 20, 30]
    procs = []

    # instantiating process with arguments
    for length in lengths:
        proc = Process(target=print_total, args=(length,))
        procs.append(proc)
        proc.start()

    # complete the processes
    for proc in procs:
        proc.join()

    end = time() * 1000

    print(end - start)