import datetime

# datetime() class constructor of the datetime module requires three parameters to create a date object: year, month, day.
# Note - The datetime() class also takes parameters for time and timezone (hour, minute, second, microsecond, tzone),
# but they are optional, and has a default value of 0, & (None for timezone).
# Create a date object:

# to display the current date & time-
myTime = datetime.datetime.now()
print("date is- ", myTime.day, '-', myTime.month, '-', myTime.year, '& time is- ',
      myTime.hour, ':', myTime.minute, ':', myTime.second, ':', myTime.microsecond)

x = datetime.datetime(2020, 5, 17)
print(x)

# The datetime class has a method for formatting date objects into readable strings.
# strftime() - string format for time

print("full week day-", myTime.strftime("%A"))
print("week day with 3 letters-", myTime.strftime("%a"))
print("Weekday as a number-", myTime.strftime("%w"))
print("Day 01-31 -", myTime.strftime("%d"))
print("full month name-", myTime.strftime("%B"))
print("Month name with 3 letters-", myTime.strftime("%b"))
print("month 01-12 -", myTime.strftime("%m"))
print("full year-", myTime.strftime("%Y"))
print("year with 2 letter-", myTime.strftime("%y"))
print("Hour 00-23 -", myTime.strftime("%H"))
print("Hour 00-12 -", myTime.strftime("%I"))
print("am/pm -", myTime.strftime("%p"))
print("Day number 001-366 -", myTime.strftime("%j"))
print("Week number 00-53 -", myTime.strftime("%U"))  # if sunday is first day  of week
print("Local version of date- ", myTime.strftime("%x"))
print("Local version of time- ", myTime.strftime("%X"))
