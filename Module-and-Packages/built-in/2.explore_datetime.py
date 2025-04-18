from datetime import datetime, time, date, timedelta, timezone

# Get the current date and time
print(datetime.now())

# Get the fixed time
print(time(hour=20, minute=10, second=50))

# Get UTC timezone specific datetime
print(datetime.now(timezone.utc))

# Get the current date
today = date.today()
print(today)

days_before_seven = datetime.now() - timedelta(days=7)
print(days_before_seven)

days_after_seven = datetime.now() + timedelta(days=78)
print(days_after_seven)

format = "%d - %m - %y"
print(datetime.now().strftime(format))

format = "%A"
print(days_after_seven.strftime(format))

# Date object representing data in Python
my_date = date(2025, 4, 13)
print(my_date)

# Get the Current Date
todays_date = date.today()
print(todays_date)

# Get Today’s Year, Month, and Date
this_year = todays_date.year
print(this_year)

this_month = todays_date.month
print(this_month)

this_day = todays_date.day
print(this_day)

# Get Date from Timestamp
date_time = datetime.fromtimestamp(time)
print(date_time)
