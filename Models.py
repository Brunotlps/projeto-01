from datetime import datetime


class Categoria:
    
    def __init__(self, categoria):
        self.categoria = categoria
    
class Produtos:
    
    def _init__(self, nome, preco, categoria):
        self.nome = nome
        self.preco = preco
        self.categoria = categoria

class Estoque:
    
    def __init__(self, produto: Produtos, quantidade: int):
        self.produto = produto
        self.quantidade = quantidade


class Venda:
    
    def __init__(self, itens_vendidos: Produtos, vendedor, comprador, quantidade_vendida: int, data = datetime.now().strftime("%d/%m/%Y")):
        self.itens_vendidos = itens_vendidos
        self.vendedor = vendedor
        self.comprador = comprador
        self.quantidade_vendida = quantidade_vendida
        self.data = data

class Fornecedor:
    
    def __init__(self, nome, cnpj, telefone, categoria_produtos):
        self.nome = nome
        self.cnpj = cnpj
        self.telefone = telefone
        self.categoria_produtos = categoria_produtos

class Pessoa:
    
    def __init__(self, nome, cpf, telefone, email, endereco):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.endereco = endereco

class Funcionario(Pessoa):
    
    def __init__(self, clt, nome, cpf, telefone, email, endereco):
        self.clt = clt
        super(Funcionario, self).__init__(nome, cpf, telefone, email, endereco)