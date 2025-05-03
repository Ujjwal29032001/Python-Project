# import time
# timestamp = time.strftime('%H:%M:%S')
# print(timestamp)
# timestamp = time.strftime('%H')
# print(timestamp)
# timestamp = timestamp('%M')
# print(timestamp)
# timestamp = timestamp('%S')
# # print(timestamp)     
# import time
# h=int(time.strftime('%H'))
# if h<12:
#     print("Good Morning Sir")
# elif h<17:
#     print("Good Afternoon Sir")
# else:
#     print("Good afternoon sir")

#Second Example
import time
timestamp=time.strftime("%H:%M:%S")
print(timestamp)
timestamp=int(time.strftime("%H"))
timestamp=int(input("Enter the Current time:"))
if timestamp>=12 and timestamp<17:
    print("Good Afternoon Sir")
elif timestamp<12 and timestamp>=0:
    print("Good Morning Sir")
elif timestamp<0 or timestamp>=24:
    print("Invalid! Enter the Correct time")
else:
    print("Good Night Sir ")


