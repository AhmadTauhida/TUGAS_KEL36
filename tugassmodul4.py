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

    def tampilkan_menu_pembayaran(self):
        print("Pilih metode pembayaran:")
        print("1. Transfer Bank (Diskon 10%)")
        print("2. Cash (Tidak ada diskon)")

    def hitung_diskon(self, harga, metode_pembayaran):
        if metode_pembayaran == 1:
            return harga * 0.9  # Diskon 10%
        elif metode_pembayaran == 2:
            return harga
        else:
            print("Pilihan metode pembayaran tidak valid!")
            return 0

    def konfirmasi_pemesanan(self, nama, kategori, jumlah_tiket, metode_pembayaran, total_harga):
        kategori_nama = {1: "VIP", 2: "Reguler", 3: "Budget"}
        metode_nama = {1: "Transfer Bank", 2: "Cash"}

        print(f"\nKonfirmasi Pemesanan:")
        print(f"Nama: {nama}")
        print(f"Kategori: {kategori_nama.get(kategori, 'Tidak valid')}")
        print(f"Jumlah Tiket: {jumlah_tiket}")
        print(f"Metode Pembayaran: {metode_nama.get(metode_pembayaran, 'Tidak valid')}")
        print(f"Total Harga: Rp {total_harga:,}")
