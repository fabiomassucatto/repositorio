while True:

 
 num1=int(input("me diga um valor"))
 
 num2=int(input("me diga um valor"))

 print("1-adição 2-sub 3-divisão 4-mult 0-sair")
 
 numer=int(input("ecolha uma opçao"))

 if numer == 0:
  break
 if numer==1:
  
  soma =num1+num2
  print(f"a soma dos numeros é {soma}")

 if numer==2:
   sub=num1-num2
   print(f"a subtração é {sub}")

 if numer==3:
    dive=num1/num2 
    print(f"a divsão é {dive}")

 if numer ==4:
    mult=num1*num2
    print(f"a mult é {mult}")
 

