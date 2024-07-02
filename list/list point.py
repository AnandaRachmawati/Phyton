# Ananda Rachmawati P (24060123130061)
from math import sqrt
def point(x,y):
    return[x,y]

def absis(a):
    return(a[0])

def ordinat(a):
    return (a[1])

def Jarak(p1,p2):
    return (sqrt((absis(p1)-absis(p2))**2 + (ordinat(p1)-ordinat(p2))**2))

def Konso(e,L):
    return [e] + L
def Konsi(L,e):
    return L + [e]

def first_elmt(L):
    return L[0]

def last_elmt(L):
    return L[-1]

def Head(L):
    return L[:-1]

def Tail(L):
    return L[1:]

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
    
def isEmpty(L):
    if L == []:
        return True
    else:
        return False

def isOneElmt(L):
    return len(L) == 1

def min(a, b):
    if a <= b:
        return a
    else:
        return b

def NearestPoint(P,L):
    if isOneElmt(L):
        return first_elmt(L)
    else:
        if Jarak(P, first_elmt(L)) <= Jarak(P, first_elmt(Tail(L))):
            return NearestPoint(P, Konso(first_elmt(L), Tail(Tail(L))))
        else:
            return NearestPoint(P, Tail(L))
        
print(NearestPoint([1,2], [[0,0], [3,4], [6,7], [1,1], [2,1]]))