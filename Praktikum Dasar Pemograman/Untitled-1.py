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

def isEmpty(L):
    if L == []:
        return True
    else:
        return False

def NbElmt(L):
    if isEmpty(L) == True:
        return 0
    else:
        return 1 + NbElmt(Tail(L))
    
def isMember(x,L):
    if isEmpty == True:
        return False
    else:
        if first_elmt(L)==x:
            return True
        else:
            return isMember(x, Tail(L))
        
def copy(L):
    if isEmpty(L) == True:
        return []
    else:
        return Konso(first_elmt(L),copy(Tail(L)))
    
def Inverse(L):
    if isEmpty(L):
        return []
    else:
        return Konsi(Inverse(Tail(L)), first_elmt(L))

def isEqual(L1,L2):
    if isEmpty(L1)== True and isEmpty(L2)== True :
        return True
    elif isEmpty(L1)== True and isEmpty(L2)== False:
        return False
    elif isEmpty(L1)== False and isEmpty(L2)== True:
        return False
    
    else:
        if first_elmt(L1) == first_elmt(L2):
            return isEqual(Tail(L1), Tail(L2))
        else:
            return False
        
def ElmntKeN(N,L):
    if N == 1:
        return first_elmt(L)
    else:
        return ElmntKeN(N-1, Tail(L))

def Konkat(L1,L2):
    if isEmpty(L1) == True:
        return L2
    else:
        return Konso(first_elmt(L1), Konkat(Tail(L1),L2))


print( Konkat([1,2,3],[4,5,6]))
print (isEqual([1,2,3], [4,5,6]))
print (isEqual([], [4,5,6]))
print (ElmntKeN(2, [4,5,6]))
print( NbElmt([1,3,5]))
print(isMember(3,[1,2,3]))
print(copy([1,2,3]))
print(Inverse([1,4,5]))
