# Program Input Data Karyawan
 
Program sederhana berbasis terminal untuk menginput, menyimpan, dan menampilkan data karyawan menggunakan Python.
 
---
 ## Fitur
- Input data karyawan (nama, kota, jabatan, gaji)
- Validasi input nama dan kota (hanya huruf dan spasi)
- Validasi input gaji (hanya angka)
- Menyimpan banyak data karyawan sekaligus
- Menampilkan semua data atau data tertentu
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
  └── lainnya → "Data not match!"
```
 
---