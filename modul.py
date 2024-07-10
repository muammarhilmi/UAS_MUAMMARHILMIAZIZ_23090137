from collections import deque

class AntrianRestoran:
    def __init__(self):
        self.antrian = deque()

    def enqueue(self, nama_pelanggan):
        self.antrian.append(nama_pelanggan)
        print(f'{nama_pelanggan} ditambahkan ke dalam antrian.')

    def dequeue(self):
        if len(self.antrian) > 0:
            pelanggan = self.antrian.popleft()
            print(f'{pelanggan} dilayani dan dihapus dari antrian.')
            return pelanggan
        else:
            print('Antrian kosong, tidak ada pelanggan untuk dilayani.')
            return None

    def tampilkan_antrian(self):
        """Menampilkan seluruh pelanggan dalam antrian."""
        print('=== DAFTAR ANTRIAN ===')
        if len(self.antrian) == 0:
            print('Antrian kosong.')
        else:
            for i, pelanggan in enumerate(self.antrian, start=1):
                print(f'{i}. {pelanggan}')