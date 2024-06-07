# 1 criando uma classe em python
class Restaurante:
    nome=''
    categoria=''
    ativo=False

restaurante_praca=Restaurante()
# questão 2/5
restaurante_praca.nome='Bistrô'

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
