#12. Write a Python program that prints the calendar for a given month and year.
#Note : Use 'calendar' module.
import calendar

year = int(input("Enter the year: "))
mon = int(input("Enter the month: "))
print(calendar.month(year,mon))