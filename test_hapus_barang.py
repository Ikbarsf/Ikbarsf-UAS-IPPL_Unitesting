import pandas as pd
import unittest
from unittest.mock import patch
from io import StringIO

fileName = "List Harga.csv"
ddata = pd.read_csv("List Harga.csv")

def tambah_barang():
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

class TestHapusBarang(unittest.TestCase):

    @patch('builtins.input', side_effect=[1])
    def test_hapus_barang_succesfull(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            tambah_barang()
        actual_output = mock_stdout.getvalue()
        expected_output = "Selamat, barang berhasil dihapus!"
        self.assertIn(expected_output, actual_output)

    @patch('builtins.input', side_effect=[10])
    def test_hapus_barang_failed(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            tambah_barang()
        actual_output = mock_stdout.getvalue()
        expected_output = "Data yang anda pilih tidak tersedia"
        self.assertIn(expected_output, actual_output)

if __name__ == '__main__':
    unittest.main()