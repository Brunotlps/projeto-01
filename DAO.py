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

        for categoria in cls.categoria:
            cat.append(Categoria(categoria))
        
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
        cls.venda = list(map(lambda x: x.split(' | '), cls.categoria))

        vend = []
        for venda in cls.venda:
            vend.append(Venda(Produtos(venda[0], venda[1], venda[2]), venda[3], venda[4], venda[5], venda[6]))
        return vend
