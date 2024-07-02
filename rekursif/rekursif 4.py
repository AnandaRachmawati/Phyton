
def CountDigit(n):
    if n // 10 == 0:
        return 1
    else:
        return 1 + CountDigit(n//10)
    
print(CountDigit(234))
print(CountDigit(24))
print(CountDigit(2346))