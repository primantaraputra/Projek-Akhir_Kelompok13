data = []
buku_favorit = {}

def daftar_buku():
    print("\nTOP 10 BUKU PALING LARIS")
    print("1. AMBALAN 1969")
    print("2. AMBARAWA SOSOK PENJAGA RAWA HYTAM MISTERIYUS")
    print("3. AMBABELLE BONEKA YANG TERKUTUK")
    print("4. LEOAMBA DA VINCI")
    print("5. KISAH HOROR BONEKA AMBALABU")
    print("6. IRONI MAN")
    print("7. CAPTAIN NGAWI")
    print("8. AMBALEON")
    print("9. AMBAWICK")
    print("10. RUSDI SHELBY")

def pinjam_buku():
    pilih = int(input("Silahkan pilih buku : "))
    nama = input("Nama peminjam : ")
    tanggal = input("Tanggal Pinjam (DD/MM/YYYY) : ")
    judul = [
        "AMBALAN 1969", 
        "AMBARAWA SOSOK PENJAGA RAWA HYTAM MISTERIYUS", 
        "AMBABELLE BONEKA YANG TERKUTUK", 
        "LEOAMBA DA VINCI",
        "KISAH HOROR BONEKA AMBALABU", 
        "IRONI MAN", 
        "CAPTAIN NGAWI", 
        "AMBALEON", 
        "AMBAWICK", 
        "RUSDI SHELBY"
    ][pilih - 1]
    id_buku = 1234 + (pilih - 1) * 1111
    peminjaman = [nama, id_buku, judul, tanggal, False]  
    data.append(peminjaman)
    buku_favorit[judul] = buku_favorit.get(judul, 0) + 1
    return peminjaman

def tampilkan_data():
    if data:
        print("\nDATA PEMINJAMAN")
        for i in range(len(data)):
            peminjaman = data[i]
            status = "Sudah Dikembalikan" if peminjaman[4] else "Belum Dikembalikan"
            print(f"{i + 1}. Nama: {peminjaman[0]}, Judul Buku: {peminjaman[2]}, Tanggal Pinjam: {peminjaman[3]}, Status: {status}")
    else:
        print("Tidak ada data untuk sementara ini, Mari meminjam buku terlebih dahulu")

def edit_peminjaman():
    tampilkan_data()
    if not data:
        return
    pilihan = int(input("Pilih nomor peminjaman yang ingin diubah : ")) - 1
    if pilihan < 0 or pilihan >= len(data):
        print("Nomor tidak valid.")
        return
    peminjaman = data[pilihan]
    print(f"Data saat ini: Nama: {peminjaman[0]}, Judul Buku: {peminjaman[2]}, Tanggal Pinjam: {peminjaman[3]}")
    nama_baru = input("Masukkan nama peminjam baru (tekan enter untuk tidak mengubah): ")
    if nama_baru:
        peminjaman[0] = nama_baru  
    tanggal_baru = input("Masukkan tanggal pinjam baru (DD/MM/YYYY, tekan enter untuk tidak mengubah): ")
    if tanggal_baru:
        peminjaman[3] = tanggal_baru  
    print("\nPilih buku baru jika ingin mengubah buku yang dipinjam:")
    daftar_buku()
    buku_baru = input("Silahkan pilih buku baru (tekan enter untuk tidak mengubah): ")
    if buku_baru.isdigit() and int(buku_baru) in range(1, 11):
        judul_baru = [
            "AMBALAN 1969", 
            "AMBARAWA SOSOK PENJAGA RAWA HYTAM MISTERIYUS", 
            "AMBABELLE BONEKA YANG TERKUTUK", 
            "LEOAMBA DA VINCI",
            "KISAH HOROR BONEKA AMBALABU", 
            "IRONI MAN", 
            "CAPTAIN NGAWI", 
            "AMBALEON", 
            "AMBAWICK", 
            "RUSDI SHELBY"
        ][int(buku_baru) - 1]
        id_buku_baru = 1234 + (int(buku_baru) - 1) * 1111
        buku_favorit[peminjaman[2]] -= 1
        if buku_favorit[peminjaman[2]] == 0:
            del buku_favorit[peminjaman[2]]
        peminjaman[2] = judul_baru
        peminjaman[1] = id_buku_baru
        buku_favorit[judul_baru] = buku_favorit.get(judul_baru, 0) + 1
    print("\nBerhasil mengubah data peminjaman.")

def remove_buku():
    if not data:  
        print("Maaf, tidak bisa menghapus buku, karena anda belum meminjam buku.")
        return
    tampilkan_data()
    pilihan = int(input("Pilih nomor yang ingin dihapus : ")) - 1
    if pilihan < 0 or pilihan >= len(data):
        print("Nomor tidak valid.")
        return
    peminjaman = data[pilihan]
    if not peminjaman[4]:  
        print(f"Buku '{peminjaman[2]}' belum dikembalikan. Tidak dapat menghapus peminjaman.")
        return
    judul = peminjaman[2]
    buku_favorit[judul] -= 1
    if buku_favorit[judul] == 0:
        del buku_favorit[judul]
    del data[pilihan]
    print("Berhasil menghapus peminjaman.")

def pengembalian_buku():
    tampilkan_data()
    if not data:
        return
    pilihan = int(input("Pilih nomor peminjaman yang ingin dikembalikan : ")) - 1
    if pilihan < 0 or pilihan >= len(data):
        print("Nomor tidak valid.")
        return
    peminjaman = data[pilihan]
    peminjaman[4] = True  
    print(f"Buku '{peminjaman[2]}' berhasil dikembalikan.")

def tampilkan_buku_favorit():
    if buku_favorit:
        favorit_terbanyak = max(buku_favorit.values())
        buku_favorit_list = [judul for judul, jumlah in buku_favorit.items() if jumlah == favorit_terbanyak]
        print("\nBUKU FAVORIT:")
        for buku in buku_favorit_list:
            print(f"{buku} - Jumlah Peminjaman: {favorit_terbanyak}")
    else:
        print("Tidak ada peminjaman buku untuk akhir akhir ini, Jadi belum ada buku favorit.")

while True: 
    print("\nWELCOME TO LIBRARY OF NGAWI CITY")
    print("1. Pinjam Buku")
    print("2. Pengembalian Buku")
    print("3. Update Peminjaman")
    print("4. Hapus Peminjaman")
    print("5. Tampilkan Data Peminjaman")
    print("6. Tampilkan Buku Favorit")
    print("7. Keluar")
    pilih = int(input("Silahkan pilih : "))
    if pilih == 1:
        daftar_buku()
        peminjaman = pinjam_buku()
        print(f"\nBerhasil meminjam: ID Buku: {peminjaman[1]}, Judul: {peminjaman[2]}, Peminjam: {peminjaman[0]}, Tanggal Pinjam: {peminjaman[3]}")
    elif pilih == 2:
        pengembalian_buku()
    elif pilih == 3:
        edit_peminjaman()
    elif pilih == 4:
        remove_buku()
    elif pilih == 5:
        tampilkan_data()
    elif pilih == 6:
        tampilkan_buku_favorit()
    elif pilih == 7:
        print("Terima kasih sudah berkunjung di perpustakaan!")
        break
    else:
        print("Invalid! Masukkan pilihan yang benar.")