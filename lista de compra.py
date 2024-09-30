from os import system 
listadecompra =[]
while True:

 lista=int (input("0-sair 1-adicionar  2-remover  3-mostrar "))

 if lista == 0:
  break
 if lista == 1:
  x=str(input("digite oq quer "))
  listadecompra.append(x)
  print(f"{x}")
 
 if lista ==2:
  y=int(input("voce deseja remover qual item : digite o local onde ele esta "))
  listadecompra.pop(y)
  print(f"{y}")
 if lista ==3:
   print(f"aki esta sua lista {listadecompra} ")


