import threading, random, time

def t1(s):
    for i in range(5):
        print(s)
        time.sleep(random.random())


threading.Thread(target=t1, args=['A']).start()
threading.Thread(target=t1, args=['B']).start()
