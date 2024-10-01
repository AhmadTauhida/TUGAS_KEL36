class Program:
    def __init__(self):
        print("Selamat datang di konser ZerOne")
        print(f"Silahkan pesan tiket anda\n")

    def tampilkan_menu_kategori(self):
        print("Pilih kategori tiket:")
        print("1. VVIP - Rp 1.000.000")
        print("2. VIP - Rp 750.000")
        print("3. Reguler - Rp 500.000")

    def hitung_harga(self, kategori):
        if kategori == 1:
            return 1000000
        elif kategori == 2:
            return 750000
        elif kategori == 3:
            return 500000
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
        kategori_nama = {1: "VVIP", 2: "VIP", 3: "Reguler"}
        metode_nama = {1: "Transfer Bank", 2: "Cash"}

        print(f"\nKonfirmasi Pemesanan:")
        print(f"Nama: {nama}")
        print(f"Kategori: {kategori_nama.get(kategori, 'Tidak valid')}")
        print(f"Jumlah Tiket: {jumlah_tiket}")
        print(f"Metode Pembayaran: {metode_nama.get(metode_pembayaran, 'Tidak valid')}")
        print(f"Total Harga: Rp {total_harga:,}")

        pilihan = input("Apakah Anda yakin dengan pemesanan ini? (ya/tidak): ").lower()
        return pilihan == "ya"

    def pemesanan_tiket(self):
        nama = input("Masukkan nama Anda: ")

        while True:
            self.tampilkan_menu_kategori()
            try:
                kategori = int(input("Masukkan pilihan kategori (1-3): "))
                harga_per_tiket = self.hitung_harga(kategori)
                print(f"Harga per tiket untuk kategori {kategori} adalah {harga_per_tiket}")

                if harga_per_tiket == 0:
                    continue  # Kembali ke awal jika kategori tidak valid

                jumlah_tiket = int(input("Masukkan jumlah tiket yang ingin dipesan: "))
                total_harga = harga_per_tiket * jumlah_tiket
                print(f"Total harga untuk {jumlah_tiket} tiket adalah {total_harga}")

                self.tampilkan_menu_pembayaran()
                metode_pembayaran = int(input("Masukkan pilihan metode pembayaran (1-2): "))
                total_harga_setelah_diskon = self.hitung_diskon(total_harga, metode_pembayaran)
                print(f"Total harga setelah diskon adalah {total_harga_setelah_diskon}")

                if total_harga_setelah_diskon == 0:
                    continue  # Kembali ke awal jika metode tidak valid

                if self.konfirmasi_pemesanan(nama, kategori, jumlah_tiket, metode_pembayaran, total_harga_setelah_diskon):
                    print("\nPemesanan berhasil! Silakan melakukan pembayaran.")
                    break
                else:
                    print("\nMengulangi pemesanan...\n")
            except ValueError:
                print("Input tidak valid! Harap masukkan angka.")
                continue

# Membuat objek dari class Program dan memulai proses pemesanan tiket
program = Program()
program.pemesanan_tiket()
