note_list = [7 , 7 , 8 , 10, 12, 6.8]
S = 0
for note in note_list:
    S = S + note # a cada repeticao a soma ira receber o total somado + o valor contido na lista
#encerra laço em 6.8
med = S/len(note_list)#o len() em list_notes ira contar a quantidade de termos e associa-la a formula da media
print("Média = " + str(med))
##S = 3 + 6 + 9 + ... + 333.

S = 0
for i in range(3 , 334 , 3):# iniciando em 3 n = os multiplos de 3 até 333
    S = S + i
#final do laco por identacao
print("S = " + str(S))
