class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        return f'Olá ${id(self)}'


if __name__ == '__main__':
    pessoa = Pessoa('Rafael')
    print(Pessoa.cumprimentar(pessoa))
    print(id(pessoa))
    print(pessoa.cumprimentar())
    print(pessoa.nome)
    pessoa.idade = 29
    print(pessoa.idade)
