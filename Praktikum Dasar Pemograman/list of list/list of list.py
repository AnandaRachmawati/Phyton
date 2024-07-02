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

def Konslo(L,S):
    return [L] + S

def Konsli(S,L):
    return S + [L]

def firstList(L):
    return L[0]

def lastList(S):
    return S[-1]

def headList(S):
    return S[:-1]

def tailList(S):
    return S[1:]

def isEmpty(S):
    if S == []:
        return True
    else:
        return False
def NbElmt(S):
    if isEmpty(S) == True:
        return 0
    else:
        return 1 + NbElmt(tailList(S))
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
    
def isOneElmt(S):
    return len(S) == 1



def isEqual(S1,S2):
    if isEmpty(S1)== True and isEmpty(S2)== True :
        return True
    elif isEmpty(S1)== True and isEmpty(S2)== False:
        return False
    elif isEmpty(S1)== False and isEmpty(S2)== True:
        return False
    
    else:
        if isAtom(firstList(S1)) == isAtom(firstList(S2)):
            return firstList(S1) == firstList(S2) and isEqual(tailList(S1),tailList(S2))
        elif isList(firstList(S1) and isList(firstList(S2))):
            return isEqual(firstList(S1), firstList(S2)) and isEqual(tailList(S1),tailList(S2))
        else:
            return False

# print(isEqual([],[[4],5]))

# print(isEqual([1,[2]],[1,[2]]))

def isMember(A,S):
    if isEmpty(S):
        return False
    else:
        if isAtom(firstList(S)):
            return A == firstList(S) or isMember(A, tailList(S))
        elif isList(firstList(S)):
            return isMember(A, firstList(S)) or isMember(A, tailList(S))
        
# print(isMember(1,[]))
# print(isMember(3,[1,[2,3]]))

def rember(a,S):
    if isEmpty(S):
        return S
    else:
        if isList(firstList(S)):
            return Konslo(rember(a, firstList(S)), rember(a, tailList(S)))
        else:
            if first_elmt(S)==S:
                return rember(a, tailList(S))
            else:
                return Konslo(first_elmt(S), rember(a, Tail(S)))
            
# print(rember(1,[2,[5,1]]))

def max2 (a,b):
    if a <= b :
        return b
    else:
        return a
        
def max(S):
    if isOneElmt(S):
        if isAtom(firstList(S)) == True:
            return firstList(S)
        else:
            return max(firstList(S))
    else:
        if isAtom(firstList(S))== True :
            return max2(firstList(S), max(tailList(S)))
        else:
            return max2(max(firstList(S)), max (tailList(S)))
print(max([1,[5,[6]],[8]]))

