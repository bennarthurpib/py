nota_1 = float(input("Digite a primeira nota do aluno : "))
nota_2 = float(input("Digite a segunda nota do aluno: "))
media = (nota_1 + nota_2)/2
if media > 6:
	print("aluno aprovado")
elif media <= 6 and media >= 4 : 
	print("aluno em recuperação")
else:
	print("aluno reprovado")		
