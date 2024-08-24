# PARAMETRO NOMEADO
a = 'a'
b = '2'
c = 3.2
d = 3.14444444444

var = 'A = {}, B = {}, C= {}, D= {:.3f}'
formato = var.format(a, b, c, d)
print(formato)


# OUTRA FORMA
e = 1
f = 2
g = 3
h = 4

var1 = 'Primeiro: {0}, Segundo: {1}, Terceiro: {2}, Quarto: {3}'
formato = var1.format(e, f, g, h)
print(formato)
# MUDANDO AS COORDENADAS /////////////////////////////////////////
var1 = 'Primeiro: {2}, Segundo: {1}, Terceiro: {3}, Quarto: {0}'
formato = var1.format(e, f, g, h)
print(formato)