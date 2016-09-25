from unittest import TestCase
from Codigo import Codigo

class TestCodigo(TestCase):


    def test_solve_value(self):
        memoria = Codigo.solve_value("0x0010") # -16
        registrador = Codigo.solve_value("A") # -65
        valor = Codigo.solve_value("20")# 20

        self.assertEqual(-16, memoria)
        self.assertEqual(-65, registrador)
        self.assertEqual(20, valor)

