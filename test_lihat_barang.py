import pandas as pd
import unittest
from unittest.mock import patch
from io import StringIO

fileName = "List Harga.csv"
fileNameEmpty = "List Harga Kosong.csv"

def lihat_barang():
    global ddata
    ddata = pd.read_csv(fileName)
    print("Berhasil Melihat Data Barang")
    print(ddata)

def lihat_barang_kosong():
    global ddata
    ddata = pd.read_csv(fileNameEmpty)
    print(ddata)


class TestLihatBarang(unittest.TestCase):
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_lihat_barang_data_exists(self, mock_stdout):        
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            lihat_barang()
        actual_output = mock_stdout.getvalue()
        expected_output = "Berhasil Melihat Data Barang"  
        # Sesuaikan dengan output yang diharapkan
        self.assertIn(expected_output, actual_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_lihat_barang_empty_data(self, mock_stdout):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            lihat_barang_kosong()
        actual_output = mock_stdout.getvalue()
        expected_output = "Tidak ada barang tersedia."  # Output yang diharapkan jika data kosong
        self.assertIn(expected_output, actual_output)

if __name__ == '__main__':
    unittest.main()
