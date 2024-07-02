#Nama File  : typepecahan.py
#Deskripsi  : Membuat tipe pecahan beserta konstruktor dan selektornya.
#Pembuat    :  
#Tanggal    : 

#DEFINISI DAN SPESIFIKASI TYPE
#type pecahan: <n: integer >=0 ,d: integer>0>
#   < n:integer>=0, d:integer>0 > n adalah pembilang (numerator) dan d adalah penyebut (denumerator). Penyebut sebuah pecahan tidak boleh nol.

#DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# makeP: integer>=0, integer>0 --> pecahan
#   makeP(x,y) membentuk sebuah pecahan dari pembilang x dan penyebut y, dengan x dan y integer
#Realisasi dalam Python


#DEFINISI DAN SPESIFIKASI SELEKTOR DENGAN FUNGSI 
#Pemb: pecahan --> integer>0
#   Pemb(p) memberikan numerator pembilang n dari pecahan tersebut
#Realisasi dalam Python


#Peny: pecahan --> integer>0
#   Peny(p) memberikan denumerator penyebut d dari pecahan tersebut
#Realisasi dalam Python


#DEFINISI DAN SPESIFIKASI OPERATOR TERHADAP PECAHAN
#Operator aritmatika Pecahan

#AddP : 2 pecahan --> pecahan
#   AddP(P1,P2) menambahkan dua buah pecahan P1 dan P2: n1/d1 + n2/d2 = (n1*d2+n2*d1)/d1*d2
#Realisasi


#SubP: 2 pecahan --> pecahan
#   SubP(P1,P2) mengurangkan dua buah pecahan P1 dan P2: n1/d1 - n2/d2 = (n1*d2-n2*d1)/d1*d2
#Realisasi


#MulP: 2 pecahan --> pecahan
#   MulP(P1,P2) mengalikan dua buah pecahan P1 dan P2: n1/d1 * n2/d2 = n1*n2/d1*d2
#Realisasi


#DivP: pecahan --> pecahan
#   DivP(P1,P2) membagi dua buah pecahan P1 dan P2: (n1/d1)/(n2/d2) = n1*d2/d1*n2
#Realisasi


#RealP: pecahan --> real
#   Menuliskan bilangan pecahan dalam notasi desimal
#Realisasi


#DEFINISI DAN SPESIFIKASI PREDIKAT
#operator relasional Pecahan

#IsEqP? : 2 pecahan --> boolean
#   IsEqP?(P1,P2) membandingkan apakah dua buah pecahan sama nilainya
#Realisasi

#IsLtP? : 2 pecahan --> boolean
#   IsLtP?(P1,P2) membandingkan dua buah pecahan, apakah P1 lebih kecil daripada P2
#Realisasi

#IsGtP? : 2 pecahan --> boolean
#   IsGtP?(P1,P2) membandingkan dua buah pecahan, apakah P1 lebih besar daripada P2
#Realisasi


############################################################################################################################
#APLIKASI KONSTRUKTOR


#APLIKASI SELEKTOR


#APLIKASI OPERATOR


#APLIKASI PREDIKAT



