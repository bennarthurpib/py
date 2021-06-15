x = float(input("Digite a nota de 'aluno_X': "))
y = float(input("Digite a nota de 'aluno_y': "))
z = float(input("Digite a nota de 'aluno_z': "))
f = float(input("Digite a nota de 'aluno_f': "))
g = float(input("Digite a nota de 'aluno_g': "))
n = 5 #len de alunos
#med = (x + y + z + f + g)/5
#print(med)
#notas_dicionario
dic = {"aluno_x" : x , "aluno_y " : y , "aluno_z" : z ,"aluno_f" : f, "aluno_g": g}
med = sum(dic.values())/n
print(med)
