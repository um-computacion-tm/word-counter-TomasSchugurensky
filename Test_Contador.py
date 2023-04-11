import unittest
from ContarPalabras import contar_palabras
class Test_Contador (unittest.TestCase):
    def test_palabrachica(self):
       resultado = contar_palabras ("hola mundo")
       self.assertEqual (resultado, {"hola":1, "mundo":1})

if __name__ == "__main__":
    unittest.main()
