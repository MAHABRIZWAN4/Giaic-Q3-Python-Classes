import time # This is required to include time module.
ticks = time.time()
print(ticks)   #  This will print the number of seconds since the epoch (January 1, 1970)


localtime = time.localtime(time.time())
print ("Local current time :", localtime)


t1 = time.localtime()
print("Local current time :", t1)
print(t1.tm_year) # 2025
print(t1.tm_gmtoff)


localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time :", localtime)



# tm_year=2025 → Saal
# tm_mon=4 → Mahina (April)
# tm_mday=1 → Date (1st)
# tm_hour=23 → Ghanta (11 PM)
# tm_min=26 → Minute
# tm_sec=38 → Second
# tm_wday=1 → Din (Monday, kyunki Sunday = 0)
# tm_yday=91 → Year ka 91st day (April 1)
# tm_isdst=0 → Daylight saving time off hai.

# time.time() → Seconds since January 1, 1970.

# time.localtime() → Us seconds ko local time me convert karta hai.

# time.asctime() → Structured time ko readable format 
# (jaise "Thu Apr 1 23:26:38 2025") me convert karta hai.


import calendar
cal = calendar.month(2025, 4) # 2025 ka April month ka calendar print karega.
print ("Here is the calendar:")
print (cal)


from datetime import date

date1 = date(2023, 4, 19)
print("Date1:", date1)   #  date(2023, 4, 19)
date2 = date(2023, 4, 30)
print("Date2:", date2)   # date(2023, 4, 30)


import datetime

x = datetime.datetime.now() #The date contains year, month, day, hour, minute, 
# second, and microsecond.
print(x)

time.sleep(5) # 5 seconds ka sleep karega.







