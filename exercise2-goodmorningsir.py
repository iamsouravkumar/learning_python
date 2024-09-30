# import time
# timestamp = time.strftime('%H:%M:%S')
# print(timestamp)
# timestamp = time.strftime('%H')
# print(timestamp)
# timestamp = time.strftime('%M')
# print(timestamp)
# timestamp = time.strftime('%S')
# print(timestamp)

import time
name = input("Enter Your Name: ")
t = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))
# hour = int(input("Enter Time: "))
# print(hour)

if(hour>=0 and hour<12):
   print("Good Morning", name)

elif(hour>=12 and hour<15):
   print("Good Afternoon", name)

elif(hour>=15 and hour<18):
   print("Good Evening", name)

elif(hour>=18 and hour<0):
   print("Good Night", name)