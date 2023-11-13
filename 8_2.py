import os
import time
# os.system('cls') # windows
os.system('clear') # linux and mac

i=0
while True:
    p = input("Enter password")
    if p=='phone':
        print("Welcome")
        break
    else:
        i = i + 1
        print("Wrong password")
        time.sleep(i)
