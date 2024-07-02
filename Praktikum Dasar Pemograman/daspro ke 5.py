def point(x,y):
    return [x,y]

def absis(p):
    return (p[0])

def ordinat (p):
    return (p[1])

def gradient(p1,p2):
    return (ordinat(p2)-ordinat(p1))/(absis(p2)- absis(p1))

def jarakTerpendek(p1,p2):
    if (((ordinat(p1))**2 + absis(p1)**2)**0.5 ) < (((ordinat(p2))**2 + absis(p2)**2)**0.5 ):
        return point(absis(p1),ordinat(p1))
    else:
        return point(absis(p2),ordinat(p2))

p1 = [5,5]
p2 = [9,10]

print(gradient(p1,p2))
print(jarakTerpendek(p1,p2))


# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# make_layang2: 2 float --> float

# REALISASI
def make_layang2(a,t):
    return [a,t]

def d1(a):
    return (a[0])

def d2(a):
    return (a[1])

def luas(p):
    return 0.5*(d1(p) * d2(p))

print(luas(make_layang2(4.0, 6.0)))
print(luas(make_layang2(4.3, 7.2)))
print(luas(make_layang2(3.9, 6)))


    

def make_jajargenjang(a,t):
    return [a,t]

def A(a):
    return (a[0])

def T(a):
    return (a[1])

def luas(p):
    return (A(p) * T(p))

print(luas(make_jajargenjang(5.0, 6.0)))
print(luas(make_jajargenjang(3.3, 8.2)))
print(luas(make_jajargenjang(4.9, 5)))
# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# make_mhs: string, 2 integer --> mahasiswa
# make_mhs(nama,nilai_uts,nilai_uas) membentuk sebuah tipe bentukan mahasiswa yang berisikan nama, nim, dan ipk.
# REALISASI
def make_mhs(nama,nim, ipk):
    return [nama,nim,ipk]

def namaMhs(a):
    return (a[0])

def nimMhs(a):
    return (a[1])

def ipk(a):
    return (a[2])

def cek_ipk(p):
    if 3.5 < ipk(p) > 4.0:
        return "TRUE"
    else:
        return "FALSE"

def nama_mhs(p):
    return namaMhs(p)

def banyak_sks(p):
    if ipk(p) < 2.0:
        return '18 sks'
    elif 2.0 <= ipk(p) <= 2.49:
        return '20 sks'
    elif 2.5 <= ipk(p) <= 2.99:
        return '22 sks'
    elif 3.0 <= ipk(p) <= 4.0:
        return '24 sks'

print(cek_ipk(make_mhs('Dengklek', '123456', 4.0 )))
print(nama_mhs(make_mhs('Dengklek', '123456', 4.0 )))
print(banyak_sks(make_mhs('Dengklek', '123456', 4.0 )))