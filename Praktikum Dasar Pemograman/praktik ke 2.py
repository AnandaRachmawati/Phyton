gunting = 5 #ini namanya variabel global

def kamar1 ():
    kertas = 3  # kalo ini variaibel lokal
    return gunting - kertas
print (kamar1()) # omg lu harus tau nan kalo parameter bisa () * emot  nangies


#realisasi
def tambahDuaBilangan(x,y):
    return x + y

print(tambahDuaBilangan(4,7))

def hargaAlatTulis(a,b,c):
      return (a * 2000 + b * 5000 + c * 3000)
       
a = int(input())
b = int(input())
c = int(input())

print(hargaAlatTulis(2,3,2))