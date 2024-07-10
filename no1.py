mahasiswa = []

while True:
    nim = input("Masukan NIM: ")
    nama = input("Masukan nama: ")

    data_mahasiswa = {"NIM": nim, "Nama": nama}
    mahasiswa.append(data_mahasiswa)

    response = input("Ingin tambah lagi? (iya/tidak): ")
    if response.lower() == "tidak":
        break

print("Data Mahasiswa:")
for i, mahasiswa in enumerate(mahasiswa, 1):
    print(f"Mahasiswa {i}:")
    print(f"  NIM: {mahasiswa['NIM']}")
    print(f"  Nama: {mahasiswa['Nama']}")
    print()