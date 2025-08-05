from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Ana', 5)
restaurante_praca.receber_avaliacao('Bia', 4)





def main():
    Restaurante.listar_restaurantes()


if __name__ == "__main__":
    main()