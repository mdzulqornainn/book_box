
perpustakaan = []
# menyimpan data buku ke dalam list & memuat data dari data.txt
def muat_data():
    try:
        with open("data.txt", "r") as f:
            for baris in f:
                data = baris.strip().split("|")
                if len(data) == 5:
                    buku = {
                        "id": data[0],
                        "judul": data[1],
                        "penulis": data[2],
                        "tahun": data[3],
                        "status": data[4]
                    }
                    perpustakaan.append(buku)
    except FileNotFoundError:
        # Jika file belum ada maka buat file kosong
        open("data.txt", "w").close()

# simpan data buku ke dalam data.txt
def simpan_data():
    with open("data.txt", "w") as f:
        for buku in perpustakaan:
            baris = f"{buku['id']}|{buku['judul']}|{buku['penulis']}|{buku['tahun']}|{buku['status']}\n"
            f.write(baris)



# fungsi tambah buku
def tambah_buku():
    judul = input("Masukkan judul buku: ")
    penulis = input("Masukkan penulis buku: ")
    tahun = input("Masukkan tahun terbit: ")

    for buku in perpustakaan:
        if buku["judul"].lower() == judul.lower() and buku["penulis"].lower() == penulis.lower():
            print("Buku tersebut sudah ada (duplikat).")
            konfirmasi = input("apakah buku masih ingin dimasukkan? ketik 'Ya' untuk konfirmasi 'Tidak' untuk skip :")
            if konfirmasi == "Ya":
                if not perpustakaan:
                    id_baru = "B001"
                else:
                    last_id = perpustakaan[-1]["id"]
                    angka = int(last_id[1:]) + 1       
                    id_baru = f"B{angka:03d}" 

                buku = {
                    "id": id_baru,
                    "judul": judul,
                    "penulis": penulis,
                    "tahun": tahun,
                    "status": "Tersedia"
                }

                perpustakaan.append(buku)
                simpan_data()
                break


    #   Generate ID 
    if not perpustakaan:
        id_baru = "B001"
    else:
        last_id = perpustakaan[-1]["id"]
        angka = int(last_id[1:]) + 1       
        id_baru = f"B{angka:03d}"   

    buku = {
        "id": id_baru,
        "judul": judul,
        "penulis": penulis,
        "tahun": tahun,
        "status": "Tersedia"
    }

    perpustakaan.append(buku)
    simpan_data()
    print("\n Buku berhasil ditambahkan.")


def hapus_buku():
    print("\n=== Hapus Buku ===")
    id_buku = input("Masukkan ID buku: ").strip()

    for buku in perpustakaan:
        if buku["id"] == id_buku:
            perpustakaan.remove(buku)
            print("Buku berhasil dihapus.")
            return

    print("ID buku tidak ditemukan.")

# menampilkan seluruh buku
def tampilkan_buku():
    if perpustakaan == []:
        print("Belum ada data buku.")
        return  
    else:
        print("\n=== DAFTAR SEMUA BUKU ===")
        print(f"{'No':<4} {'ID':<5} {'Judul Buku':<30} {'Penulis':<20} {'Tahun':<6} {'Status':<10}")
        print("-" * 80)

        for i, buku in enumerate(perpustakaan):
            print(f"{i+1:<4} {buku['id']:<5} {buku['judul']:<30}  {buku['penulis']:<20} {buku['tahun']:<6} {buku['status']:<10}")
            i += 1


# fungsi cari buku
def cari_buku():
    print("\n=== CARI BUKU ===")
    keyword = input("Masukkan judul atau penulis: ").strip().lower()
    hasil = [buku for buku in perpustakaan if keyword in buku["judul"].lower() or keyword in buku["penulis"].lower()]
    if hasil:
        print(f"\n{'Judul Buku':<30} {'Penulis':<20} {'Tahun':<6}")
        print("-" * 60)
        for buku in hasil:
            print(f"{buku['judul']:<30} {buku['penulis']:<20} {buku['tahun']:<6}")
    else:
        print("\nBuku tidak ditemukan.")


# Pinjam buku
def pinjam_buku():
    print("\n=== PINJAM BUKU ===")
    id_buku = input("Masukkan ID buku yang ingin dipinjam: ").strip()
    for buku in perpustakaan:
        if buku["id"] == id_buku:
            if buku["status"] == "Tersedia":
                buku["status"] = "Dipinjam"
                simpan_data()
                print(f"\nBuku '{buku['judul']}' berhasil dipinjam.")
                return
            else:
                print("\nBuku sedang tidak tersedia untuk dipinjam.")
                return
    print("\nBuku dengan ID tersebut tidak ditemukan.")

# kembalikan buku
def kembalikan_buku():
    print("\n=== KEMBALIKAN BUKU ===")
    id_buku = input("Masukkan ID buku yang ingin dikembalikan: ").strip()
    for buku in perpustakaan:
        if buku["id"] == id_buku:
            if buku["status"] == "Dipinjam":
                buku["status"] = "Tersedia"
                simpan_data()
                print(f"\nBuku '{buku['judul']}' berhasil dikembalikan.")
                return
            else:
                print("\nBuku tersebut tidak sedang dipinjam.")
                return
    print("\nBuku dengan ID tersebut tidak ditemukan.")

#menu
def menu():
    muat_data()

    while True:
        print("\n========== SISTEM PERPUSTAKAAN MINI ==========")
        print("1. Tambah Buku")
        print("2. Hapus Buku")
        print("3. Tampilkan Buku")
        print("4. Cari Buku")
        print("5. Pinjam Buku")
        print("6. Kembalikan Buku")
        print("7. Exit")

        pilihan = input("Pilih Menu (1-7): ")

        if pilihan == "1":
            tambah_buku()
        elif pilihan == "2":
            hapus_buku()
        elif pilihan == "3":
            tampilkan_buku()
        elif pilihan == "4":
            cari_buku()
        elif pilihan == "5":
            pinjam_buku()
        elif pilihan == "6":
            kembalikan_buku()
        elif pilihan == "7":
            print("Terimakasih, program selesai")
            break
        else:
            print("Pilihan tidak valid")



menu()