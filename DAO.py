from Models import *

class DaoCategoria:
    
    @classmethod
    def salvar(cls, categoria):
        
        with open('categorias.txt', 'a') as arq:
            arq.writelines(categoria)
            arq.writelines('\n')
    
    @classmethod
    def ler(cls):
        
        with open('categorias.txt','r') as arq:
            cls.categoria = arq.readlines()
        
        cls.categoria = list(map(lambda x: x.replace('\n', ''), cls.categoria))
        
        cat = []

        for i in cls.categoria:
            cat.append(Categoria(i))
        
        return cat

class DaoVenda:

    @classmethod
    def salvar(cls, venda: Venda):
        
        with open('vendas.txt', 'a') as arq:
            arq.writelines(venda.itens_vendidos.nome + ' | ' +  venda.itens_vendidos.preco + ' | ' 
                           + venda.itens_vendidos.categoria + ' | ' + venda.vendedor + ' | ' + venda.comprador + 
                           ' | ' + str(venda.quantidade_vendida) + ' | ' + venda.data)
            arq.writelines('\n')
    
    @classmethod
    def ler(cls):
        
        with open('vendas.txt', 'r') as arq:
            cls.venda = arq.readlines()

        cls.venda = list(map(lambda x: x.replace('\n', ''), cls.categoria))
        cls.venda = list(map(lambda x: x.split('|'), cls.categoria))

        vend = []
        for venda in cls.venda:
            vend.append(Venda(Produtos(venda[0], venda[1], venda[2]), venda[3], venda[4], venda[5], venda[6]))
        return vend

class DaoEstoque:
    @classmethod
    def salvar(cls, produto: Produtos, quantidade):
        
        with open('estoque.txt', 'a') as arq:
            arq.writelines(produto.nome + '|' + produto.preco + '|' 
                           + produto.categoria + '|' + str(quantidade)) # type: ignore
            arq.writelines('\n')
    
    @classmethod
    def ler(cls):
        
        with open('estoque.txt', 'r') as arq:
            cls.estoque = arq.readlines()

        cls.estoque = list(map(lambda x: x.replace('\n', ''), cls.estoque))
        cls.estoque = list(map(lambda x: x.split('|'), cls.estoque))
        
        est = []
        if len(cls.estoque) > 0:
            for i in cls.estoque:
                est.append(Estoque(Produtos(i[0], i[1], i[2]), int(i[3])))
        return est
    
class DaoFornecedor:
    
    @classmethod
    def salvar(cls, fornecedor: Fornecedor):
        
        with open('fornecedores.txt', 'a') as arq:
            arq.writelines(fornecedor.nome + '|' + fornecedor.cnpj + '|' + fornecedor.telefone
                            + '|' + fornecedor.categoria_produtos)
            arq.writelines('\n')
    
    @classmethod
    def ler(cls):
        
        with open('fornecedores.txt', 'r') as arq:
            cls.fornecedores = arq.readlines()
        
        cls.fornecedores = list(map(lambda x: x.replace('\n', ''), cls.fornecedores))
        cls.fornecedores = list(map(lambda x: x.split('|'), cls.fornecedores))

        forn = []
        for i in cls.fornecedores:
            forn.append(Fornecedor(i[0], i[1], i[2], i[3]))

        return forn

class DaoPessoa:

    
    @classmethod
    def salvar(cls, pessoas: Pessoa):

        with open('pessoas.txt', 'a') as arq:
            arq.writelines(pessoas.nome + '|' + pessoas.telefone + '|' + pessoas.cpf + '|' 
                           + pessoas.email + '|' + pessoas.endereco)
            arq.writelines('\n')
    
    @classmethod
    def ler(cls):

        with open('pessoas.txt', 'r') as arq:
            cls.clientes = arq.readlines()

        cls.clientes = list(map(lambda x: x.replace('\n', ''), cls.clientes))
        cls.clientes = list(map(lambda x: x.split('|'), cls.clientes))

        clientes = []
        for cliente in cls.clientes:
            clientes.append(Pessoa(cliente[0], cliente[1], cliente[2], cliente[3], cliente[4]))
        
        return clientes
    
class DaoFuncionario:

    @classmethod
    def salvar(cls, funcionario: Funcionario):
        
        with open('funcionarios.txt', 'a') as arq:
            arq.writelines(funcionario.clt + '|' + funcionario.nome + '|' + funcionario.telefone
                           + '|' + funcionario.cpf + '|' + funcionario.email + '|' + funcionario.endereco)
            arq.writelines('\n')

    @classmethod
    def ler(cls):

        with open('funcionarios.txt', 'r') as arq:
            cls.funcionarios = arq.readlines()

        cls.funcionarios = list(map(lambda x: x.replace('\n', ''), cls.funcionarios))
        cls.funcionarios = list(map(lambda x: x.split('|'), cls.funcionarios))

        funcionario = []
        for i in cls.funcionarios:
            funcionario.append(Funcionario(i[0], i[1], i[2], i[3], i[4], i[5]))
        
        return funcionario