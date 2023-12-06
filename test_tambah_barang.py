import pandas as pd
import unittest
from unittest.mock import patch
from io import StringIO

fileName = "List Harga.csv"
ddata = pd.read_csv("List Harga.csv")

def tambah_barang():
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

class TestTambahBarang(unittest.TestCase):

    @patch('builtins.input', side_effect=['Cabe', 10000, 30])
    def test_tambah_barang_succesfull(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            tambah_barang()
        actual_output = mock_stdout.getvalue()
        expected_output = "Selamat, barang berhasil ditambahkan!"
        self.assertIn(expected_output, actual_output)

    @patch('builtins.input', side_effect=['Cabe', 'sepuluhribu', 'tigapuluh'])
    def test_tambah_barang_failed(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            tambah_barang()
        actual_output = mock_stdout.getvalue()
        expected_output = "Data gagal ditambahkan"
        self.assertIn(expected_output, actual_output)

if __name__ == '__main__':
    unittest.main()