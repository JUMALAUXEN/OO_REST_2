
#atividade 1
# class Pessoa:
#     def __init__(self,nome, idade,profissao):
#         self.nome=nome
#         self.idade=idade
#         self.profissao=profissao
   
#     def __str__(self):
#         return f"Nome: {self.nome}, Idade: {self.idade}, Profissão: {self.profissao}"

#     def aniversario(self):
#         self.idade += 1

#     @property
#     def saudacao(self):
#         return f"Saudação, me chamo {self.nome}, e trabalho como {self.profissao}."
   
# pessoa1 = Pessoa("Jhulya", 22+1, "Médica")
# print(pessoa1)              
# pessoa1.aniversario()        
# print(pessoa1.saudacao)    


#atividade 2
class ContaBancaria:
    def __init__(self,titular,saldo,ativo,profissao,idade):
        self.titular=titular
        self.saldo=saldo
        self.ativo=False
        self.profissao=profissao
        self.idade=idade
#atividade 3
    def __str__(self):
        return f'{self.titular} | {self.saldo} | {self.ativo} | {self.profissao} | {self.idade}'
#atividade 4  
    @classmethod
    def ativar_conta(self):
        self.ativo=True

conta_titular=ContaBancaria('Murilo','R$700.000',True,'Empresario',10)
conta_titular.ativar_conta()
print(conta_titular)

#atividade 5
conta2 =ContaBancaria('Maria', 100000)
print(conta2.conta_titular)