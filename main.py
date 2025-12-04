
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
        # Jika file belum ada → buat file kosong
        open("data.txt", "w").close()

# simpan data buku ke dalam data.txt
def simpan_data():
    with open("data.txt", "w") as f:
        for buku in perpustakaan:
            baris = f"{buku['id']}|{buku['judul']}|{buku['penulis']}|{buku['tahun']}|{buku['status']}\n"
            f.write(baris)

def tambah_buku():
    judul = input("Masukkan judul buku: ")
    penulis = input("Masukkan penulis buku: ")
    tahun = input("Masukkan tahun terbit: ")

    buku = {
        "judul": judul,
        "penulis": penulis,
        "tahun": tahun,
        "status": "Tersedia"
    }

    perpustakaan.append(buku)
    # simpan_data()
    print("\n Buku berhasil ditambahkan.")

# menampilkan seluruh buku
def tampilkan_buku():
    print("\n=== DAFTAR SEMUA BUKU ===")
    print(f"{'No':<4} {'Judul Buku':<30} {'Penulis':<20} {'Tahun':<6} {'Status':<10}")
    print("-" * 80)

    i = 1 
    for buku in data_buku:
        print(f"{i:<4} {buku['judul']:<30} {buku['penulis']:<20} {buku['tahun']:<6} {buku['status']:<10}")
        i += 1


# fungsi cari buku
def cari_buku():
    print("\n=== CARI BUKU ===")
    keyword = input("Masukkan judul atau penulis: ").strip().lower()
    hasil = [buku for buku in data_buku if keyword in buku["judul"].lower() or keyword in buku["penulis"].lower()]
    if hasil:
        print(f"\n{'Judul Buku':<30} {'Penulis':<20} {'Tahun':<6}")
        print("-" * 60)
        for buku in hasil:
            print(f"{buku['judul']:<30} {buku['penulis']:<20} {buku['tahun']:<6}")
    else:
        print("\n❗ Buku tidak ditemukan.")

tambah_buku()
tampilkan_buku()
