class Pessoa:
    def cumprimentar(self):
        return f'Olá ${id(self)}'


if __name__ == '__main__':
    pessoa = Pessoa()
    print(Pessoa.cumprimentar(pessoa))
    print(pessoa.cumprimentar())
