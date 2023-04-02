year = 2400

is_leap = (year%4==0 and year % 100 !=0 ) or (year%400==0)

print("The condition of the given year being a leap year is", is_leap)