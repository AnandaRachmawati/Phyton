#tinggi_badan = 155.5
#umur = 18
#nama = 'Ananda rachmawati'
#print('nama saya ' + nama + ' tinggi saya adalah ' + str(tinggi_badan) +
 #      ' saat ini umur saya ' + str(umur)) 
#print(input('nama kamu siapa?'))
#print(input('kuliah dimana?'))
#print('ooh begitu, yaudah semangat ya')
#a = 56
#b = 10
#c = b + a
#d = b - a
#print(c * d)

#NIM itu string karena operasinya gabisa di aritmatika

def hargaAlatTulis(a,b,c):
      a = pensil * (2.000) 
      b = buku * (5.000) 
      c = pulpen * (3.000)
      return a + b + c
       
pensil = int(input())
buku = int(input())
pulpen = int(input())

print(hargaAlatTulis(2,3,2))