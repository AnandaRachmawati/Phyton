# Ananda Rachmawati P (24060123130061)
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
    

# def isOneElmt(L):
#     if isEmpty(L):
#         return False
#     else:
#         if first_elmt(L) == True and isEmpty(Tail(L)):
#             return True
#         else:
#             return False

# print(isOneElmt([1]))
# print(isOneElmt([1,3]))
# print(isOneElmt([]))

def isOneElmt(L):
    return len(L) == 1

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

def MultiRember(x,L):
    if isEmpty(L):
        return L
    else:
        if first_elmt(L) == x:
            return MultiRember(x, Tail(L))
        else:
            return Konso(first_elmt(L), MultiRember(x, Tail(L)))

#nilai maksimum kedua dari sebuah list.
def max(a, b):
    if a <= b:
        return b
    else:
        return a
            
def maxList1(L):
    if isOneElmt(L):
        return last_elmt(L)
    else:
        return max(last_elmt(L), maxList1(Head(L)))

def MaxList2(L):
    if isOneElmt(L):
        return []
    else:
        if maxList1(L) == last_elmt(L):
            return MaxList2(Head(L))
        else:
            return maxList1 (MultiRember(maxList1(L),L))
     
print(MaxList2([2, 6, 10, 99, 100, 20]))
print(MaxList2([28, 9, 11, 55, 25, 8]))

# perkalian tiap elemen list
def kaliList(L1,L2):
    if isEmpty(L1) or isEmpty(L2) :
        return []
    else:
        return Konso(first_elmt(L1)*first_elmt(L2) ,kaliList(Tail(L1),Tail(L2) ))

# print(kaliList([2, 4, 6], [1, 2, 3]))
# print(kaliList([7, 5, 10], [2, 2, 2]))

#menghitung banyaknya kemunculan elemen x
def NBElmtX(x, L):
    if L == '':
        return 0
    else:
        if x == first_elmt(L):
            return 1 + NBElmtX(x, Tail(L))
        else:
            return NBElmtX(x, Tail(L))


# print(NBElmtX('a','ananda'))
# print(NBElmtX('o', 'ilmu komputer dan informatika'))


#cek palindrom
def CekPalindrom (T):
    if T == '':
        return True
    else:
        if first_elmt(T) == last_elmt(T):
            return CekPalindrom(Head(Tail(T)))
        else:
            return False
        
# print(CekPalindrom("KODOK"))
# print(CekPalindrom('daspro'))

  

