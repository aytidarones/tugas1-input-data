# Simpan semua data karyawan
allKaryawan = []

def isValid(text):
    for char in text:
        if not char.isalpha() and char != " ":
            return False
    return True

while True:
    print("\n=== Input Data Karyawan ===")

    # Input NAMA
    while True:
        inputNama = input("Nama    : ")
        if isValid(inputNama):
            break
        print("Input hanya boleh huruf dan spasi!")

    # Input KOTA
    while True:
        inputKota = input("Kota    : ")
        if isValid(inputKota):
            break
        print("Input hanya boleh huruf dan spasi!")

    # Input JABATAN
    inputJabatan = input("Jabatan : ")

    # Input GAJI
    while True:
        inputGaji = input("Gaji    : ")
        if inputGaji.isdigit():
            inputGaji = int(inputGaji)
            break
        print("Gaji harus berupa angka!")

    # Simpan ke list
    dataKaryawan = {
        'nama'   : inputNama,
        'kota'   : inputKota,
        'jabatan': inputJabatan,
        'gaji'   : inputGaji
    }
    allKaryawan.append(dataKaryawan)
    print("Data tersimpan!")

    # Tanya tambah data lagi
    tambahLagi = input("\nTambah data karyawan lagi? (y/n) : ")
    if tambahLagi.lower() != "y":
        break

# Pilih data
while True:
    pilihData = input(f"\nPilih data untuk ditampilkan (0 = semua, 1-{len(allKaryawan)} = pilih, q = keluar) : ")

    if pilihData == "q":
        print("Keluar...")
        break
    elif not pilihData.isdigit():
        print("Input harus angka!")
    else:
        pilihData = int(pilihData)
        if pilihData == 0:
            print("\n=== Semua Data ===")
            for i, karyawan in enumerate(allKaryawan, start=1):
                print(f"{i}. {karyawan}")
        elif 1 <= pilihData <= len(allKaryawan):
            print(f"\n=== Data #{pilihData} ===")
            print(allKaryawan[pilihData - 1])
        else:
            print("Data tidak ada!")