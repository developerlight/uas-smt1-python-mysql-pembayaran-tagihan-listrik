from prettytable import PrettyTable

#fungsi input
def masukan(ket):
    temp = input(f'Masukan {ket} : ')
    return temp

#fungsi proses
def golongan(dictnya, gol):
    harga = dictnya[gol-1].get(gol)
    return harga

def proses_bayar(harga,kwh):
    total = harga * kwh
    return total

def input_data(dictnya):
    #1. masukan nama
    nama = masukan('nama')
    #2. masukan golongan
    gol = int(masukan('golongan'))
    harga_gol = golongan(dictnya,gol)
    #3. masukan kwh
    kwh = int(masukan('kwh'))
    #4. proses bayar = harga_golongan * kwh
    total = proses_bayar(harga_gol,kwh)
    status = 'Belum Lunas'
    return nama, gol, kwh, harga_gol, total, status

def input_list(list_rekap, nama, gol, kwh, harga, total, status):
    temp = {
    'nama':nama, 
    'golongan':gol, 
    'kwh':kwh, 
    'harga':harga, 
    'total':total, 
    'status':status}
    list_rekap.append(temp)
    return list_rekap

def rek_pengguna(data_list):
    temp = 0
    tempp = 0
    for i in range(len(data_list)):
        status = data_list[i].get('status')
        if (status == 'LUNAS'):
            temp +=1
        elif (status == 'Belum Lunas'):
            tempp +=1
    return temp, tempp

def rek_lunas(data):
    lunas = 0
    status = ''
    for i in range(len(data)):
        status = data[i].get('status')
        if (status == 'LUNAS'):
            lunas += data[i].get('total')
    return lunas

def rek_blm_lunas(data):
    lunas = 0
    status = ''
    for i in range(len(data)):
        status = data[i].get('status')
        if (status == 'Belum Lunas'):
            lunas += data[i].get('total')
    return lunas

def proses_rekap(x, rekap):
    if x == 1:
        pengguna_lunas, pengguna_blm_lunas = rek_pengguna(rekap)
        out_rekap_pengguna('sudah', pengguna_lunas)
        out_rekap_pengguna('belum', pengguna_blm_lunas)
    elif x == 2:
        penghasilan = rek_lunas(rekap)
        blm_bayar = rek_blm_lunas(rekap)
        garis()
        out_rekap_bayar('sudah', penghasilan)
        out_rekap_bayar('belum', blm_bayar)
        # keluaran('Sudah Bayar',penghasilan)
        # keluaran('Belum Bayar', blm_bayar)
        garis()
    elif x == 0:
        msg('Pilihan tidak boleh kosong!')
    else:
        msg(f'Pilihan {x} tidak ada')

def get_total_harga(index, list_data):
    harga = int(list_data[index].get('total')) 
    return harga

def get_kembalian(nominal, harga):
    kembalian = nominal - harga
    return kembalian

def get_data(index, data):
    data[index].update({'status':'LUNAS'})
    nama = data[index].get('nama')
    gol = data[index].get('golongan')
    kwh = data[index].get('kwh')
    harga = data[index].get('harga')
    total = data[index].get('total')
    status = data[index].get('status')
    return nama, gol, kwh, harga, total, status

def update_data(index,list_rekap, nama, gol, kwh, harga, total, status):
    temp = {'nama':nama, 'golongan':gol, 'kwh':kwh, 'harga':harga, 'total':total, 'status':status}
    #list_rekap.insert(index, temp)
    list_rekap[index] = temp
    return list_rekap

#fungsi tampilan

def tampil(data):
    tabel = PrettyTable(['nama', 'golongan', 'kwh', 'harga', 'total', 'status'])
    for i in data:
        nama = i.get('nama')
        golongan = i.get('golongan')
        kwh = i.get('kwh')
        harga = i.get('harga')
        total = i.get('total')
        status = i.get('status')
        tabel.add_row([nama, golongan, kwh, harga, total, status])
    tabel.add_autoindex('No.')
    print(tabel)

def out_rekap_bayar(ket, nominal):
    print(f'total {ket} dibayar : Rp.{nominal}')

def out_rekap_pengguna(ket, data):
    print(f'jumlah {ket} bayar : {data} Orang')

def msg(ket):
    print(f'{ket}')

def garis():
    print(f'------------------------------')

def keluaran(ket, data):
    print(f'Jumlah {ket} : {data}')

def struk_tampil(index, list_rekap):
    for index in list_rekap:
        nama = index.get('nama')
        gol = index.get('golongan')
        kwh = index.get('kwh')
        harga = index.get('harga')
        total = index.get('total')
        status = index.get('status')

        print(f'''
    Nama        : {nama}
    Golongan    : {gol}
    kWh         : {kwh} kWh
    Harga/kWh   : Rp.{harga}
    Total       : Rp.{total}
    Status      : {status}
    ''')

def menu_tampil():
    print('''
    1. Tampilan Tabel
    2. Tampilan Struk''')
    x = int(input('-> ') or 0)
    return x

def menu_rekap():
    print('''
    1. Total Pengguna
    2. Total Penghasilan''')
    temp = int(input('-> ') or 0)
    return temp

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
    list_rekap=[]
    list_golongan=[{1:1300},{2:1500}]
    total = 0
    harga = 0
    subharga = 0
    kwh = 0
    gol = 0
    bayar = 0
    kembalian = 0
    pilih = 0
    nama = ''
    status = ''
    while(True):
        #1. menu
        garis()
        pilih = menu_utama()
        garis()
        #2. jika pilih 1 =  inputkan data dan simpan data
        #                   ke list of dictionary
        if pilih == 1 :
            nama, gol, kwh, harga, total, status = input_data(list_golongan)
            list_rekap = input_list(list_rekap,nama, gol, kwh, harga, total, status)
        #3. jika pilih 2 = tampilkan data
        elif pilih == 2 :
            #3.1 menampilkan data
            garis()
            tampil(list_rekap)
            garis()
        #4. Jika pilih 3 = proses pembayaran
        elif pilih == 3 :
            #4.1 tampil data
            garis()
            tampil(list_rekap)
            garis()
            #4.2 pilih data
            x = int(input('-> ')) - 1
            if (x in range(len(list_rekap))):
                #4.3 masukan uang bayar
                bayar = int(masukan('uang'))
                #4.3.1 ambil harga pelanggan
                subharga = get_total_harga(x, list_rekap)
                #4.3.1 proses pembayaran
                #       Jika kurang batalkan operasi
                if (bayar < subharga):
                    print('Uang anda kurang')
                #       Jika lebih atau pas jalankan operasi
                else:
                    kembalian = get_kembalian(bayar,subharga)
                    #4.3.2 tampil struk
                    keluaran('sisa', kembalian)
                    #4.4 ubah status menjadi lunas
                    nama, gol, kwh, harga, total, status = get_data(x, list_rekap)
                    list_rekap = update_data(x, list_rekap,nama, gol, kwh, harga, total, status)
                    #tampil(list_rekap)
                    struk_tampil(x, list_rekap)
            else:
                msg('Data tidak ada!')
        #5. jika pilih 4 = proses rekap data
        elif pilih == 4 :
            garis()
            x = menu_rekap()
            garis()
            #5.1 jika pilih 1 = tampil total pengguna
            #5.2 jika pilih 2 = tampil total penghasilan
            proses_rekap(x,list_rekap)
        #6. jika pilih 5 = selesai
        elif pilih == 5:
            msg('Terima kasih')
            garis()
            exit()
        elif pilih == 0:
            msg('Pilihan tidak boleh kosong')
        else:
            msg(f'Pilihan {pilih} tidak ada')    