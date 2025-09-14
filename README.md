# MINPRO-1.
Nama: Bunga Zulfa Aqila NIM: 2509116024 Sistem Informasi C '2025

# Deskripsi Singkat

Program Sistem Pendaftaran Acara ini dibuat untuk mengelola data peserta dengan menerapkan konsep CRUD (Create, Read, Update, Delete). Program menggunakan list of tuple untuk menyimpan data peserta berupa ID, Nama, dan Email.
Pengguna bisa:

- Menambahkan peserta baru (Create)
- Menampilkan daftar peserta (Read)
- Mengubah data peserta (Update)
- Menghapus pendaftaran peserta (Delete)
- Keluar dari program

# Alur Program

<img width="1092" height="1600" alt="MINPRI-1 drawio" src="https://github.com/user-attachments/assets/555a2e37-6ca0-40a1-ac1d-e4c90a534524" />

**1. Menu Utama**
Program menampilkan pilihan:

=== SISTEM PENDAFTARAN ACARA ===\
Pilih:
1. Daftarkan peserta
2. Tampilkan daftar peserta
3. Ubah data peserta
4. Batalkan pendaftaran
5. Keluar


User memilih angka 1–5.

**2. Daftarkan Peserta (Create)**\
Jika user pilih 1:

- User diminta input ID, Nama, dan Email.
- Data baru ditambahkan ke list peserta.
- Program menampilkan data yang baru ditambahkan dan daftar peserta terbaru.

Contoh Output:

<img width="295" height="240" alt="Screenshot 2025-09-14 185842" src="https://github.com/user-attachments/assets/9df7648d-8eaa-4b1d-bf94-2174b53ef293" />



**3. Tampilkan Daftar Peserta (Read)**\
Jika user pilih 2:

- Program akan menampilkan jumlah peserta dan seluruh data yang ada.
- Jika kosong, tampil pesan “Tidak ada peserta terdaftar”.

Contoh Output:

<img width="277" height="97" alt="Screenshot 2025-09-14 190247" src="https://github.com/user-attachments/assets/ff1e67d9-1bb6-4dce-9cad-81959a9d2323" />


**4. Ubah Data Peserta (Update)**\
Jika user pilih 3:

- Program menampilkan daftar peserta.
- User memilih urutan data (dimulai dari 0).
- User memasukkan data baru (ID, Nama, Email).
- Data lama diganti dengan data baru.

Contoh Output:

<img width="493" height="334" alt="Screenshot 2025-09-14 200803" src="https://github.com/user-attachments/assets/860cb8d7-1277-4d12-8109-1553a1c5d4ee" />


**5. Batalkan Pendaftaran (Delete)**\
Jika user pilih 4:

- Program menampilkan daftar peserta.
- User memilih urutan data (dimulai dari 0).
- Data yang dipilih akan dihapus.

Contoh Output:

<img width="494" height="248" alt="Screenshot 2025-09-14 201414" src="https://github.com/user-attachments/assets/9d73ae4e-cfe6-44fa-8001-ffda88901bb3" />


**6. Keluar Program**\
Jika user pilih 5 atau input tidak valid:

Output:

<img width="274" height="56" alt="Screenshot 2025-09-14 201542" src="https://github.com/user-attachments/assets/80c74422-1723-4274-bd8d-a46ca7dc37a9" />


