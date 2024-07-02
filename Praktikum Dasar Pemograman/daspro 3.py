
def hargaAlatTulis(a,b,c):
    pensil = a * (2000) 
    buku = b * (5000) 
    pulpen = c * (3000) 
    Jumlah_Harga = pensil + buku + pulpen
    return Jumlah_Harga 

a = int(input("harga pensil"))
b = int(input("harga buku"))
c = int(input("harga pulpen"))

print(hargaAlatTulis(a,b,c))

def cekBilangan(x):
    if (x==0):
        return "nol"
    else:
        if (x>0):
            return "positif"
        else:
            return "negatif"

print(cekBilangan(6))


