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

current_time = datetime.datetime.now().time()
print("Hour: ", current_time.hour)
print("Minute: ", current_time.minute)
print("Second: ", current_time.second)
print("Microsecond: ", current_time.microsecond)

specific_date = datetime.date(2025, 4, 5)
specific_time = datetime.time(12, 30,0)
print(specific_date)
print(specific_time)

duration = datetime.timedelta(days=5, hours=3)

new_date = current_date + duration
print(new_date)

previous_date = current_date - duration
print(previous_date)

utc_time = datetime.datetime.now(datetime.timezone.utc)
print("Current UTC time: ", utc_time)

custom_offset = datetime.timedelta(hours=3)
custom_time = utc_time.replace(tzinfo=datetime.timezone(custom_offset))
print("Current time in custom time zone (UTC+3): ", custom_time)