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
        lista_estoque = DaoEstoque.ler()
        lista_categorias = DaoCategoria.ler()

        filtro_categorias = list(filter(lambda x: x.categoria == categoria, lista_categorias))
        filtro_nome = list(filter(lambda x: x.produto.nome == nome, lista_estoque))

        if len(filtro_categorias) > 0:
            if len(filtro_nome) == 0:
                produto = Produtos(nome, preco, categoria)
                DaoEstoque.salvar(produto, quantidade)
                print("Produto cadastrado com sucesso!")
        
            else:
                print("Produto já existente")
        
        else:
            print("Categoria inexistente.")







a = ControllerEstoque()
a.cadastrar_produto('musculo', '5', 'carnes', 10)

















# a = ControllerCategoria()
# # a.cadastrar_categoria('frios')
# # a.remover_categoria('frios')
# # a.cadastrar_categoria('frutas')
# # a.alterar_categoria('frios', 'carnes')
# a.mostrar_categorias()