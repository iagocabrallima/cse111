#Imports
from datetime import datetime
from turtle import rt

#Variables
width=int(input('Enter the width of the tire in mm (ex 205):'))
ratio=int(input('Enter the aspect ratio of the tire (ex 60):'))
diameter=int(input('Enter the diameter of the wheel in inches (ex 15):'))

#Calculate
v=round((3.14*(width**2)*ratio*((width*ratio)+(2540*diameter)))/10000000000,2)
print(f"The approximate volume is {v} liters")
#Time
current_date_and_time = datetime.now()


with open('volume.txt',mode='at') as volumes_file:
    print(f"{current_date_and_time:%Y-%m-%d}{width},{ratio},{diameter},{v}", file=volumes_file)
with open('volume.txt',mode='rt') as volumes_file:
    print(volumes_file.read())
