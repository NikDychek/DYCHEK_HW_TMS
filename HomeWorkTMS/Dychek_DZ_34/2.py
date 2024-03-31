import threading

count = 0
res = 1


def fact(lock, name, num):
    lock.acquire()
    global count
    global res
    count += 1
    if count <= num:
        print(f"{name} умножил переменную {res} на {count}")
        res = res * count
    lock.release()


def thread_task(lock, name, num):
    for _ in range(0, num):
        fact(lock, name, num)


def main_task():
    lock = threading.Lock()
    num = int(input("введите число факториал,которого хотите узнать "))
    t1 = threading.Thread(target=thread_task, args=(lock, "thread-1", num))
    t2 = threading.Thread(target=thread_task, args=(lock, "thread-2", num))
    t3 = threading.Thread(target=thread_task, args=(lock, "thread-3", num))
    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()


if __name__ == "__main__":
    main_task()

print(f'окончательный результат {res}')