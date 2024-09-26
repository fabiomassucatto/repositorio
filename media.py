import os 
import time
lista=[]
while True:
 opção=int(input("0-sair, 1-adicionar nota,2-mostrar media"))
 if opção == 0:
   print("Saindo...")
   break
 elif opção ==1:
   nota=int(input("me diga sua nota de 0 a 10 "))
   if 0 <= nota <= 10:
    lista.append(nota)
    
   else:
    print("sua nota é invalida")
    time.sleep(1)
    nota=int(input("me diga sua nota de 0 a 10 "))
     
   
 elif opção == 2:
     soma=sum(lista)/len(lista)
     print(f"sua media é {soma}")

  
 

