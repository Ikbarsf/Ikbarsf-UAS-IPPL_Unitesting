import unittest
from unittest.mock import patch

user_penjual = ['afif']
pw_penjual = ['afif123']

# Fungsi yang akan diuji
def masuk_penjual():
    user = input("Masukkan Username Anda : ")
    passw = input("Masukkan Password Anda : ")
    if user in user_penjual and passw in pw_penjual and user_penjual.index(user) == pw_penjual.index(passw):
        return "Login Berhasil!"
    else:
        return "Username atau Password yang Anda masukkan salah!"

class TestMasukPenjual(unittest.TestCase):
    
    @patch('builtins.input', side_effect=['afif', 'afif123'])  # Penggunaan input untuk username dan password
    def test_login_correct_credentials(self, mock_input):
        self.assertEqual(masuk_penjual(), "Login Berhasil!")

    @patch('builtins.input', side_effect=['user_wrong', 'afif123'])  # Username salah, password benar
    def test_login_wrong_username(self, mock_input):
        self.assertEqual(masuk_penjual(), "Username atau Password yang Anda masukkan salah!")

    @patch('builtins.input', side_effect=['afif', 'wrong_password'])  # Username benar, password salah
    def test_login_wrong_password(self, mock_input):
        self.assertEqual(masuk_penjual(), "Username atau Password yang Anda masukkan salah!")

    @patch('builtins.input', side_effect=['user_wrong', 'wrong_password'])  # Keduanya salah
    def test_login_wrong_credentials(self, mock_input):
        self.assertEqual(masuk_penjual(), "Username atau Password yang Anda masukkan salah!")

if __name__ == '__main__':
    unittest.main()
