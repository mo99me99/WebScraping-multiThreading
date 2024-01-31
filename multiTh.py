import threading
import time 


done = False

def worker(text):
    counter = 0
    while True:
        time.sleep(1)
        counter +=1
        print(f'{text}{counter}')

t1 = threading.Thread(target=worker,args=('abc',), daemon=True)
t2 = threading.Thread(target=worker,args=('xyz',), daemon=True)

t1.start()
t2.start()
input('press to quit')
done = True