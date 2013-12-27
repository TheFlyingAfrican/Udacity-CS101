# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#

# determine if year is a leap year
def isLeapYear(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

# determine number of days from beginning of year to given date
def daysFromYearStart(year, month, day):
    month_with_30 = [4,6,9,11]
    month_with_31 = [1,3,5,7,8,10,12]

    total_days = 0
    #total number of days from 1/1 to month before given date
    if month != 1:
        for i in range(1, month):
            if i in month_with_30:
                total_days += 30
            elif i in month_with_31:
                total_days += 31
            elif i == 2:
                if isLeapYear(year):
                    total_days += 29
                else:
                    total_days += 28
    
    #add number of days in current month  
    total_days += day - 1      

    return total_days
    
    
        
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    num_years = year2 - year1
    num_leap_years = 0
    total_days = 0
    
    if num_years > 1:
        total_days = daysFromYearStart(year2, month2, day2)
    elif num_years == 1:
        if isLeapYear(year1):
            total_days = 366 - daysFromYearStart(year1, month1, day1)
        else:
            total_days = 365 - daysFromYearStart(year1, month1, day1)
        total_days += daysFromYearStart(year2, month2, day2)
    elif num_years == 0:
        total_days = daysFromYearStart(year2, month2, day2) - daysFromYearStart(year1, month1, day1)
        
    #determine number of leap years between periods excluding the years which we'll evaluate separately
    if (year1+1 < year2-1): 
        for i in range(year1+1, year2):
            if isLeapYear(i):
                num_leap_years = num_leap_years + 1
        total_days += (365 * num_years ) + num_leap_years
    
    return total_days 
    
# Test routine
def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"


test()
