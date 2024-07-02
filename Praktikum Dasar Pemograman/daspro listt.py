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
    
def isOneElmt(L):
    return len(L) == 1

def NbElmt(L):
    if isEmpty(L) == True:
        return 0
    else:
        return 1 + NbElmt(Tail(L))
def dimensi(L):
    if isEmpty(L):
        return 0
    else:
        return 1 + dimensi(Tail(L))


# def HapusNilai(hapus,X):
#     if isEmpty(X):
#         return X
#     else:
#         if first_elmt(X) == hapus:
#             return HapusNilai(hapus, Tail(X))
#         else:
#             return Konso(first_elmt(X), HapusNilai(hapus, Tail(X)))
  
  
# # def Tia(L1,L2):
     
# # print(HapusNilai(69,[60, 70, 69, 73, 90, 100, 99, 89, 59])) 
# # print(HapusNilai(100,[50, 90, 100, 89, 70, 65, 76, 99])) 
# # hapus = [int(x) for x in input().split()]
# # X = int(input())
def gaji(A, B):
    if isEmpty(A) or isEmpty(B):
        return 0
    if first_elmt(A) > first_elmt(B):
        return 1 + gaji(Tail(A), Tail(B))
    elif first_elmt(A) < first_elmt(B):
        return -1 + gaji(Tail(A), Tail(B))
    else:
        return gaji(Tail(A), Tail(B))

def perusahaanTia(A, B):
    if gaji(A, B) > 0:
        return 'A'
    elif gaji(A, B) < 0:
        return 'B'
    else:
        return 'A B'

print(perusahaanTia([32, 30, 44, 94], [19, 91, 5, 34]))
    
print(perusahaanTia([32, 30 ,44 ,94], [19 ,91 ,5 ,34]))
