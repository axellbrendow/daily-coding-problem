import threading
import time

def schedule(n, f, *args, **kwargs):
    def delay_f():
        time.sleep(n / 1000)
        f(*args, **kwargs)
    threading.Thread(target=delay_f).start()

for i in range(100):
    schedule(500, lambda x, y: print(x, y), i, y=i*2)
