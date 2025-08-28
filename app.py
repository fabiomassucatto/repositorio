from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida ('Suco de Laranja', 5.0, 'grande')
prato_paozinho= Prato('paozinho', 2.0, 'paozinho com manteiga')
restaurante_praca.adicionar_item_cardapio(bebida_suco)
restaurante_praca.adicionar_item_cardapio(prato_paozinho)



def main():
 restaurante_praca.exibir_cardapio

if __name__ == "__main__":
   main()