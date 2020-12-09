class Motor:
    """
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0
    """
    def __init__(self):
        self.velocidade = 0

    def acelerar (self):
        self.velocidade += 1

    def frear (self):
        self.velocidade = self.velocidade - 2 if self.velocidade >= 2 else 0

    def calcular_velocidade(self):
        return self.velocidade

class Direcao:
    """
    >>> # Testando Direcao
    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Norte'
    """
    girar = {
        'direita': {
            'Norte': 'Leste',
            'Leste': 'Sul',
            'Sul': 'Oeste',
            'Oeste': 'Norte'
        },
        'esquerda': {
            'Norte': 'Oeste',
            'Oeste': 'Sul',
            'Sul': 'Leste',
            'Leste': 'Norte'
        }
    }

    def __init__(self):
        self.valor = 'Norte'

    def calcular_direcao(self):
        return self.valor

    def girar_a_direita(self):
        self.valor = self.girar['direita'][self.valor]

    def girar_a_esquerda(self):
        self.valor = self.girar['esquerda'][self.valor]


class Carro:
    """
    >>> direcao = Direcao()
    >>> motor = Motor()
    >>> carro = Carro(direcao, motor)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    'Leste'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Oeste'
    """

    def __init__(self, direcao, motor):
        self.direcao = direcao
        self.motor = motor

    def calcular_velocidade(self):
        return self.motor.calcular_velocidade()

    def acelerar(self):
        return self.motor.acelerar()

    def frear(self):
        return self.motor.frear()

    def calcular_direcao(self):
        return self.direcao.calcular_direcao()

    def girar_a_direita(self):
        return self.direcao.girar_a_direita()

    def girar_a_esquerda(self):
        return self.direcao.girar_a_esquerda()
