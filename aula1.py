
produtos = ["Arroz", "Feijão", "Macarrão", "Açúcar", "Sal"]
preços = [5.50, 4.20, 3.80, 2.50, 1.20]
quantidades = [10, 20, 15, 25, 30]


def imprimir_produto(index):
    if 0 <= index < len(produtos):
        print(f"Produto: {produtos[index]}")
        print(f"Preço: R$ {preços[index]:.2f}")
        print(f"Quantidade: {quantidades[index]}")
    else:
        print("Índice inválido!")


def retirar_produto(index):
    if 0 <= index < len(produtos):
        produto_removido = produtos.pop(index)
        preços.pop(index)
        quantidades.pop(index)
        print(f"Produto '{produto_removido}' removido com sucesso!")
    else:
        print("Índice inválido!")

# Exemplo de uso das funções
imprimir_produto(2)  
retirar_produto(3)   
imprimir_produto(3)  


imprimir_produto(1)