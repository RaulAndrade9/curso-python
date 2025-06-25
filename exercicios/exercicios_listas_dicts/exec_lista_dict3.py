"""
Cadastro de alunos e suas notas
Peça ao usuário para digitar o nome de 3 alunos e suas respectivas notas.
 Armazene os dados em um dicionário, onde o nome do aluno seja a chave e a nota o valor."""

info_alunos = {}

for i in range(0,3):
    nome = input("Informe o nome: ")
    nota = float(input("informe a nota: "))
    info_alunos[nome] = nota

print(info_alunos)