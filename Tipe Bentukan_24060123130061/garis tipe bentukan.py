#Nama: Ananda Rachmawati Purwanto
#NIM : 24060123130061
# Garis

#Definisi dan spesifikasi konstruktor
def point(x,y):
    return[x,y]

def makeGaris(m,n):
    return[m,n]

#Definisi dan spesifikasi selektor
def absis(a):
    return(a[0])

def ordinat(a):
    return (a[1])

def makeGaris(m,n):
    return[m,n]

def p1(p):
    return (p[0])

def p2(p):
    return(p[1])

#Definisi, spesifikasi, realisasi dan aplikasi operator
def gradien(G):
    return ordinat(p2(G))- ordinat(p1(G))/ absis(p2(G))- absis(p1(G))

def panjangGaris(G):
    return ((absis(p2(G))- absis(p1(G)))**2 + (ordinat(p2(G))- ordinat(p1(G)))**2)**0.5

#Definisi, spesifikasi,realisasi dan aplikasi predikat 
def IsSejajar(G1,G2):
    if gradien(G1) == gradien(G2):
        return True
    else:
        return False

def IsTegakLurus(G1,G2):
    if gradien(G1) * gradien(G2) == -1:
        return True
    else: 
        return False

#Aplikasi
G1 = makeGaris(point(2,7),point(8,9))
G2 = makeGaris(point(2,2),point(8,6))
print(gradien(G1))
print(panjangGaris(G2))
print(IsSejajar(G1,G2))
print( IsTegakLurus(makeGaris(point(2,2), point(6,4)),makeGaris(point(2,2),point(4,6))))


