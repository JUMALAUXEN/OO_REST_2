
# Classe Carro
class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

    def __str__(self):
        return f"Carro: {self.modelo}, Cor: {self.cor}, Ano: {self.ano}"


# Criando uma instância da classe Carro
carro1 = Carro('Bmw', 'Vermelha', 2000)
print(carro1)


# Classe Restaurante
class Restaurante:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        self.endereco = None
        self.capacidade = 0

    def __str__(self):
        return f"Restaurante: {self.nome}, Categoria: {self.categoria}, Ativo: {self.ativo}, Endereço: {self.endereco}, Capacidade: {self.capacidade}"


# Criando uma instância da classe Restaurante e atribuindo valores aos seus atributos
restaurante1 = Restaurante('La Gourmet', 'Massas')
restaurante1.endereco = 'Rua Paulo Bianco, 328'
restaurante1.capacidade = 70
print(restaurante1)


# Criando uma instância da classe Restaurante utilizando o construtor
restaurante2 = Restaurante('La Bonele', 'Sorveteria')
print(restaurante2)


# Classe Cliente
class Cliente:
    def __init__(self, nome, email, telefone, endereco):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.endereco = endereco

    def __str__(self):
        return f"Cliente: {self.nome}, Email: {self.email}, Telefone: {self.telefone}, Endereço: {self.endereco}"


# Instanciando 3 objetos da classe Cliente e atribuindo valores aos seus atributos
cliente1 = Cliente('Eduarda Mouro', 'dudaMouro@hotmail.com', '1934-2671', 'Rua A, 117')
cliente2 = Cliente('Pedro Brecher', 'pedroBrecher@hotmail.com', '9761-4251', 'Rua B, 280')
cliente3 = Cliente('Ana Luia', 'anaLuiza@hotmail.com', '1572-3974', 'Rua C, 390')

print(cliente1)
print(cliente2)
print(cliente3)