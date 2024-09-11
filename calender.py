import calendar

def display_calendar():
    
    year = int(input("Enter year: "))
    month = int(input("Enter month: "))
    
    cal = calendar.TextCalendar(calendar.SUNDAY)
    
    month_calender = cal.formatmonth(year, month)
    print(month_calender)
    
    display_calendar()