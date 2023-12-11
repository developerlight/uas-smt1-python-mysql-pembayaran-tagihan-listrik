# Electricity Payment System using Python and MySQL

![Electricity](https://img.icons8.com/cotton/2x/electricity.png)

Welcome to the Electricity Payment System, a Python program with MySQL integration for managing electricity customer data and transactions. This system provides a set of functionalities including customer data input, transaction processing, data display, and financial recap.

## Prerequisites

1. Install the required Python libraries:
   ```bash
   pip install mysql-connector-python prettytable
   ```

2. Set up a MySQL server with the database named `db_pln`. Update the MySQL connection details in the `conn()` function.

## How to Use

1. Run the program:
   ```bash
   python main_utama.py
   ```

2. Choose the desired menu option:
   - **Input Data (1)**: Enter customer data and initiate transactions.
   - **Display Data (2)**: View information about customers, transactions, or electricity categories.
   - **Payment (3)**: Process payments for customers.
   - **Rekap Data (4)**: View financial recaps.
   - **Exit (5)**: Exit the program.

## Database Structure

- **Tables**:
  - `tb_pelanggan`: Customer data including ID, name, and electricity category.
  - `tb_jenisdaya`: Electricity category data including ID, category, and price per kWh.
  - `tb_transaksi`: Transaction data including ID, date, kWh, total price, and payment status.

## Program Output

```bash
------------------------------
1. input data
2. tampil data
3. bayar
4. rekap data
5. exit
-> 1
Masukan nama : John Doe
Masukan golongan : 1
Masukan kwh : 100
------------------------------
1. input data
2. tampil data
3. bayar
4. rekap data
5. exit
-> 2

------------------------------
1. tampil jenis daya
2. tampil pelanggan
3. tampil transaksi
-> 2
+--------------+---------+--------------+--------------+
| Id Pelanggan |   Nama  | Golongan Daya| Harga / Kwh  |
+--------------+---------+--------------+--------------+
|      1       | John Doe|      1300    |     1500     |
+--------------+---------+--------------+--------------+
------------------------------
1. input data
2. tampil data
3. bayar
4. rekap data
5. exit
-> 3

------------------------------
1. Id Transaksi |     Nama      | Gologan Daya | KWH | Total Harga |   Status    |
+--------------+---------------+--------------+-----+-------------+-------------+
|      1       | John Doe      |      1300    | 100 |    150000   | BELUM LUNAS |
+--------------+---------------+--------------+-----+-------------+-------------+
Pilih ID Transaksi untuk membayar: 1
Bayar : 200000
Kembalian   : 50000
------------------------------
1. input data
2. tampil data
3. bayar
4. rekap data
5. exit
-> 4

------------------------------
1. Total Pengguna
2. Total Penghasila
-> 2
Total Terbayarkan : Rp.150000
Total Belum Terbayarkan : Rp.0
------------------------------
1. input data
2. tampil data
3. bayar
4. rekap data
5. exit
-> 5
Terima kasih
------------------------------
```

## Contributions

Contributions are welcome! Feel free to create pull requests or report issues through GitHub.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Thank you for using the Electricity Payment System! ⚡🔧
