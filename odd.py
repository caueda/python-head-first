from datetime import datetime
from os import getcwd,getenv
from random import randint
from time import sleep

odds = [ 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21,
         23, 25, 27, 29, 31, 33, 35, 37, 39,
         41, 43, 45, 49, 51, 53, 55, 57, 59]

rigth_this_minute = datetime.today().minute

for i in range(5):
    sleep_time = randint(1, 60)
    if rigth_this_minute in odds:
        print("This minute seems a little odd.")
    else:
        print("Not an odd minute")
    print(f"{i} Sleeping for {sleep_time} seconds")
    sleep(sleep_time)

print(getcwd())

print(getenv("JAVA_HOME", "Not Set"))


