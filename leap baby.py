def is_leap_baby(day,month,year):
    if year%4==0:
        if year%100==0 and year%400!=0:
            return False
        else:
            if month==2:
                if day==29:
                    return True
                return False
    else:
        return False
       
def output(status,name):
    if status:
        print "%s is one of an extremely rare species. He is a leap year baby!" % name
    else:
        print "There's nothing special about %s's birthday. He is not a leap year baby!" % name


output(is_leap_baby(29, 2, 1996), 'Calvin')

output(is_leap_baby(19, 6, 1978), 'Garfield')

output(is_leap_baby(29, 2, 2000), 'Hobbes')

output(is_leap_baby(29, 2, 1900), 'Charlie Brown')

output(is_leap_baby(28, 2, 1976), 'Odie')
