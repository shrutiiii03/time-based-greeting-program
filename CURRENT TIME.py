import time

hour = int(time.strftime("%H"))
print("current hour is ", hour)

if hour < 12 and  hour >= 4:
    print("good morning")
elif (hour <= 3 or hour == 0) or hour >= 20:
    print("good night")
elif hour <= 16 and hour >= 12:
    print("good afternoon")
elif hour < 20 and hour > 16:
    print("good evening")








    
