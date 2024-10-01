#membuat class untuk method, membuat fungsi sambutan
#membuat fungsi kategori, membuat fungsi hitung 

class Program:
    def __init__(self):
        print("Selamat datang di konser JMK 48")
        print(f"Silahkan pesan tiket anda\n")

    def tampilkan_menu_kategori(self):
        print("Pilih kategori tiket:")
        print("1. VIP - Rp 1,500,000")
        print("2. Reguler - Rp 750,000")
        print("3. Budget - Rp 200,000")

    def hitung_harga(self, kategori):
        if kategori == 1:
            return 1500000
        elif kategori == 2:
            return 750000
        elif kategori == 3:
            return 200000
        else:
            print("Pilihan kategori tidak valid!")
            return 0

    
