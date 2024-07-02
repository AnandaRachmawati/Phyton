
def Biner(n):
    if (n//2 == 0):
        return str(n % 2)
    else:
        return Biner(n // 2) + str(n % 2)

# aplikasi
#print(Biner(10)) 


def IsPrima (n, i = 2):
    
    if n == i :
        return True
    elif n % i == 0:
        return False
    elif n == 1:
        return False
    else: IsPrima(n, i + 1)

def FPB(x,y):
    if y == 0:
        return x
    else: 
        return FPB(y, x%y)
    
print (FPB(60,10))
print (FPB(1,40))
print (FPB(10,11))
print (FPB(10,17))
print (FPB(60,15))

def CountDigit(n):
    if n // 10 == 0:
        return 1
    else:
        return 1 + CountDigit(n//10)
    
    
 