#contador = 0 
#somador = 0 sem esses trechos o script não funcionará
while (contador < 5):
    contador = contador + 1
    valor = float(input("Digite o " + str(contador) + "° valor: "))
    somador = somador + valor
print("A soma é igual a " + str(somador))    
