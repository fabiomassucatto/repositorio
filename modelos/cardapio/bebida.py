from modelos.cardapio.Item_Cardapio import Item_Cardapio
class Bebida:
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self._tamanho = tamanho

    def __str__(self):
        return self._nome