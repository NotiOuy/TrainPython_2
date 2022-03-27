import threading
import time


def eat_dinner():
    time.time(4)
    print("I eat dinner")


x = threading.Thread(target=eat_dinner())
x.start()

