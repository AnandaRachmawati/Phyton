def Konslo(e,L):
    return [e] + L

def Konsli(L,e):
    return L + [e]

def firstList(L):
    return L[0]

def lastList(L):
    return L[-1]

def headList(L):
    return L[:-1]

def tailList(L):
    return L[1:]

def isEmpty(L):
    if L == []:
        return True
    else:
        return False
def NbElmt(L):
    if isEmpty(L) == True:
        return 0
    else:
        return 1 + NbElmt(tailList(L))
def isAtom(S):
    if type(S) != list:
        return True
    else:
        return False
    
def isList(S):
    if type(S) == list:
        return True
    else:
        return False
    
def isOneElmt(L):
    return len(L) == 1

def jumlahList(L):
    if isEmpty(L):
        return 0
    else:
        return firstList(L) + jumlahList(tailList(L))
    
#6
def min2 (a,b):
    if a <= b :
        return b
    else:
        return a 
        
def MinList(S):
    if isOneElmt(S):
        if isAtom(firstList(S)):
            return firstList(S)
        else:
            return MinList(firstList(S))
    else:
        if isAtom(firstList(S))   :
            return min2(firstList(S), MinList(tailList(S)))
        else:
            return min2(MinList(firstList(S)), MinList (tailList(S)))

print(MinList([3, [2, 4, 5], [6, 3], [6, 4, 1, 2], 7, [2]]) )



#7
def NBOdds(S):
    if isEmpty(S):
        return 0
    else:
        if isAtom(firstList(S)) == True and (firstList(S)) % 2 != 0:
            return 1 + NBOdds(tailList(S))
        elif isAtom(firstList(S)) == True and (firstList(S)) %2 == 0:
            return NBOdds(tailList(S))
        else: 
            return NBOdds(firstList(S)) + NBOdds(tailList(S))
print(NBOdds([3, [2, 4, 5], [6, 3], [6, 4, 1, 2], 7, [2]]))




#8
def MakeListAtom(S):
    if isEmpty(S):
        return []
    else:
        if isAtom(firstList(S)) == False:  
            return Konslo(jumlahList(firstList(S)), MakeListAtom(tailList(S)))
        else:
            return Konslo(firstList(S), MakeListAtom(tailList(S)))

print(MakeListAtom([3, [2, 4, 5], [1, 3], [6, 4, 1, 2], 7, [2]]))