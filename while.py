email = "email"
senha = "admin"
leitura = " "
while(leitura != email):
    leitura = input("Digite seu email:")
    if email == leitura:
        print("Vamos checkar sua senha")
    else:
        print("Email incorreto, tente novamente")


while(leitura != senha):
    leitura = input("Digite a sua senha:")
    if senha == leitura:
        print("Acesso liberado")
    else:
        print("senha incorreta, tente novamente")
