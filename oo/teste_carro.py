import unittest
from oo.carro import Motor

class TesteCarro(unittest.TestCase):
    def teste_velocidade(self):
        motor = Motor()
        self.assertEqual(0, motor.velocidade)

    def teste_aceleracao(self):
        motor = Motor()
        motor.acelerar()
        self.assertEqual(1, motor.velocidade)


if __name__ == '__main__':
    unittest.main()
