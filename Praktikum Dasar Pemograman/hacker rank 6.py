                                         
import math

def hitung_diskon(harga):
    if harga <= 10000:
        return harga* 0.9
    elif harga <= 50000:
        return harga* 0.95
    elif harga <= 100000:
        return harga* 0.97
    else:
        return harga

def hitung_pajak(harga):
    if harga < 50000:
        return harga + (0.05 * harga)
    elif harga <= 250000:
        return harga + (0.07 * harga)
    else:
        return harga + ( 0.1 * harga)
    

def diskon_dan_pajak(a):
    return math.ceil(hitung_pajak(hitung_diskon(a)))



                            
                             
                            