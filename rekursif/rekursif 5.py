def makeDate(d,m,y):
    return [d,m,y]

def Day(D):
    return D[0]

def Month(D):
    return D[1]

def Year(D):
    return D [2]

def IsKabisat(a):
    if ((a % 4 == 0) and (a % 100 !=0)) or a % 400 == 0:
        return True
    else:
        return False

def NextDay(D):
    if Month(D) == 8 or Month(D) == 3 or Month(D)==5 or Month(D)==7 or Month(D)== 10:
        if Day(D) < 31:
            return makeDate(Day(D) + 1, Month(D), Year(D))
        else:
            return makeDate(1, Month(D) +1 , Year(D))
        
    elif Month(D) == 2:
        if Day(D) < 28:
            return makeDate(Day(D) + 1, Month(D), Year(D))
        elif IsKabisat(Year(D)):
            if Day(D) == 28:
                return makeDate(Day(D) + 1, Month(D), Year(D))
            else:
                return makeDate(1, Month(D) + 1, Year(D))
        else:
            return makeDate(Day(D), Month(D) + 1, Year(D))
    
    elif Month(D)== 4 or Month(D)== 6 or Month(D)==9 or Month(D)==11:
        if Day(D) < 30 :
            return makeDate(Day(D)+1, Month(D), Year(D))
        else:
            return makeDate(1, Month(D)+1, Year(D))
    elif Month(D) == 12:
        if Day(D) < 31 :
            return makeDate(Day(D)+1, Month(D), Year(D))
        else: 
            return makeDate(1,1, Year(D) +1)
        
def NextNday(D,n):
    if n == 0:
        return D
    else:
        return NextNday(NextDay(D),n-1)
    
print(NextNday(makeDate(21,2,2004),3))
print(NextNday(makeDate(29,2,2004),3))
print(NextNday(makeDate(31,4,2004),3))