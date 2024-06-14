
#questão 1
class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

    def __str__(self):
        return f"Carro: {self.modelo}, Cor: {self.cor}, Ano: {self.ano}"

carro_1 = Carro('Bmw', 'Vermelha', 2000)
print(carro_1)

#questão 2
class Restaurante:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        self.menu = None
        self.mesas = 0

#questão 4
    def __str__(self):
        return f"Restaurante: {self.nome}, Categoria: {self.categoria}, Ativo: {self.ativo}, Menu: {self.menu}, Mesas: {self.mesas}"
    
#questão 3
restaurante1 = Restaurante('Burguer King', 'Lanches')
restaurante1.endereco = 'R. Paulo Bianco, 515'
restaurante1.capacidade = 50
print(restaurante1)
#construtor
restaurante2 = Restaurante('Petit Poa', 'Sorveteria')
print(restaurante2)

#questão 5
class Cliente:
    def __init__(self, nome, email, telefone, endereco):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.endereco = endereco

    def __str__(self):
        return f"Cliente: {self.nome}, Email: {self.email}, Telefone: {self.telefone}, Endereço: {self.endereco}"

cliente1 = Cliente('Ana Luiza', 'anaLuiza@hotmail.com', '8888-3333', 'Rua 5, 843')
cliente2 = Cliente('Pedro Brecher', 'pedroBrecher@hotmail.com', '9999-1111', 'Rua 9, 470')
cliente3 = Cliente('Eduarda Baltazar', 'eduardaBaltazar@hotmail.com', '777-6666', 'Rua 1, 392')

print(cliente1)
print(cliente2)
print(cliente3)