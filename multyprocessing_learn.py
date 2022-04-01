import threading
from multiprocessing import Process
import time


def counter(num):
    count = 0
    while count < num:
        count += 1


def main():

    a = Process(target=counter, args=(100,))
    a.start()

    a.join()

    print("Finished in: ", time.perf_counter())

if __name__ == '__main__':
#    main()
    print(threading.Thread(main()))




