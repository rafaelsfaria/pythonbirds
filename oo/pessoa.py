class Pessoa:
    def __init__(self, *filhos, nome=None, idade=30):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá ${id(self)}'


if __name__ == '__main__':
    rafael = Pessoa(nome='Rafael', idade=10)
    julia = Pessoa(rafael, nome='Julia')
    print(Pessoa.cumprimentar(rafael))
    print(id(rafael))
    print(rafael.cumprimentar())
    print(rafael.nome)
    print(rafael.idade)
    for filho in julia.filhos:
        print(filho.nome)

