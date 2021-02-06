from queue import Queue
from random import randint

process_time = randint(3, 9)

q = Queue()

for i in range(30):
    q.put(i)
