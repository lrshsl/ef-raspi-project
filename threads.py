
import time
import threading


def thread_function(name, duration):
    print(f"Thread {name}: started")
    time.sleep(duration)
    print(f"Thread {name}: finished")

def basic_test():
    print("Main    : Start")
    x = threading.Thread(target=thread_function, args=(1, 1))
    y = threading.Thread(target=thread_function, args=(2, 3))
    z = threading.Thread(target=thread_function, args=(3, 5))

    print("Main    : starting threads")
    start_time = time.time()
    x.start()
    y.start()
    z.start()

    print("Main    : wait for the threads to finish")
    x.join()
    y.join()
    z.join()

    time_taken = time.time() - start_time
    print(f"Main    : all done: Time taken {time_taken}")





def f1(max_n):
    a = 0
    for n in range(max_n):
        a = 2 ** n
    return a

calc_fns = [
    lambda: f1(100_000),
    lambda: f1(100_000),
    lambda: f1(100_000),
]
sleep_fns = [
    lambda: time.sleep(10),
    lambda: time.sleep(10),
    lambda: time.sleep(10),
]


# Synchronous
def synchronous_time(fns):
    start_time = time.time()
    for fn in fns:
        fn()
    return time.time() - start_time


# Multithreading
def multithreading_time(fns):
    thread1 = threading.Thread(target=fns[0])
    thread2 = threading.Thread(target=fns[1])
    thread3 = threading.Thread(target=fns[2])

    # Start threads
    start_time = time.time()
    thread1.start()
    thread2.start()
    thread3.start()

    # Wait for threads to finish
    thread1.join()
    thread2.join()
    thread3.join()

    return time.time() - start_time


# Multiprocessing
from multiprocessing import Process


def multiprocessing_time(fns):
    process1 = Process(target=fns[0])
    process2 = Process(target=fns[1])
    process3 = Process(target=fns[2])

    # Start processes
    start_time = time.time()
    process1.start()
    process2.start()
    process3.start()

    # Wait for processes to finish
    process1.join()
    process2.join()
    process3.join()

    return time.time() - start_time


# Execute
if __name__ == "__main__":

    print("---- Functions Separately ----\n")
    print("# time.sleep(10) #")
    for i, fn in enumerate(sleep_fns):
        start_time = time.time()
        fn()
        time_taken = time.time() - start_time
        print(f"fn {i}: {time_taken}")

    print("\n# for n in range(100_000): 2 ** n #")
    for i, fn in enumerate(calc_fns):
        start_time = time.time()
        fn()
        time_taken = time.time() - start_time
        print(f"fn {i}: {time_taken}")

    print('\n' * 3)

    print("---- Sleep Functions ----\n")
    t = synchronous_time(sleep_fns)
    print(f"Synchronous: {t}\n")
    t = multithreading_time(sleep_fns)
    print(f"Threads: {t}\n")
    t = multiprocessing_time(sleep_fns)
    print(f"Processes: {t}")

    print('\n' * 3)
    print("---- Calculating Functions ----\n")
    t = synchronous_time(calc_fns)
    print(f"Synchronous: {t}\n")
    t = multithreading_time(calc_fns)
    print(f"Threads: {t}\n")
    t = multiprocessing_time(calc_fns)
    print(f"Processes: {t}\n")






