#Nama: Ananda Rachmawati Purwanto
#NIM : 24060123130061
# Pecahan

#Definisi dan spesifikasi konstruktor
def makeP(x,y):
    return [x,y]

def makePC(bil,n,d):
    if n< d:
        return [bil,n,d]
    else:
        return [bil + (n//d), n%d, d]
    
#Definisi dan spesifikasi selektor
def pembilang(p):
    return(p[0])

def penyebut(p):
    return(p[1])

def bil(p):
    return(p[0])

def n(p):
    return(p[1])
def d(p):
    return(p[2])
    
#Definisi, spesifikasi, realisasi dan aplikasi operator
def konversiPecahan(p):
    if (bil(p)>= 0):
        return makeP(bil(p)*d(p)+n(p),d(p))
    else:
        return makeP(bil(p)*d(p)-n(p),d(p))

def konversiReal(p):
    if (bil(p)>= 0):
        return (bil(p)*d(p)+n(p)/d(p))
    else:
        return (bil(p)*d(p)-n(p)/d(p))

def AddP(p1,p2):
    return makeP(((pembilang(p1)*penyebut(p2))+(pembilang(p2)*penyebut(p1))), penyebut(p1)*penyebut(p2))

def subP(p1,p2):
        return makeP(((pembilang(p1)*penyebut(p2))-(pembilang(p2)*penyebut(p1))), penyebut(p1)*penyebut(p2))


def divP(p1,p2):
    return makeP((pembilang(p1)*penyebut(p2)), (pembilang(p2)*penyebut(p1)))

def mulP(p1,p2):
    return makeP((pembilang(p1)*pembilang(p2)),( penyebut(p1)*penyebut(p2)))

#Definisi, spesifikasi,realisasi dan aplikasi predikat
def isEqP(p1,p2):
    if  pembilang(p1) * penyebut(p2) == pembilang(p2) * penyebut(p1):
        return True
    else:
        False

def isLtP(p1,p2):
    if (pembilang(p1)*penyebut(p2)) < (pembilang(p2))*(penyebut(p1)):
        return True
    else:
        return False

def isGtP(p1,p2):
    if (pembilang(p1)*penyebut(p2)) > ((pembilang(p2))*(penyebut(p1))):
        return True
    else:
        return False
    
#Aplikasi
print(konversiPecahan(makePC(2,7,5)))
print(konversiReal(makePC(2,4,6)))
print(AddP(makeP(1,4), makeP(1,4)))
print(subP(makeP(2,4), makeP(2,4)))
print(mulP(makeP(1,4), makeP(1,4)))
print(isEqP(makeP(2,3), makeP(2,3)))
print(isLtP(makeP(2,7), makeP(2,3)))
print(isGtP(makeP(2,7), makeP(2,3)))

