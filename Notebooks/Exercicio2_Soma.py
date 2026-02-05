# # Exercício 2: Criar uma função para comparar dois números.

# ==  verificar se é igual
# !=  verificar se é diferente
# >   verifica se é menor que
# <   verifica se é maior que

# A função recebe dois inteiros e imprime o maior número.
# Se ambos os números forem iguais, deve-se imprimir a frase “os números são iguais”.

numero_1 = input("Digite o primeiro número: ")
numero_2 = input("Digite o segundo número: ")

def comparacao(numero_1,numero_2):
  if numero_1 > numero_2:
    print("O primeiro numero é maior")
    return
  elif numero_1 < numero_2:
    print("O segundo numero é maior")
    return
  else:
    print("Os números são iguais")
    return
comparacao(numero_1, numero_2)