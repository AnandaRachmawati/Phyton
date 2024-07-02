def namaHari(x):
    if (x==1):
        return "minggu"
    elif (x==2):
        return "senin"
    elif (x==3):
        return "selasa"
    elif (x==4):
        return "rabu"
    elif (x==5):
        return "kamis"
    elif (x==6):
        return "jumat"
    elif (x==7):
        return "sabtu"
    else:
        return "bukan hari"

print(namaHari(6))

def nilaiUjian(nilai):
    if ( 90 <= nilai <= 100):
        return "A"
    elif (  75 <= nilai < 89):
        return "B"
    elif (60 <= nilai < 75):
        return "C"
    elif (40 <= nilai < 60):
        return "D"
    elif ( 0 <= nilai < 40):
        return "E"
    else:
        return "Masukan angka nilai"
    
print(nilaiUjian(30))

def Ordinat(x,y):
    if (x==0 and y !=0):
        return "Titik berada di sumbu X"
    elif (y == 0 and x != 0):
        return "Titik berada di sumbu y"
    elif ( x==0 and y == 0):
        return "Titik berada di titik asal/origin"

print(Ordinat(1,7))


def minimalBelanja(a,b,c,d,e):
    total_belanja = (a*20000)+(b*7000)+(c*35000)+(d*5000)+(e*3000)
    if ( total_belanja >= 50000):
        result = (total_belanja - (10/100 * total_belanja))
    else:
        result = total_belanja
    return int(result)

a= int(input())
b= int(input())
c= int(input())
d= int(input())
e= int(input())

print("Rp", minimalBelanja(1,1,1,1,1))

def beasiswa(semester, status, nilaiMataKuliah):
    if status == 'aktif' and  3 < semester <= 8:
        jumlah_mata_kuliah = len(nilaiMataKuliah)   
        total_nilai = 0
        for nilai in nilaiMataKuliah:
            if nilai == 'A':
                total_nilai += 4
            elif nilai == 'B':
                total_nilai += 3
            elif nilai == 'C':
                total_nilai += 2
            elif nilai == 'D':
                total_nilai += 1
            elif nilai == 'E':
                total_nilai += 0
        
        nilai_ip = total_nilai / (jumlah_mata_kuliah)  
        
        if 3.3 <= nilai_ip <= 4.0 and ['C','D','E'] not in nilaiMataKuliah:
            return "Anda dapat beasiswa"
            
    return "Anda tidak dapat beasiswa"

print(beasiswa(7,'aktif',['A', 'B', 'A', 'B', 'A']))

