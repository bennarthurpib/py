#Encontrar soma S = 2+4+6+8+10+12+14+16+18
S = 0
for x in range(2 , 20 , 2):
    S = S + x
print("A soma da P.A é:" + str(S))

#Escrever os 5 primeiros termos da P.A  2N+1 (ímpares)
n = 0
for n in range(0 , 5 , 1):
    a = (2*n)+1
    print("O " + str(n) + "° termo dessa P.A é igual a: " + str(a))

    
