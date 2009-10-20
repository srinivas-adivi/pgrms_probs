months = [(31,31), (28,29), (31,31), (30,30), (31,31),
          (30,30), (31,31), (31,31),(30,30), (31,31), (30,30), (31,31)]

#1stJan 1900 was Monday
def problem19():
    result = 0
    starting_day = 0
    Dec31st1900 = find_day_31stDec(1901, starting_day)
    start_of_month = (Dec31st1900+1)%7
    for year in range(1901, 2001):
        value = is_it_leapYear(year)
        for days in map(lambda x: x[value], months):
            increment = start_of_month==6 and 1 or 0
            result = result + increment
            end_of_month = (days+start_of_month-1)%7
            start_of_month = (end_of_month+1)%7

    return result

def find_day_31stDec(year, starting_day):
    value = is_it_leapYear(year) and 1 or 0
    days_months = map(lambda x : x[value], months)
    total_days = sum(days_months)
    
    remainder = (total_days+starting_day-1)%7
    
    return remainder
            
def is_it_leapYear(year):
    div1, mod1 = divmod(year, 100)
    div2, mod2 = mod1 and divmod(year, 4) or divmod(div1, 4)

    return not mod2

print problem19()
