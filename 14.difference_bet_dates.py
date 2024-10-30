#14. Write a Python program to calculate the number of days between two dates.
#Sample dates : (2014, 7, 2), (2014, 7, 11)
#Expected output : 9 days

from datetime import date
#start_date
s_date = date(2014, 7, 2)
#last_date
l_date = date(2014, 7, 11)

difference = l_date - s_date
print(difference.days)
