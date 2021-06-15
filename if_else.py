import math
print(math.factorial(2))

from math import factorial
print(math.factorial(3))


import math
n = int(input("digite o coeficiente n: "))
k = int(input("digite o coeficiente k: "))
combin = math.comb(n , k)
print("o resultado dessa análise combinatória é: " , combin)

report_user = input("O resultado está correto? [Yes/not]")
if report_user == "Yes":
    print("Obrigado por escolher essa calculadore")
else :
    print("Reportar erro")
    erro = input("Em poucas palavras reporte o erro ocorrido:")
    deixar_email = input("Okay, tentaremos resolver o problema e entraremos em contato, gostaria de deixar um e-mail para contato?")

    if  deixar_email =="Yes":
        email = input("Digite seu email: ")
    else : 
        print("Obrigado por escolher essa calculadora!")
  
    
