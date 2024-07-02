def makanPermen(permen,tanggal):
    waktuRina = 3
    waktuRani = waktuRina * 2
    if (1<= permen <= 10):
        if (1 <= tanggal <= 31):
            if (1<= tanggal <= 19 or tanggal == 31):
                return waktuRani * permen
            else:
                if (20 <= tanggal <=30 and tanggal %2 != 0 ):
                    return (permen)* (waktuRani-2)
                else:
                    return (waktuRani -1)* permen
        else:
            return "tanggal 1-31"

    else:
        return "permen harus 1 sampai 10"
    
print(makanPermen(7,2))