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

def MakeListAtom(S):
    if isEmpty(S):
        return []
    else:
        if isList(firstList(S)):  
            return Konslo(jumlahList(firstList(S)), MakeListAtom(tailList(S)))
        else:
            return Konslo(firstList(S), MakeListAtom(tailList(S)))

print(MakeListAtom([3, [2, 4, 5], [1, 3], [6, 4, 1, 2], 7, [2]]))






       
                    