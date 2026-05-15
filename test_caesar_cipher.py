import unittest

from caesar_cipher import caesar_cipher


class CaesarCipherTests(unittest.TestCase):
    def test_apple(self):
        self.assertEqual(caesar_cipher("Apple"), "Bqqmf")

    def test_banana(self):
        self.assertEqual(caesar_cipher("Banana"), "Cbobob")

    def test_max0815(self):
        self.assertEqual(caesar_cipher("Max0815"), "Nby0815")


if __name__ == "__main__":
    unittest.main()
