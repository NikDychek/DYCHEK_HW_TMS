import threading

lst = [el for el in range(10, 101)]
even_lst = []
odd_lst = []
count = 10


def increment(name):
    global count
    if count % 2 == 0 and count not in even_lst:
        even_lst.append(count)
        print(f"добавлено четное число {count} потока {name}")
    elif count % 2 == 1 and count not in even_lst:
        odd_lst.append(count)
        print(f"добавлено нечетное число {count} потока {name}")
    count += 1


def thread_task(lock, name):
    while len(even_lst) + len(odd_lst) <= 89:
        lock.acquire()
        increment(name)
        lock.release()


def main_task():
    lock = threading.Lock()

    t1 = threading.Thread(target=thread_task, args=(lock, "thread-1"))
    t2 = threading.Thread(target=thread_task, args=(lock, "thread-2"))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == "__main__":
    main_task()

print(even_lst)
print(odd_lst)