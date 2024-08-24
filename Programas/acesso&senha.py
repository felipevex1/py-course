entrada = input("Digite [E]ntrar ou [S]air: ")
senha_liberada = '123'
if entrada == 'E' or entrada == 'e':
    senha = input("Senha: ")
    if senha == senha_liberada:
        print("Acesso liberado.")
    else:
        print("Acesso negado.")
else:
    print("Saiu.")



