#Konstruktor
def makeP(x,y,z):
    return [x,y,z]
#Selektor
def bil(p):
    return p[0]

def pemb(p):
    return p[1]

def peny(p):
    return p[2]
#Operator
def KonversiPecahan (p):
    return makeP(0, bil(p)*peny(p)+pemb(p), peny(p))

def AddP(p1,p2):
    bilAdd = (bil(p1)+bil(p2))
    pembAdd = ((pemb(p1)*peny(p2)+pemb(p2)*peny(p1)))
    penyAdd = (peny(p1)*peny(p2))
    return makeP(bilAdd,pembAdd,penyAdd)

def SubP(p1,p2):
    bilSub = (bil(p1) - bil(p2))
    pembSub = ((pemb(p1) * peny(p2) - pemb(p2) * peny(p1)))
    penySub = (peny(p1) * peny(p2))
    return makeP(bilSub,pembSub,penySub)

def MulP(p1,p2):
    pembMul = (pemb(KonversiPecahan(p1)) * pemb(KonversiPecahan(p2)))
    penyMul = (peny(KonversiPecahan(p1)) * peny(KonversiPecahan(p2)))
    return makeP(0, pembMul,penyMul)

def DivP(p1,p2):
    pembDiv = (pemb(KonversiPecahan(p1)) * peny(KonversiPecahan(p2)))
    penyDiv = (pemb(KonversiPecahan(p2)) * peny(KonversiPecahan(p1)))
    return makeP(0,pembDiv,penyDiv)

def RealP(P):
    return pemb(KonversiPecahan(P)) / peny(KonversiPecahan(P))
#Predikat
def IsEqP(p1,p2):
    return RealP(p1) == RealP(p2)

def IsLtP(p1,p2):
    return RealP(p1) < RealP(p2)

def IsGtP(p1,p2):
    return RealP(p1) > RealP(p2)

############################################################################################################################
#APLIKASI KONSTRUKTOR
p = makeP(2,3,4)
p1 = makeP(1,1,4)
p2 = makeP(2,1,4)

#APLIKASI SELEKTOR
print(bil(p))
print(pemb(p))
print(peny(p))
#APLIKASI OPERATOR
print(KonversiPecahan(p))
print(AddP(p1,p2))
print(SubP(p1,p2))
print(MulP(p1,p2))
print(DivP(p1,p2))
print(RealP(p))
#APLIKASI PREDIKAT
print(IsEqP(p1,p2))
print(IsLtP(p1,p2))
print(IsGtP(p1,p2))
