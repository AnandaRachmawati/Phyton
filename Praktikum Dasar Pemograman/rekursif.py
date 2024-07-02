# Nama File : rekursif.py
# Deskripsi : Membuat modul terkait fungsi rekursif
# Pembuat   : 
# Tanggal   : 

#Plus:integer --> integer
#{Plus(x,y) mengembalikan nilai x dijumlahkan dengan
#y dengan fungsi rekursif}
#Realisasi dalam python
def Plus(x,y):
    if y == 0:
        return x
    else:
        return 1 + Plus(x, y-1)
    

#Sub:integer --> integer
#{Sub(x,y) mengembalikan nilai x dikurangi dengan
# y dengan fungsi rekursif}
#Realisasi dalam python
def Min(x,y):
    if y == 0:
        return x
    else:
        return Min(x -1 , y-1)

#Mul:integer --> integer
#{Mul(x,y) mengembalikan nilai x dikali dengan 
# y dengan fungsi rekursif}
#Realisasi dalam python
def Mul(x,y):
    if y == 0:
        return 0
    else:
        return x + Mul(x, y-1)

#Dis:integer --> integer
#{Dis(x,y) mengembalikan nilai x dibagi dengan
# y dengan fungsi rekursif}
#Realisasi dalam python
def Dis(x,y):
    if y > x:
        return 0
    else:
        return  1 +  Dis(x-y, y)

#Exp:integer --> integer
#{Exp(x,y) mengembalikan nilai x dipangkat dengan
# y dengan fungsi rekursif}
#Realisasi dalam python
def Exp(x,y):
    if y == 0:
        return 1
    elif y == 1:
        return x
    else:
        return x * Exp(x, y-1 )

#Deretint:integer --> integer
#{Deretint(n) mengembalikan jumlah deret integer
# Deretint(6) = 1+2+3+4+5+6 , output 21}
#Realisasi dalam python
def Deretint(n):
    if n == 1:
        return 1
    else:
        return n + Deretint(n-1)

#Deretbeda3:integer --> integer
#{Deretbeda3(n) mengembalikan jumlah deret 
# aritmatika beda 3 dengan Deretbeda3(2) = 3+6, output 9}
#Realisasi dalam python
def Deretbeda3(n):
    if n == 1:
        return 3
    else:
        return 3*n + Deretbeda3(n-1)

#Deretgeo3:integer --> integer
#{Deretgeo3(n) mengembalikan jumlah deret 
# geometri r=3 dengan Deretgeo3(2) = 1+8+27, output 4}
#Realisasi dalam python
def Deretgeo3(n):
    if n ==1 :
        return 1
    else:
        return 1 + 
#Deretkubik:integer --> integer
#{Deretkubik(n) mengembalikan jumlah deret 
# dengan Deretkubik(3) = 1+4+9, output 14}
#Realisasi dalam python
#def Deretkubik(n):

print(Plus(5,4))
print (Min(5,3))
print (Min(8,3))
print(Mul(5,3))
print (Dis(15,3))
print (Dis(6,3))
print (Exp(2,3))
print (Exp(2,4))
print(Deretint(3))
print(Deretint(4))
print(Deretbeda3(2))
print(Deretbeda3(3))
