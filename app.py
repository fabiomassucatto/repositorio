from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida ('Suco de Laranja', 5.0, 'grande')
prato_paozinho= Prato('paozinho', 2.0, 'paozinho com manteiga')




def main():
   print(bebida_suco)
   print(prato_paozinho)

if __name__ == "__main__":
    main()