class Pessoa:
    olhos = 2;

    def __init__(self, *filhos, nome=None, idade=30, olhos=2):
        self.olhos = olhos
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
    rafael.sobrenome = 'Faria'
    print(rafael.__dict__)
    print(julia.__dict__)
    del rafael.sobrenome
    print(rafael.__dict__)
    print(Pessoa.olhos)
    novaPessoa = Pessoa(nome="pessoa", olhos=1)
    print(novaPessoa.olhos)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(rafael.olhos)
