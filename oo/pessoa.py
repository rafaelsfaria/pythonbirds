class Pessoa:
    olhos = 2;

    def __init__(self, *filhos, nome=None, idade=30, olhos=2):
        self.olhos = olhos
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá ${id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributo_da_classe(cls):
        return f'nome: {cls}, olhos: {cls.olhos}'


class Homem(Pessoa):
    pass


if __name__ == '__main__':
    rafael = Homem(nome='Rafael', idade=10)
    julia = Homem(rafael, nome='Julia')
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
    Pessoa.olhos = 3
    novaPessoa = Pessoa(nome="pessoa", olhos=1)
    print(novaPessoa.olhos)
    print(Pessoa.olhos)
    print(rafael.olhos)
    print(Pessoa.nome_e_atributo_da_classe(), novaPessoa.nome_e_atributo_da_classe(), novaPessoa.olhos)
    print(Pessoa.metodo_estatico())
    print(isinstance(rafael, Homem))
    print(isinstance(rafael, Pessoa))
    print(isinstance(julia, Homem))
    print(isinstance(julia, Pessoa))
