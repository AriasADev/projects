import string
import time

text = 'hello world'
temp = ''

for ch in text:
    for i in string.printable:
        if i.lower() == ch.lower():
            time.sleep(0.02)
            temp += i
            print(temp)
            break
        else:
            time.sleep(0.02)
            print(temp + i, end='\r', flush=False)
