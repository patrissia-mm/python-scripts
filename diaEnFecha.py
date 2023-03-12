def isYearLeap(year):
    if(year%4==0):
        if(year%100==0):
            if(year%400==0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False
        
def daysInMonth(year, month):
    diasAnoBisiesto=[31,29,31,30,31,30,31,31,30,31,30,31]
    diasAnoNoBisiesto=[31,28,31,30,31,30,31,31,30,31,30,31]
    if(isYearLeap(year)):
        return diasAnoBisiesto[month-1]
    else:
        return diasAnoNoBisiesto[month-1]

def dayOfYear(year, month, day):
    sumaDias=0
    dia=0
    for ano in range(1,year):
        for mes in range(1,13):
            sumaDias=sumaDias+daysInMonth(ano,mes)
    sumaDias=sumaDias%7

    for mes in range(1,month):
        sumaDias+=daysInMonth(year,mes)

    sumaDias=sumaDias%7

    sumaDias+=(day)
    
    dia=sumaDias%7
    
    return dia
    
print(dayOfYear(2021, 5, 31))
print(dayOfYear(1982, 4, 12))
print(dayOfYear(2006, 6, 8))
print(dayOfYear(2007, 10, 10))
print(dayOfYear(1973, 9, 25))




