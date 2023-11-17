import unittest
from division import dividir

class TestDividir(unittest.TestCase):

    def test_dividir(self):
        #Casos normales
        self.assertEqual(dividir(6, 3), (2, 0))
        self.assertEqual(dividir(9, 2), (4, 1))

        #Casos de division por 0
        with self.assertRaises(ZeroDivisionError):
            dividir(5,0)
        
        with self.assertRaises(ZeroDivisionError):
            dividir(0,0)

if __name__ == "__main__":
    unittest.main()