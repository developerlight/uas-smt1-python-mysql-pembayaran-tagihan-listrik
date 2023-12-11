import mysql.connector
from datetime import date
from prettytable import PrettyTable

def conn():
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='db_pln'
    )
    return mydb

def getTanggal():
    today = date.today()
    tanggal = today.strftime("%Y-%m-%d")
    return tanggal

def show_pelanggan_daya():
    tabel = PrettyTable(['Id Pelanggan', 'Nama', 'Golongan Daya', 'Harga / Kwh'])
    kursor.execute('''select 
            tb_pelanggan.id_pelanggan, tb_pelanggan.nama, 
            tb_jenisdaya.daya, tb_jenisdaya.harga 
            from tb_jenisdaya, tb_pelanggan 
            where tb_pelanggan.kd_daya = tb_jenisdaya.kd_daya''')
    hasil = kursor.fetchall()
    for x in hasil:
        idpel = x[0]
        nama = x[1]
        gol = x[2]
        harga = x[3]
        tabel.add_row([idpel,nama,gol,harga])
    print(tabel)

def show_transaksi():
    tabel = PrettyTable(['Id Transaksi','Nama', 'Gologan Daya', 'KWH', 'Total Harga', 'Status'])
    kursor.execute('''select tb_transaksi.id_transaksi, tb_pelanggan.nama, tb_jenisdaya.daya, 
    tb_transaksi.kwh, tb_transaksi.total_harga, tb_transaksi.status
    from tb_pelanggan, tb_jenisdaya, tb_transaksi
    where tb_transaksi.id_pelanggan = tb_pelanggan.id_pelanggan 
    and tb_pelanggan.kd_daya = tb_jenisdaya.kd_daya''')
    hasil = kursor.fetchall()
    for i in hasil:
        id_transaksi = i[0]
        nama = i[1]
        gol =i[2]
        kwh = i[3]
        tot = i[4]
        status = i[5]
        tabel.add_row([id_transaksi,nama,gol,kwh,tot,status])
    print(tabel)

def insert_tbPelanggan(nama,gol):
    kursor = koneksi.cursor()
    sql = "insert into tb_pelanggan (nama, kd_daya) values (%s,%s)"
    val = (nama,gol)
    kursor.execute(sql,val)
    koneksi.commit()

def insert_transaksi(tanggal,kwh,total,primary):
    kursor = koneksi.cursor()
    sql = "insert into tb_transaksi (tanggal, kwh, total_harga, id_pelanggan) values(%s,%s,%s,%s)"
    val = (tanggal,kwh,total,primary)
    kursor.execute(sql,val)
    koneksi.commit()

def get_last_id():
    kursor.execute("select * from tb_pelanggan where id_pelanggan=last_insert_id()")
    hasil = kursor.fetchall()
    tup=hasil[0]
    return tup[0]

def masukan(ket):
    temp = input(f'Masukan {ket} : ')
    return temp

def input_data(kursor):
    #1. masukan nama
    nama = masukan('nama')
    #2. masukan golongan
    gol = int(masukan('golongan'))
    harga_gol = get_harga(kursor,gol)
    #3. masukan kwh
    kwh = int(masukan('kwh'))
    #4. proses bayar = harga_golongan * kwh
    total = (harga_gol * kwh)
    status = 'BELUM LUNAS'
    return nama, gol, kwh, harga_gol, total, status

def get_harga(kursor,gol):
    kursor.execute(f"select * from tb_jenisdaya where kd_daya like '{gol}'")
    hasil = kursor.fetchall()
    tampil = hasil[0]
    return tampil[2]

def get_total_harga(id_transaksi):
    kursor.execute(f"select * from tb_transaksi where id_transaksi like '{id_transaksi}'")
    hasil = kursor.fetchall()
    tampil = hasil[0]
    return tampil[3]

def showdb(kursor,tabel):
    kursor.execute(f'select * from {tabel}')
    hasil = kursor.fetchall()
    for i in hasil:
        print(i)

def menu_tampil_data():
    print('''
    1. tampil jenis daya
    2. tampil pelanggan
    3. tampil transaksi
    ''')
    x = int(input('-> '))
    return x

def menu_rekap():
    print('''
    1. Total Pengguna
    2. Total Penghasila''')
    x = int(input('-> '))
    return x

def get_status(kursor, id_transaksi):
    kursor.execute(f"select * from tb_transaksi where id_transaksi like '{id_transaksi}'")
    hasil = kursor.fetchall()
    tampil = hasil[0]
    return tampil[4]

def update_status():
    sql = f"update tb_transaksi set status = 'LUNAS' where id_transaksi = '{x}'"
    kursor.execute(sql)
    koneksi.commit()

def get_rekap_pengguna():
    lunas = 0
    blm_lunas = 0
    kursor.execute('select * from tb_transaksi')
    hasil = kursor.fetchall()
    for i in hasil:
        j = i[4]
        if j == 'LUNAS': lunas +=1
        elif j == 'BELUM LUNAS': blm_lunas +=1
    return lunas, blm_lunas

def get_rekap_total():
    lunas = 0
    blm_lunas = 0
    kursor.execute('select * from tb_transaksi')
    hasil = kursor.fetchall()
    for i in hasil:
        j = i[4]
        k = i[3]
        if j == 'LUNAS': lunas +=k
        elif j == 'BELUM LUNAS': blm_lunas +=k
    return lunas, blm_lunas

def menu_utama():
    print('''
    1. input data
    2. tampil data
    3. bayar
    4. rekap data
    5. exit''')
    x = int(input('-> ') or 0)
    return x

if __name__ == '__main__':
    nama = ''
    gol = 0
    primary=0
    kwh = 0
    harga = 0
    total = 0
    lunas = 0
    blm_lunas = 0
    status = ''
    tanggal = getTanggal()
    koneksi = conn()
    kursor = koneksi.cursor()
    while(True):
        #1. menu
        menu = menu_utama()
        #2. seleksi pilihan
        if (menu == 1):
            nama, gol, kwh, harga, total, status = input_data(kursor)
            # insert tb pelanggan
            insert_tbPelanggan(nama,gol)
            #ambil id terakhir
            primary = get_last_id()
            # insert ke table transaksi
            insert_transaksi(tanggal,kwh,total,primary)
        elif (menu == 2):
            x = menu_tampil_data()
            if x == 1:
                showdb(kursor,'tb_jenisdaya')
                #tampil jenis data
            elif x == 2:
                show_pelanggan_daya()
                #tampil pelangan
            elif x == 3:
                showdb(kursor,'tb_transaksi')
                #tampil transaksi
        elif (menu == 3):
            #show_pelanggan_daya()
            show_transaksi()
            x = int(input('-> '))
            status = get_status(kursor,x)
            if(status == 'LUNAS'):print('Maaf yang anda pilih sudah lunas')
            else:
                bayar = int(input('Bayar : '))
                total = get_total_harga(x)
                kembalian = bayar - total
                if (kembalian < 0): print('maaf uang anda kurang')
                else:
                    print(f'Kembalian   : {kembalian}')
                    update_status()
        elif (menu == 4):
            x = menu_rekap()
            # show_transaksi()
            if x == 1:
                lunas, blm_lunas = get_rekap_pengguna()
                print(f'Lunas : {lunas} Orang')
                print(f'Belum Lunas : {blm_lunas} Orang')
            elif x == 2:
                lunas, blm_lunas = get_rekap_total()
                print(f'Total Terbayarkan : Rp.{lunas}')
                print(f'Total Belum Terbayarkan : Rp.{blm_lunas}')
        elif (menu == 5):
            exit()