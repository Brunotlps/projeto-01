from Models import *
from DAO import *
from datetime import datetime

class ControllerCategoria:

    def cadastrar_categoria(self, nova_categoria):
        existe = False
        lista_categorias = DaoCategoria.ler()

        for i in lista_categorias:
            if i.categoria == nova_categoria:
               existe = True
        if not existe:
            DaoCategoria.salvar(nova_categoria)
            print('Categoria salva com sucesso!') 
        else:
            print('Categoria já existente.')

    def remover_categoria(self, categoria_selecionada):
        
        lista_categorias = DaoCategoria.ler()
        cat = list(filter(lambda x: x.categoria == categoria_selecionada, lista_categorias))

        if len(cat) <= 0:
            print('Categoria inexistente.')

        else:
            for i in range(len(lista_categorias)):
                if lista_categorias[i].categoria == categoria_selecionada:
                    del lista_categorias[i]
                    break

            print('Categoria removida com sucesso!')

            with open('categorias.txt', 'w') as arq:
                for i in lista_categorias:
                    arq.writelines(i.categoria)
                    arq.writelines('\n')
#        TODO: Colocar 'sem categoria' no estoque
    def alterar_categoria(self, categoria_existente, nova_categoria):

        lista_categorias = DaoCategoria.ler()
        cat = list(filter(lambda x: x.categoria == categoria_existente, lista_categorias))


        if len(cat) > 0:
            
            cat1 = list(filter(lambda x: x.categoria == nova_categoria, lista_categorias))
            
            if len(cat1) == 0:
                lista_categorias = list(map(lambda x: Categoria(nova_categoria) if (x.categoria == categoria_existente) else(x), lista_categorias))
                print('Alteração concluída!')
            else:
                print('A categoria que você deseja cadastrar já existe no sistema.')
        
        else:
            print('A categoria que você deseja remover não existe no sistema.')
        
        with open('categorias.txt', 'w') as arq:
            for i in lista_categorias:
                arq.writelines(i.categoria)
                arq.writelines('\n')
#        TODO: alterar categoria no estoque
    def mostrar_categorias(self):
        
        categorias = DaoCategoria.ler()

        if len(categorias) == 0:
            print('Categoria vazia.')
        else:
            sum = 1
            for categoria in categorias:
                print(f'{sum}. {categoria.categoria}')
                sum+=1

class ControllerEstoque:

    def cadastrar_produto(self, nome, preco, categoria, quantidade):

        lista_categoria, lista_estoque = DaoCategoria.ler(), DaoEstoque.ler()

        categoria_filter = list(filter(lambda x: x.categoria == categoria, lista_categoria))
        nome_filter = list(filter(lambda x: x.produto.nome == nome, lista_estoque))

        if len(categoria_filter) > 0:
            if len(nome_filter) == 0:
                produto = Produtos(nome, preco, categoria)
                DaoEstoque.salvar(produto, quantidade)
                print('Produto cadastrado com sucesso')
            else:
                print("Produto já existe no estoque.")
        else:
            print('Categoria inexistente')

    def remover_produto(self, nome):
        
        lista_estoque = DaoEstoque.ler()
        estoque_filter = list(filter(lambda x: x.produto.nome == nome, lista_estoque))
        
        if len(estoque_filter) > 0:
            
            for i in range(len(lista_estoque)):
                
                if lista_estoque[i].produto.nome  == nome:
                    del lista_estoque[i]
                    print('Produto removido com sucesso!')
                    break
        else:
            print('Produto não cadastrado.')

        with open('estoque.txt', 'w') as arq:

            for i in lista_estoque:
                arq.writelines(i.produto.nome + '|' + i.produto.preco + '|' + i.produto.categoria 
                               + '|' + str(i.produto.quantidade))
                arq.writelines('\n')

    def alterar_produto(self, nome_atual, novo_nome, novo_preco, nova_categoria, nova_quantidade):
        lista_estoque, lista_categoria = DaoEstoque.ler(), DaoCategoria.ler()

        h = list(filter(lambda x: x.categoria == nova_categoria, lista_categoria))
        
        if len(h) > 0:
            est = list(filter(lambda x: x.produto.nome == nome_atual, lista_estoque))
            
            if len(est) > 0:
                
                est = list(filter(lambda x: x.produto.nome == novo_nome, lista_estoque))
                
                if len(est) == 0:
                    
                    lista_estoque = list(map(lambda x: Estoque(Produtos(novo_nome, novo_preco, nova_categoria), nova_quantidade) 
                                             if (x.produto.nome == nome_atual) else (x), lista_estoque))
                    print('Produto alterado com sucesso!')
                
                else:
                    print('Produto já cadastrado')
            else:
                print('Produto não cadastrado.')

            with open('estoque.txt', 'w') as arq:
                for i in lista_estoque:
                    arq.writelines(i.produto.nome + '|' + i.produto.preco + '|' + i.produto.categoria 
                                + '|' + str(i.quantidade))
                    arq.writelines('\n')
        else:
            print('Categoria não cadastrada.')

    def mostrar_estoque(self):
        lista_estoque = DaoEstoque.ler()
        if len(lista_estoque) == 0:
            print('Estoque vazio')
        else:
            print("===========Estoque===========")
            for i in lista_estoque:
                
                print(
                    f'Nome: {i.produto.nome}\nPreço: {i.produto.preco}R$\nCategoria: {i.produto.categoria}\nQuantidade: {i.quantidade}'
                    
                )
                print("======================")

class ControllerVenda:
    
    def cadastrar_venda(self, nome_produto, vendedor, comprador, quantidade_vendida):
        lista_estoque = DaoEstoque.ler()
        temp = []

        existe = False
        quantidade = False

        for i in lista_estoque:

            if existe == False:
                if i.produto.nome == nome_produto:
                    existe = True
                    if i.quantidade >= quantidade_vendida:
                        quantidade = True
                        i.quantidade = int(i.quantidade) - int(quantidade_vendida)
                        
                        vendido = Venda(Produtos(i.produto.nome, i.produto.preco, i.produto.categoria), vendedor, comprador, quantidade_vendida)

                        valor_compra = int(quantidade_vendida) * int(i.produto.preco)

                        DaoVenda.salvar(vendido)
                temp.append([Produtos(i.produto.nome, i.produto.preco, i.produto.categoria), i.quantidade])

                arq = open('estoque.txt', 'w')
                arq.write('')

                for i in temp:
                    with open('estoque.txt', 'a') as arq:
                        arq.writelines(i[0].nome + ' | ' + i[0].preco + ' | ' + i[0].categoria + ' | ' + str(i[1]))
                        arq.writelines('\n')
                
                if existe == False:
                    print('Produto não existe')
                    return None
                elif not quantidade:
                    print('Quantidade ultrapassada')
                else:
                    return valor_compra







# a = ControllerCategoria()
# # a.cadastrar_categoria('frios')
# # a.remover_categoria('frios')
# # a.cadastrar_categoria('frutas')
# # a.alterar_categoria('frios', 'carnes')
# a.mostrar_categorias()


# b = ControllerEstoque()
# b.cadastrar_produto('banana', '5', 'frutas', 10)
# b.alterar_produto('banana', 'maça', '6', 'frutas', 11)
# b.mostrar_estoque()

c = ControllerVenda()
c.cadastrar_venda('maça', 'joao', 'lucas', 1)