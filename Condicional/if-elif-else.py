# if / elif / else
# se / se nao se / se nao

entrada = input('Você quer "entrar" ou "sair"?')

if entrada == 'entrar':
    print('Entrou.')
elif entrada == 'sair':
    print('Saiu.')
else: # Necessariamente a ultima condição precisa ser else
    print('Comando não reconhecido.')