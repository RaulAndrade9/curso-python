#64 - Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
#  Um número primo é aquele que é divisível somente por ele mesmo e por 1.

numero = int(input("Informe um número "))
resultado = 0
primo = True
for i in range(2,numero):
    resultado = numero % i
    if resultado == 0:
        primo = False
        break;
    else:
        primo = True

if primo == True:
    print("O número é primo")
else: 
    print("O número não é primo")
    

    