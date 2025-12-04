def tampilkan_buku():
    print("\n=== DAFTAR SEMUA BUKU ===")
    print(f"{'No':<4} {'Judul Buku':<30} {'Penulis':<20} {'Tahun':<6} {'Status':<10}")
    print("-" * 80)

    i = 1 
    for buku in data_buku:
        print(f"{i:<4} {buku['judul']:<30} {buku['penulis']:<20} {buku['tahun']:<6} {buku['status']:<10}")
        i += 1


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