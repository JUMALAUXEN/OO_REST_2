# 1 criando uma classe usando construtor

class Restaurante:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        
        def __STR__(self):
            #return self.nome
            return f'{self.nome}' | {self.categoria} | {self.ativo}

restaurante_praca = Restaurante()
# 2 criando uma instância da classe Restaurante com construtor
restaurante_praca = Restaurante ('Praça', 'Gourmet')

# questão 1
restaurante_praca.categoria='Italiana'
# questão 3
restaurante_praca.ativo="ativo" if restaurante_praca.ativo else "inativo"
print(f"O restaurante está {restaurante_praca}.")
# questão 9
print(f"Nome: {restaurante_praca.nome}, Categoria: {restaurante_praca.categoria}")

# questão 6
restaurante_pizza=Restaurante()
restaurante_pizza.nome='Pizza Place'
#questão 7
restaurante_pizza.categoria='Fast Food'
#questão 8
restaurante_pizza.ativo=True


# 3 consumindo os objetos criados
restaurantes=[restaurante_praca,restaurante_pizza]
# print(restaurantes)

print(dir(restaurante_praca))
print('')
print(vars(restaurante_praca))
print('')
print(restaurante_praca)