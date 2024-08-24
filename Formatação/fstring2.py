nome = 'Felipe Ribeiro'
altura = 1.77
peso = 60
imc = peso / (altura * altura)

#fstring
string1 = f'{nome} tem {altura} de altura.'
print(string1)
#fstring junto da formatação de casas decimais   V
string2 = f'Pesa {peso}kg e seu IMC é {imc:.2f}.'
print(string2)