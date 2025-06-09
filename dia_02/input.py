#57 - Faça um programa que peça 10 
# números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

impar = 0
par = 0
for i in range(0,10):
    num = int(input("Informe um número: "))
    if num % 2 == 0:
        par += 1
    else: impar += 1

print(f"Há {par} números pares e {impar} números ímpares") 
    