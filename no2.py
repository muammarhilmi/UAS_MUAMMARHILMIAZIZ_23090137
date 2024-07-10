nilai = [
    [90, 80],  # Siswa 1: Algoritma dan Struktur Data 2 = 90, Matematika Numerik = 80
    [50, 60],  # Siswa 2: Algoritma dan Struktur Data 2 = 50, Matematika Numerik = 60
    [65, 70]   # Siswa 3: Algoritma dan Struktur Data 2 = 65, Matematika Numerik = 70
]

rata_rata_nilai = []
for i in range(len(nilai[0])):
    rata_rata = sum([nilai_siswa[i] for nilai_siswa in nilai]) / len(nilai)
    rata_rata_nilai.append(rata_rata)

print("Rata-rata nilai untuk setiap mata kuliah:")
print(f"Algoritma dan Struktur Data 2: {rata_rata_nilai[0]:.2f}")
print(f"Matematika Numerik: {rata_rata_nilai[1]:.2f}")

rata_rata_nilai_mahasiswa = []
for nilai_siswa in nilai:
    rata_rata = sum(nilai_siswa) / len(nilai_siswa)
    rata_rata_nilai_mahasiswa.append(rata_rata)

print("Rata-rata nilai untuk setiap Mahasiswa:")
for i, rata_rata in enumerate(rata_rata_nilai_mahasiswa, 1):
    print(f"Mahasiswa {i}: {rata_rata:.2f}")