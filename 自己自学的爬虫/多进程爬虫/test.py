from multiprocessing import Queue

queue = Queue()
for i in range(1,10):
    queue.put(i)

while True:
    try:
        if queue.get(block=False,timeout=2):
            print(queue.get())
    except:
        pass
