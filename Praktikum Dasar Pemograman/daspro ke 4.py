def hitung_gaji(waktuKerja, lamaJadiKaryawan):
    jam_kerja = waktuKerja // 60

    if 1 <= lamaJadiKaryawan <= 1024 :
        gaji_pokok = jam_kerja * 1000
    elif lamaJadiKaryawan < 5:
        gaji_pokok = jam_kerja * 1250
    elif lamaJadiKaryawan < 7:
        gaji_pokok = jam_kerja * 1500
    else:
        gaji_pokok = jam_kerja * 2000

    # Hitung gaji lembur
    if jam_kerja > 8:
        lembur = jam_kerja - 8
        if lembur <= 2:
            gaji_lembur = lembur * gaji_pokok * 0.05
        else:
            gaji_lembur = (2 * gaji_pokok * 0.05) + ((lembur - 2) * gaji_pokok * 0.10)
    else:
        gaji_lembur = 0

    # Total gaji
    total_gaji = gaji_pokok + gaji_lembur

    # Check jam kerja
    if waktuKerja <= 480:
        return total_gaji
    elif waktuKerja > 600:
        return "Pulang bro, kantor dah mau tutup!"
    else:
        return "Jangan bolos bro"

# Input
waktuKerja = int(input("Masukkan waktu kerja dalam menit: "))
lamaJadiKaryawan = int(input("Masukkan lama menjadi karyawan dalam tahun: "))

# Output
if lamaJadiKaryawan >= 1:
    print(hitung_gaji(waktuKerja, lamaJadiKaryawan))
else:
    print("Kamu kan bukan karyawan sini!")
