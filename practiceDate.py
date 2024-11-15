# Task 3
# from datetime import datetime

# input= "1 января 2014 14:43:33"
# date_time_obj = datetime.strptime(input, "%d %B %Y %H:%M:%S")
# output= date_time_obj.strftime("%Y-%m-%d %H:%M:%S")
# print(output)


# Task 4
# from datetime import datetime
# current = datetime.now()
# formatted = current.strftime("%H:%M:%S.%f")
# print(formatted)

# Task 3.1

from datetime import datetime

mondays = 0
for year in range(2015, 2017):
    for month in range(1, 13):
        date = datetime(year, month, 1)
        if date.weekday() == 0: 
            mondays += 1

print(f"{mondays}")

# Task 4.1
import time

string = "Привет,как дела"

for _ in range(5):
    print(string)
    time.sleep(3)

# Task 5
from datetime import datetime, timedelta

current = datetime.now()
date_30_days_ago = current - timedelta(days=30)
date_30_days_after = current + timedelta(days=30)

print("30 дней назад:", date_30_days_ago.strftime("%Y-%m-%d"))
print("через 30 дней:", date_30_days_after.strftime("%Y-%m-%d"))


