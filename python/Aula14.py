a = 'A'
b = 'B'
c = 1.1
String = 'a= {nome1}, b= {nome2}, c= {nome3:.2f} '
formato = String.format(nome1=a, nome2=b, nome3=c)
# Cada chaves é para cada variavel no format
# Você pode colocar tbm numeros nas chaves para referenciar a ordem no format

print(formato)
