def lihat_tugas(tugas):
    """
    Menampilkan semua tugas yang ada di dalam list ke konsol.

    Fungsi ini akan melakukan iterasi pada list tugas dan mencetak detail
    setiap tugas dengan format yang rapi. Jika tidak ada tugas, fungsi akan
    menampilkan pesan informasi.

    Args:
        tugas (list): Sebuah list yang berisi dictionary dari setiap tugas.
    """
    # Mengecek apakah list 'tugas' kosong. 'not tugas' akan bernilai True jika listnya kosong.
    if not tugas:
        # Jika tidak ada tugas, cetak pesan ini ke layar.
        print("Tidak ada tugas yang tersedia.")
        # Menghentikan eksekusi fungsi ini lebih awal karena tidak ada yang perlu ditampilkan.
        return

    # Jika ada tugas, cetak judul untuk daftar tugas.
    print("Daftar Tugas:")
    # Memulai perulangan (loop) untuk setiap item tugas di dalam list 'tugas'.
    # 'tugas_item' akan berisi satu dictionary tugas pada setiap iterasinya.
    for tugas_item in tugas:
        # Mencetak ID dan Judul tugas dengan format yang rapi.
        print(f"- {tugas_item['id']}. {tugas_item['title']}")
        # Mencetak Deskripsi dari tugas yang sedang ditampilkan.
        print(f"  Deskripsi: {tugas_item['description']}")
        # Mencetak Status dari tugas tersebut.
        print(f"  Status: {tugas_item['status']}")
        # Mencetak Estimasi Waktu Pengerjaan tugas.
        print(f"  Estimasi Waktu: {tugas_item['estimasi_waktu_pengerjaan']} menit")
        # Mencetak garis pemisah agar tampilan antar tugas lebih jelas.
        print("-" * 20)

def tambah_tugas(tugas):
    """
    Menambahkan tugas baru ke dalam list berdasarkan input dari pengguna.

    Fungsi ini akan meminta pengguna untuk memasukkan judul, deskripsi,
    status, dan estimasi waktu. Setelah semua input valid, tugas baru
    akan ditambahkan ke dalam list 'tugas'.

    Args:
        tugas (list): List tugas yang akan ditambahkan item baru.
    """
    # Memulai perulangan tak terbatas untuk memastikan pengguna memasukkan judul.
    while True:
        # Meminta input dari pengguna untuk judul tugas.
        title = input("Masukkan judul tugas: ")
        # Mengecek apakah input judul tidak kosong.
        if title:
            # Jika judul tidak kosong, hentikan perulangan 'while' ini.
            break
        # Jika judul kosong, cetak pesan error.
        print("Judul tugas tidak boleh kosong. Silakan coba lagi.")

    # Memulai perulangan tak terbatas untuk memastikan pengguna memasukkan deskripsi.
    while True:
        # Meminta input dari pengguna untuk deskripsi tugas.
        description = input("Masukkan deskripsi tugas: ")
        # Mengecek apakah input deskripsi tidak kosong.
        if description:
            # Jika deskripsi tidak kosong, hentikan perulangan 'while' ini.
            break
        # Jika deskripsi kosong, cetak pesan error.
        print("Deskripsi tugas tidak boleh kosong. Silakan coba lagi.")

    # Memulai perulangan tak terbatas untuk memastikan status yang dimasukkan valid.
    while True:
        # Meminta input status dan langsung mengubahnya menjadi huruf kecil.
        status = input("Masukkan status tugas (Selesai/Belum Selesai): ").lower()
        # Mengecek apakah input pengguna adalah 'selesai' atau 'belum selesai'.
        if status in ["selesai", "belum selesai"]:
            # Jika valid, hentikan perulangan.
            break
        # Jika tidak valid, cetak pesan error.
        print("Status tugas harus 'Selesai' atau 'Belum Selesai'. Silakan coba lagi.")

    # Memulai perulangan tak terbatas untuk memastikan estimasi waktu adalah angka positif.
    while True:
        # 'try' digunakan untuk menangani error jika input bukan angka.
        try:
            # Meminta input estimasi waktu dan mengubahnya menjadi tipe data integer (angka bulat).
            estimasi_waktu = int(input("Masukkan estimasi waktu pengerjaan (menit): "))
            # Mengecek apakah angka yang dimasukkan lebih besar dari 0.
            if estimasi_waktu > 0:
                # Jika valid, hentikan perulangan.
                break
            # Jika angka 0 atau negatif, cetak pesan error.
            print("Estimasi waktu harus lebih dari 0. Silakan coba lagi.")
        # 'except ValueError' akan berjalan jika input tidak bisa diubah menjadi integer (misal: "abc").
        except ValueError:
            # Cetak pesan error jika input bukan angka.
            print("Estimasi waktu harus berupa angka. Silakan coba lagi.")

    # Membuat sebuah dictionary baru untuk menampung data tugas yang baru.
    new_task = {
        # Membuat ID baru secara otomatis dengan mengambil jumlah tugas saat ini lalu ditambah 1.
        "id": len(tugas) + 1,
        # Mengisi 'title' dengan data dari input pengguna.
        "title": title,
        # Mengisi 'description' dengan data dari input pengguna.
        "description": description,
        # Mengisi 'status' dengan data dari input pengguna.
        "status": status,
        # Mengisi 'estimasi_waktu_pengerjaan' dengan data dari input pengguna.
        "estimasi_waktu_pengerjaan": estimasi_waktu
    }
    # Menambahkan dictionary 'new_task' ke dalam list 'tugas'.
    tugas.append(new_task)
    # Mencetak pesan konfirmasi bahwa tugas berhasil ditambahkan.
    print("Tugas berhasil ditambahkan!")

def tandai_selesai(tugas):
    """
    Mengubah status sebuah tugas menjadi "Selesai" berdasarkan ID.

    Fungsi akan meminta pengguna memasukkan ID tugas. Jika ID ditemukan,
    status tugas tersebut akan diubah. Jika tidak, pesan error akan ditampilkan.

    Args:
        tugas (list): List tugas di mana status salah satu itemnya akan diubah.
    """
    # 'try' untuk menangani error jika input ID bukan angka.
    try:
        # Meminta pengguna memasukkan ID tugas yang ingin diubah dan menjadikannya integer.
        id_tugas = int(input("Masukkan ID tugas yang ingin ditandai selesai: "))
    # 'except' akan menangkap error jika input tidak bisa diubah menjadi angka.
    except ValueError:
        # Mencetak pesan error.
        print("ID tugas harus berupa angka.")
        # Menghentikan fungsi.
        return

    # Melakukan perulangan untuk setiap item tugas di dalam list 'tugas'.
    for tugas_item in tugas:
        # Mengecek apakah ID dari tugas saat ini sama dengan ID yang dimasukkan pengguna.
        if tugas_item["id"] == id_tugas:
            # Jika ID cocok, ubah statusnya menjadi "Selesai".
            tugas_item["status"] = "Selesai"
            # Cetak pesan konfirmasi.
            print("Tugas berhasil diperbarui menjadi selesai!")
            # Hentikan fungsi karena tugas sudah ditemukan dan diubah.
            return
    # Pesan ini akan dicetak jika perulangan selesai tanpa menemukan ID yang cocok.
    print("ID tugas tidak ditemukan.")

def hapus_tugas(tugas):
    """
    Menghapus sebuah tugas dari list berdasarkan ID yang diinput pengguna.

    Fungsi akan menampilkan daftar tugas terlebih dahulu, kemudian meminta
    ID tugas yang akan dihapus. Jika ID ditemukan, tugas akan dihapus.

    Args:
        tugas (list): List tugas yang akan dihapus salah satu itemnya.
    """
    # Memanggil fungsi 'lihat_tugas' agar pengguna bisa melihat ID tugas yang akan dihapus.
    lihat_tugas(tugas)
    # 'try' untuk menangani error jika input ID bukan angka.
    try:
        # Meminta pengguna memasukkan ID tugas yang ingin dihapus.
        id_tugas = int(input("Masukkan ID tugas yang ingin dihapus: "))
    # 'except' untuk menangkap error jika input bukan angka.
    except ValueError:
        # Cetak pesan error.
        print("ID tugas harus berupa angka.")
        # Hentikan fungsi.
        return

    # Melakukan perulangan untuk setiap item tugas di dalam list 'tugas'.
    for tugas_item in tugas:
        # Mengecek apakah ID dari tugas saat ini sama dengan ID yang dimasukkan pengguna.
        if tugas_item["id"] == id_tugas:
            # Jika ID cocok, hapus item tersebut dari list 'tugas'.
            tugas.remove(tugas_item)
            # Cetak pesan konfirmasi.
            print("Tugas berhasil dihapus!")
            # Hentikan fungsi karena tugas sudah ditemukan dan dihapus.
            return
    # Pesan ini akan dicetak jika perulangan selesai tanpa menemukan ID yang cocok.
    print("ID tugas tidak ditemukan.")

# Ini adalah list utama yang akan menyimpan semua data tugas.
# Setiap tugas adalah sebuah dictionary di dalam list ini.
tugas = [
    {
        "id": 1,
        "title": "Mengerjakan PR Matematika",
        "description": "Halaman 20-25",
        "status": "Belum Selesai",
        "estimasi_waktu_pengerjaan": 30
    },
    {
        "id": 2,
        "title": "Membeli bahan makanan",
        "description": "Daftar belanja ada di catatan",
        "status": "Selesai",
        "estimasi_waktu_pengerjaan": 60
    },
    {
        "id": 3,
        "title": "Mencuci mobil",
        "description": "Gunakan sabun khusus",
        "status": "Selesai",
        "estimasi_waktu_pengerjaan": 60
    },
    {
        "id": 4,
        "title": "Membaca buku",
        "description": "Bab 3 dan 4",
        "status": "Belum Selesai",
        "estimasi_waktu_pengerjaan": 45
    },
    {
        "id": 5,
        "title": "Menulis esai",
        "description": "Tema bebas, minimal 3 halaman",
        "status": "Selesai",
        "estimasi_waktu_pengerjaan": 60
    },
    {
        "id": 6,
        "title": "Pergi ke gym",
        "description": "Lakukan latihan kardio",
        "status": "Belum Selesai",
        "estimasi_waktu_pengerjaan": 45
    }
]

def menu():
    """Menampilkan menu utama aplikasi kepada pengguna."""
    # Mencetak judul aplikasi.
    print("\nSelamat Datang di Aplikasi To-Do List")
    # Mencetak pilihan 1.
    print("1. Lihat Semua Tugas")
    # Mencetak pilihan 2.
    print("2. Tambah Tugas")
    # Mencetak pilihan 3.
    print("3. Tandai Tugas Selesai")
    # Mencetak pilihan 4.
    print("4. Hapus Tugas")
    # Mencetak pilihan 5.
    print("5. Keluar")

def main():
    """
    Fungsi utama yang menjalankan alur program.

    Fungsi ini berisi loop utama yang akan terus menampilkan menu,
    menerima input dari pengguna, dan memanggil fungsi yang sesuai
    sampai pengguna memilih untuk keluar.
    """
    # Memulai perulangan tak terbatas agar menu terus ditampilkan setelah satu aksi selesai.
    while True:
        # Memanggil fungsi 'menu' untuk menampilkannya ke pengguna.
        menu()
        # Meminta input pilihan dari pengguna.
        choice = input("Masukkan pilihan Anda: ")

        # Jika pengguna memilih '1'.
        if choice == '1':
            # Panggil fungsi untuk melihat tugas.
            lihat_tugas(tugas)
        # Jika pilihan bukan '1', cek apakah '2'.
        elif choice == '2':
            # Panggil fungsi untuk menambah tugas.
            tambah_tugas(tugas)
        # Jika pilihan bukan '1' atau '2', cek apakah '3'.
        elif choice == '3':
            # Panggil fungsi untuk menandai tugas selesai.
            tandai_selesai(tugas)
        # Jika bukan juga, cek apakah '4'.
        elif choice == '4':
            # Panggil fungsi untuk menghapus tugas.
            hapus_tugas(tugas)
        # Terakhir, cek apakah pilihan '5'.
        elif choice == '5':
            # Hentikan perulangan 'while', yang akan mengakhiri program.
            break
        # 'else' akan berjalan jika input tidak cocok dengan pilihan mana pun di atas.
        else:
            # Cetak pesan bahwa pilihan tidak valid.
            print("Pilihan tidak valid. Silakan coba lagi.")

# Baris ini memastikan bahwa fungsi 'main()' hanya akan dijalankan
# ketika file Python ini dieksekusi secara langsung.
if __name__ == "__main__":
    # Memanggil fungsi 'main' untuk memulai program.
    main()