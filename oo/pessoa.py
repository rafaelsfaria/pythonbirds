class Pessoa:
    def __init__(self, *filhos, nome=None, idade=30):
        self.nome = nome
        self.idade = idade
        self.filhos = filhos

    def cumprimentar(self):
        return f'Olá ${id(self)}'


if __name__ == '__main__':
    rafael = Pessoa(nome='Rafael', idade=10)
    julia = Pessoa(rafael, 'Julia')
    print(Pessoa.cumprimentar(rafael))
    print(id(rafael))
    print(rafael.cumprimentar())
    print(rafael.nome)
    print(rafael.idade)
    print(julia.filhos)
