#Timer

import time

timer = int(input("Set your timer (seconds) : "))

for counter in range(timer, 0, -1):
    seconds = counter % 60
    minutes = int(counter / 60) % 60
    hours = int(counter / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("TIMES UP! ☺")

