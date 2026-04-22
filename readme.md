# Program Input Data Karyawan
 
Program sederhana berbasis terminal untuk meng-input, menyimpan, dan menampilkan data karyawan menggunakan bahasa pemrograman Python.
 
---
 ## Fitur
- Input data karyawan berupa nama, kota, jabatan, dan gaji
- Validasi input nama dan kota (hanya huruf dan spasi yang akan diterima sebagai karakter)
- Validasi input gaji (hanya angka yang akan diterima sebagai data input)
- Menyimpan banyak data karyawan sekaligus
- Menampilkan semua data atau data tertentu berdasarkan opsi yang dipilih
---

## Alur Program
 
```
START
  │
  ▼
Input Nama → valid? → No → ulangi 
  │ Yes
  ▼
Input Kota → valid? → No → ulangi
  │ Yes
  ▼
Input Jabatan
  │
  ▼
Input Gaji → digit? → No → ulangi
  │ Yes
  ▼
Simpan ke allKaryawan
  │
  ▼
Tambah lagi? → Yes → kembali ke Input Nama
  │ No
  ▼
Pilih Data
  ├── 0       → Tampilkan semua
  ├── 1 - n   → Tampilkan data ke-n
  ├── q       → Keluar
  └── lainnya → "Data tidak ada!"
```
 
---