import unittest
from ContarPalabras import contar_palabras
class Test_Contador (unittest.TestCase):
    def test_palabrachica(self):
        frase = "hola mundo"
        self.assertEqual (contar_palabras(frase),{"hola": 1, "mundo": 1})
    def test_palabragrande(self):
        frase = "hola mundo hola que tal todos"
        self.assertEqual(contar_palabras(frase), {"hola":2, "mundo":1, "que":1,"tal":1,"todos":1})

if __name__ == "__main__":
    unittest.main()
