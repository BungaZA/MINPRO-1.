# Mini Project: Sistem Pendaftaran Acara

# Pilihan

print("=== SISTEM PENDAFTARAN ACARA ===")
print("Pilih:")
print("1. Daftarkan peserta")
print("2. Tampilkan daftar peserta")
print("3. Ubah data peserta")
print("4. Batalkan pendaftaran")
print("5. Keluar")

# Daftar peserta(id, nama, email)

peserta = [('A001', 'Paimon', 'Paimon@gmail.com'),
('A002', 'Lumine', 'Lumine@gmail.com'),
('A003', 'Aether', 'Aether@gmail.com')]

pilih = input("masukkan nomor pilihan (1-5):")

# 1. Daftarkan peserta(Create)

if pilih == "1":
    print("\n DAFTARKAN PESERTA BARU ")
    ID = input("Masukkan ID peserta:")
    Nama = input("Masukkan Nama peserta:")
    Email = input("Masukkan Email Peserta:")
    peserta_baru = (ID, Nama, Email)
    peserta.append(peserta_baru)
    print("\nPeserta berhasil didaftarkan:")
    print(peserta_baru)
    print("\nDaftar Peserta Saat ini:")
    print(*peserta, sep="\n")
    print("\n PROGRAM SELESAI")
    print(" TERIMAKASIH ❤️")

# 2. Tampilkan daftar peserta(Read)
elif pilih == "2":
    print("\n DAFTAR PESERTA TERDAFTAR ")
    if len(peserta) == 0:
        print("Tidak ada peserta terdaftar")
    else:
        print("Total peserta:", len(peserta))
        print(*peserta, sep="\n")

# 3. Ubah data peserta(Update)
elif pilih == "3":
    print("\n UBAH DATA PESERTA ")
    if len(peserta) == 0:
        print("Tidak ada peserta yang bisa diubah")
    else:
        print("daftar peserta saat ini:")
        print(*peserta, sep="\n")
        nomor = int(input("\nMasukkan Urutan peserta yang ingin diubah (dimulai dari angka 0):"))
        if nomor < 0 or nomor >= len(peserta):
            print("Urutan melebihi peserta yang ada. Silahkan Ulangi Lagi")
        else:
            print("Data peserta yang dipilih:", peserta[nomor])
            ID_update = input("Masukkan ID peserta:")
            Nama_update = input("Masukkan Nama peserta:")
            Email_update = input("Masukkan Email Peserta:")
            peserta_update = (ID_update, Nama_update, Email_update)
            print("\nData peserta yang di perbaharui:")
            print(peserta_update)
            peserta[nomor] = peserta_update
            print("\nDaftar peserta saat ini:")
            print(*peserta, sep="\n")
            print("\n PROGRAM SELESAI")
            print(" TERIMAKASIH ❤️")

# 4. Batalkan pendaftaran (Delete)
elif pilih == "4":
    print("\n BATALKAN PENDAFTARAN ")
    if len(peserta) == 0:
        print("Tidak ada peserta yang bisa dihapus")
    else:
        print("Daftar peserta saat ini:")
        print(*peserta, sep="\n")
        nomor = int(input("\nMasukkan Urutan peserta yang ingin dihapus (dimulai dari angka 0):"))
        if nomor < 0 or nomor >= len(peserta):
            print("Urutan melebihi peserta yang ada. Silahkan Ulangi Lagi")
        else:
            terhapus = peserta.pop(nomor)
            print("\nPendaftaran berhasil dibatalkan untuk peserta:")
            print(terhapus)
            print("\nDaftar peserta sekarang:")
            if len(peserta) == 0:
                print("Tidak ada peserta terdaftar")
            else:
                print(*peserta, sep="\n")
                print("\n PROGRAM SELESAI")
                print(" TERIMAKASIH ❤️")

# 5. Keluar
else:
    print("\nKeluar atau pilihan tidak dikenali")
    print(" PROGRAM SELESAI")
    print(" TERIMAKASIH ❤️")