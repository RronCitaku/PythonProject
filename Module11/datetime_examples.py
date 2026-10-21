import datetime

now = datetime.datetime.now()
print(now)

print("Year: ", now.year)
print("Month: ", now.month)
print("Day: ", now.day)
print("Hour: ", now.hour)
print("Minute: ", now.minute)
print("Second: ", now.second)
print("Microsecond: ", now.microsecond)

current_date = datetime.datetime.now().date()
print(current_date)
print("Year: ", current_date.year)
print("Month: ", current_date.month)
print("Day: ", current_date.day)