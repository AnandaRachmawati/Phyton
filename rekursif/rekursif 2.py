def IsPrima (n, i=2): 
    if n == i :
        return True
    elif n % i == 0 or n == 1:
        return False
    else: 
        return IsPrima(n, i + 1)

print(IsPrima(7))
print(IsPrima(11))
print(IsPrima(47))
print(IsPrima(12))
print(IsPrima(100))
print(IsPrima(111))
