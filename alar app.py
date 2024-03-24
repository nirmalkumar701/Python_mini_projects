import time
print(time.strftime("%H:%M"))
set_alarm=input("which time")
while time.strftime("%H:%M") !=set_alarm:
    time.sleep(1)
print("Time to wakeup")