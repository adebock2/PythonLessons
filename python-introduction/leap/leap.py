def leap_year(year):
    bolleap = False
    if year % 4 == 0:
        bolleap = True
    else:
        bolleap = False
        if year % 400 == 0:
            bolleap = True
        else:
            bolleap = False
            if year % 100 == 0:
                bolleap = True
            else:
                bolleap = False
    return bolleap
    