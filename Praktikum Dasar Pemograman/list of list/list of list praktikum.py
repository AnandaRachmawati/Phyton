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

def IsEmptyLoL(S):
    return S == []
  
def IsOneElement(S):
    if IsEmptyLoL(S):
        return False
    else:
        return IsEmptyLoL(tailList(S))
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


def JumlahKartu(S):
    if isEmpty(firstList(S)) :
        return 0
    else:
        if isAtom(firstList(S)):
            return 1 + JumlahKartu(tailList(S))
        else:
            return JumlahKartu(firstList(S)) + JumlahKartu(tailList(S))
    

# print(JumlahKartu([[]]))

# def HindariMonster(a, S):
#     if isEmpty(S):
#         return S
#     else:
#         if isAtom(firstList(S)) == True and (firstList(S)) % a != 0:
#             return Konslo(firstList(S)), HindariMonster(a, tailList(S))
#         elif isAtom(firstList(S)) == True and (firstList(S)) % a == 0:
#             return HindariMonster(a, tailList(S))
#         else: 
#             return Konslo(HindariMonster(a, firstList(S)) , HindariMonster(a, tailList(S)))  
        
# def HindariMonster(a, S):
#     if isEmpty(S):
#         return S
#     else:
#         if isAtom(firstList(S)) and (firstList(S) % a != 0):
#             return Konslo(firstList(S), HindariMonster(a, tailList(S)))
#         elif isAtom(firstList(S)) and (firstList(S) % a == 0):
#             return HindariMonster(a, tailList(S))
#         else:
#             return Konslo(HindariMonster(a, firstList(S)), HindariMonster(a, tailList(S)))

def HindariMonster(a, S):
    if isEmpty(S):
        return S
    else:
        if isAtom(firstList(S)) == True and (firstList(S)) % a != 0:
            return Konslo(firstList(S), HindariMonster(a, tailList(S)))
        elif isAtom(firstList(S)) == True and (firstList(S)) % a == 0:
            return HindariMonster(a, tailList(S))
        else: 
            return Konslo(HindariMonster(a, firstList(S)) , HindariMonster(a, tailList(S)))  
print(HindariMonster(3, [3, [2, 4, 5], [6, 3], [6, 4, 1, 2], 7, [2]]))

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

def listKosong(b):
    if IsEmptyLoL(b):
        return 0
    else: 
        if IsEmptyLoL(firstList(b)):
            return 1 + listKosong(tailList(b))
        else:
            return listKosong(tailList(b))
    
def KacangRisu(L, S):
    if listKosong(S) < NbElmt(L)-2: 
        return "Mending Pulang"
    elif IsEmptyLoL(L) or IsEmptyLoL(S): 
        return S
    else: 
        if IsEmptyLoL(firstList(S)): 
            return Konslo(Konslo(firstList(L),firstList(S)),KacangRisu(tailList(L),tailList(S)))
        else:
            return Konslo(firstList(S),KacangRisu(L,tailList(S)))
# # Example usage:
print(KacangRisu([1, 2, 3], [[], [1, 2, 3], [], []]))

def max2 (a,b):
    if a <= b :
        return b
    else:
        return a

# def PeringkatPertama(S):
#     if isOneElmt(S):
#         return (firstList(S))
#     else:
#         if isList(tailList(S)) < isList(tailList(tailList(S))):
#             return (isList(firstList(S)))
#         else:
#             return PeringkatPertama(isList(tailList(S)))    
def peringkat1(S):
    if IsOneElement(S):
        return firstList(S)
    else:
        if firstList(S)[1] >= peringkat1(tailList(S))[1]:
            return firstList(S)
        else:
            return peringkat1(tailList(S))
        
def PeringkatPertama(S):
    return firstList(peringkat1(S))

      
# print(PeringkatPertama([["Nagisa Shiota", 80], ["Manami Okuda", 85], ["Kaede Kayano", 85]]))
# print(PeringkatPertama([["Nagisa Shiota", 80]]))



