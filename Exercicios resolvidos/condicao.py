valor1 = input("Informe um valor:")
valor2 = input("Informe outro valor:")

if (valor1 > valor2):
    print(f"{valor1} é maior que {valor2}.")
elif (valor2>valor1):
    print(f"{valor2} é maior que {valor1}.")
elif (valor1==valor2):
    print("Valores iguais.")
else:
    print("Comando não reconhecido.")