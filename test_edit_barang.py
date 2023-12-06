import pandas as pd
import unittest
from unittest.mock import patch
from io import StringIO

fileName = "List Harga.csv"
ddata = pd.read_csv("List Harga.csv")

def edit_barang():
    global ddata
    print(ddata)
    ubah = int(input("Stock yang ingin diubah : "))
    ganti = int(input("Ubah menjadi : "))
    ddata.at[ubah,"Stock"] = ganti
    ddata.to_csv(fileName, index= False)
    print("Selamat, Data berhasil diupdate")
    print(ddata)
    print("Silahkan cek pada menu Lihat Barang")

class TestEditBarang(unittest.TestCase):

    @patch('builtins.input', side_effect=[1, 100])
    def test_edit_barang_succesfull(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            edit_barang()
        actual_output = mock_stdout.getvalue()
        expected_output = "Selamat, Data berhasil diupdate"
        self.assertIn(expected_output, actual_output)

    @patch('builtins.input', side_effect=['2', '50'])
    def test_edit_barang_failed(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            edit_barang()
        actual_output = mock_stdout.getvalue()
        expected_output = "Data gagal diupdate"
        self.assertIn(expected_output, actual_output)

if __name__ == '__main__':
    unittest.main()