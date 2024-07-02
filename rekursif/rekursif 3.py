def FPB(x,y):
    if y == 0:
        return x
    elif x ==0:
        return y
    else: 
        return FPB(y, x%y)
    
print (FPB(60,10))
print (FPB(1,40))
print (FPB(10,11))
print (FPB(10,17))
print (FPB(60,15))