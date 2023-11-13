import os
import time
# os.system('cls') # windows
os.system('clear') # linux and mac

for i in range(100):
    p = input("Enter password")
    if p=='phone':
        print("Welcome")
        break
    else:
        print("Wrong password")
        time.sleep(i)
