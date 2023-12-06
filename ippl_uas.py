import pandas as pd 
import os
import time

fileName = "List Harga.csv"
ddata = pd.read_csv("List Harga.csv")

user_penjual = ['afif']
pw_penjual = ['afif123']
user_pembeli = ['ikbar']
pw_pembeli = ['ikbar123']


def clearscreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def lihat_barang():
    global ddata
    print(ddata)
    print("Berhasil Melihat Data Barang")
    kembali_penjual()

def lihat_menu():
    global ddata
    print(ddata)

def kembali_pembeli():
    input("\nTekan ENTER untuk kembali...")
    menu_pembeli()

def kembali_penjual():
    input("\nTekan ENTER untuk kembali...")
    menu_penjual()    

def awal() :
    clearscreen()
    print("=" *70)
    print("SELAMAT DATANG DI NEETANI".center(70))
    print("=" *70)
    y = int(input("""
        Masuk sebagai : 
        [1] Penjual
        [2] Pembeli
        [3] Log Out
        Pilih >>> """))

    if y == 1:
        masuk_penjual()
    elif y == 2:
        menu_pembeli()
    elif y == 3:
        print("\n")
        print("=" *70)
        print("TERIMA KASIH".center(70))
        print("=" *70)

def menu_pembeli():
    clearscreen()
    print("=" *70)
    print("HALO, NEES!".center(70))
    print("=" *70)
    pilih_awal = int(input(""" 
        [1] Masuk
        [2] Kembali
        Pilih >>> """))
    if pilih_awal == 1:
        masuk_pembeli()
    # elif pilih_awal == 2:
    #     masuk()
    else:
        awal()

# def registrasi():
    # clearscreen()
    # print(" REGISTRASI ".center(70, "="))
    # user = input("Masukkan Username Anda : ")
    # passw = input("Masukkan Password Anda : ")
    # if user != "" and passw != "" and user != "Penjual" and passw != "0000":
    #     print("Registasi akun Anda berhasil!".center(70, "-"))
    #     print("=" *70)
    #     time.sleep(1.5)
    #     masuk()
    # else:
    #     print("Registrasi akun Anda gagal! Mohon masukkan data dengan benar!".center(70, "-"))
    #     print("=" *70)
    #     time.sleep(1.5)
    #     awal()

def masuk_pembeli():
    print(" LOGIN ".center(70,"="))
    user = input ("Masukkan Username Anda : ")
    passw = input("Masukkan Password Anda : ")
    if user in user_pembeli and passw in pw_pembeli and user_pembeli.index(user) == pw_pembeli.index(passw):
        print("Login Berhasil!".center(70, "-"))
        print("=" *70)
        time.sleep(1.5)
        beli()
    else:
        print("Username atau Password yang Anda masukkan salah!".center(70, "-"))
        print("=" *70)
        time.sleep(1.5)
        awal()

def masuk_penjual():
    print(" LOGIN ".center(70,"="))
    global user
    user = input ("Masukkan Username Anda : ")
    passw = input("Masukkan Password Anda : ")
    if user in user_penjual and passw in pw_penjual and user_penjual.index(user) == pw_penjual.index(passw):
        print("Login Berhasil!".center(70, "-"))
        print("=" *70)
        time.sleep(1.5)
        menu_penjual()
    else:
        print("Username atau Password yang Anda masukkan salah!".center(70, "-"))
        print("=" *70)
        time.sleep(1.5)
        awal()
        
def beli():
    lihat_menu()
    apa = int(input("Apa yang ingin dibeli : "))
    brp = int(input("Ingin membeli berapa barang? "))
    ganti = int(ddata.at[apa,"Stock"])-brp
    jumlah = int(brp*ddata.at[apa,"Harga Rp/kg"])  
    ddata.at[apa,"Stock"] = ganti
    print(f"Jumlah total yang harus dibayar adalah Rp{jumlah}")
    ddata.to_csv(fileName, index = False)
    print("Total pembelian anda : ", f"{jumlah}")
    bayar = int(input("Bayar : "))
    if bayar < jumlah :
        print("Uang yang anda berikan kurang!")
    else :
        kembali = bayar - jumlah
        print("Kembalian Anda :", kembali)
        print("=" *70)
        print("TERIMA KASIH TELAH BERBELANJA DI NEETANI")
        print("=" *70)

def menu_penjual():
    clearscreen()
    print("=" *70)
    # print("HALO," + user + "!".center(70))
    header = "HALO, " + user.upper() + "!"
    print(header.center(70))
    print("=" *70)
    pilihDua = int(input("""
                    Menu :
                    [1] Lihat Barang
                    [2] Tambah Barang
                    [3] Hapus Barang
                    [4] Edit Barang
                    [5] Keluar dan Simpan
                    Pilih >>> """))   
    clearscreen()
    if pilihDua == 1:
        lihat_barang()
    elif pilihDua == 2:
        tambah_barang()
    elif pilihDua == 3:
        hapus_barang()
    elif pilihDua == 4:
        edit_barang()
    elif pilihDua == 5:
        ddata.to_csv(fileName, index= False)
        exit()
    else:
        print("-" *70)
        print("Menu yang Anda pilih tidak tersedia!")
        print("-" *70)
        time.sleep(1.5)
        menu_penjual()

def tambah_barang():
    clearscreen()
    global ddata
    print(ddata)
    nama_barang = input("Nama Barang : ")
    harga_barang = input("Harga : ")
    jumlah_barang = input("Jumlah barang yang akan ditambahkan : ")
    ddata.loc[len(ddata)] = {"Nama Barang": nama_barang,"Harga Rp/kg": harga_barang,"Stock": jumlah_barang}
    ddata.index = list(range(len(ddata)))
    ddata.to_csv(fileName, index = False)
    print("\nSelamat, barang berhasil ditambahkan!")
    print(ddata)
    print("Silakan cek pada menu Lihat Barang")
    kembali_penjual()

def hapus_barang():
    clearscreen()
    global ddata
    print(ddata)
    hapusss = int(input("Yang ingin dihapus : "))
    ddata.drop(index= hapusss,
            inplace=True)
    ddata.index = list(range(len(ddata)))
    ddata.to_csv(fileName, index= False)
    print("Selamat, barang berhasil dihapus!")
    print(ddata)
    print("Silakan cek pada menu Lihat Barang")
    kembali_penjual()

def edit_barang():
    clearscreen()
    global ddata
    print(ddata)
    ubah = int(input("Stock yang ingin diubah : "))
    ganti = int(input("Ubah menjadi : "))
    ddata.at[ubah,"Stock"] = ganti
    ddata.to_csv(fileName, index= False)
    print("Selamat, Data berhasil diupdate")
    print(ddata)
    print("Silahkan cek pada menu Lihat Barang")
    kembali_penjual()

awal()