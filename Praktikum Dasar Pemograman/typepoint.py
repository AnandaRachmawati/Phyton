#Nama File  : typepoint.py
#Deskripsi  : Membuat tipe point beserta konstruktor dan selektornya
#Pembuat    : 
#Tanggal    :  

#DEFINISI TYPE
# type point : <x=real, y=real>
#   {x=real, y=real adalah sebuah point dimana x sebagai absis dan y sebagai ordinat}

#DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# make_point : 2 real --> point
#   {make_point(a,b) membentuk point dari a dan b dimana a sebagai absis dan b sebagai ordinat}
#Realisasi dalam Python
def point (a,b):
    return [a,b]

#DEFINISI DAN SPESIFIKASI SELEKTOR DENGAN FUNGSI
# absis : point --> real
#   {absis(P) menentukan nilai absis pada point P}
#Realisasi dalam Python
def absis (p):
    return(p[0])

# ordinat : point --> real
#   {ordinat(P) menentukan nilai ordinat pada point P}
#Realisasi dalam Python
def ordinat(p):
    return (p[1])

#DEFINISI DAN SPESIFIKASI PREDIKAT
# isOrigin : point --> boolean
#   {isOrigin(P) menentukan apakah point berada di posisi(0,0)}
#Realisasi dalam Python
def isOrigin(p):
    if absis(p) == 0 and ordinat(p)==0:
        return True

#DEFINISI DAN SPESIFIKASI OPERATOR TERHADAP POINT
# jarak : 2 point --> integer
#   {jarak(P1,P2) jarak dari 2 titik}
#Realisasi dalam Python
from math import sqrt


# jarak0 : point --> integer
#   {jarak0(P1) jarak dari titik terhadap titik pusat koordinat (0,0)}
#Realisasi dalam Python
def Jarak(p1,p2):
    return (sqrt((absis(p1)-absis(p2))**2 + (ordinat(p1)-ordinat(p2))**2))

# kuadran   : point --> integer
#   {kuadran(P) mengembalikan kuadran dimana point P berada, dengan syarat P bukan titik origin dan tidak terletak di sumbu X atau Y}
#Realisasi dalam Python
def Kuadran (p):
    if absis(p) !=0 and ordinat(p) !=0:
        if absis(p)>0 and ordinat(p)>0:
            return 1
        elif absis(p)<0 and ordinat(p)>0:
            return 2
        elif absis (p)<0 and ordinat(p)<0:
            return 3
        elif absis(p)>0 and ordinat(p)<0:
            return 4
    else:
        return 0

############################################################################################################################
#APLIKASI KONSTRUKTOR
print(point(6,7))
#APLIKASI SELEKTOR
p = point (1,5)
print(p[0])
print(p[1])
#APLIKASI PREDIKAT
print(isOrigin(point(0,0)))
#APLIKASI OPERATOR
print(Jarak(1,5))


    

    