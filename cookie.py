import os 
import time 

os.system("clear")
print()
Cookie = input("\033[32m\033[1m [\033[36m$\033[32m]\033[33m Enter Your Cookie : \033[36m")
file=open("cookie.txt", "w")
file.write(Cookie)
file.close()

file = open("cookie.txt", "r")
data = file.read()
file.close()

time.sleep(2)
print()

print("\033[32m\033[1mThanks! Your Cookie have Been saved as cookie.txt.")
print()
restart=input(" \033[32m[\033[36m→\033[32m] \033[33mPress Enter to Restart the Program")
os.system("python main.py")

