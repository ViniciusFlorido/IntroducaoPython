# Exercício 1:

# Criar uma função para somar dois números.
# A função recebe dois inteiros e imprime o resultado da soma.
# Objetivo: aprender a criação e utilização de funções; tratamento de argumentos.

# SEMPRE DÁ PRA MELHORAR!

def soma_dois_numeros(x, y):
  if x.isdigit():
    if y.isdigit():
      return int(x) + int(y)
  return None # é uma variável nula

n1 = input("Digite o primeiro número: ")
n2 = input("Digite o segundo número: ")

total = soma_dois_numeros(n1, n2)

if total:
  print("O valor da soma é", total)
else:
  print("Digitou número errado, né???")