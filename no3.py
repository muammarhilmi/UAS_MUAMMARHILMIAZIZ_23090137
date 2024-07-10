from modul import AntrianRestoran

def main():
    antrian = AntrianRestoran()

    while True:
        print('\nAntrian sekarang:', list(antrian.antrian))
        print('Jumlah antrian:', len(antrian.antrian))
        print('Pilihan:')
        print('1. Tambah Antrian')
        print('2. Antrian Selanjutnya')
        print('3. Lihat Antrian')
        print('4. Keluar\n')
        pilihan = input('Pilih Operasi (1/2/3/4): ')

        if pilihan == '1':
            nama_pelanggan = input('Masukkan nama pelanggan: ')
            antrian.enqueue(nama_pelanggan)
        elif pilihan == '2':
            antrian.dequeue()
        elif pilihan == '3':
            antrian.tampilkan_antrian()
        elif pilihan == '4':
            print("Terima kasih telah menggunakan sistem antrian restoran.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()