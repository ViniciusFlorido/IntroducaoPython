def verificar_aprovacao(n1, n2):

  media = (n1 + n2) / 2
  if media >= 6.0:
    status = "Aprovado"
  else:
    status = "Reprovado"
  return media, status

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media_calculada, situacao_aluno = verificar_aprovacao(nota1, nota2)
print(f"A média do aluno é: {media_calculada:.1f}")
print(f"Situação: {situacao_aluno}")