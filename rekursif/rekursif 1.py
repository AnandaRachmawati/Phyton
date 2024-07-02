def Biner(n):
    if (n//2 == 0):
        return str(n % 2)
    else:
        return Biner(n // 2) + str(n % 2) 

print(Biner(5))
print(Biner(9))
print(Biner(7))

