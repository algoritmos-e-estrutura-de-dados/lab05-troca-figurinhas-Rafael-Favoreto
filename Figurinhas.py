def trocaFigurinha(figurinhaDaniel, figurinhaFernandocossaneto):

  indice = 0
  qntd = 0

  if len(figurinhaDaniel) < len(figurinhaFernandocossaneto):
    for i in range(len(figurinhaDaniel)):
      for j in range(len(figurinhaFernandocossaneto)):
        if figurinhaDaniel[i] == figurinhaFernandocossaneto[j]:
          indice += 1
    qntd = len(figurinhaDaniel) - indice

  elif len(figurinhaFernandocossaneto) < len(figurinhaDaniel):
    for i in range(len(figurinhaFernandocossaneto)):
      for j in range(len(figurinhaDaniel)):
        if figurinhaFernandocossaneto[i] == figurinhaDaniel[j]:
          indice += 1
    qntd = len(figurinhaFernandocossaneto) - indice

  else:
    for i in range(len(figurinhaDaniel)):
      for j in range(len(figurinhaFernandocossaneto)):
        if figurinhaDaniel[i] == figurinhaFernandocossaneto[j]:
          indice += 1
    qntd = len(figurinhaDaniel) - indice

  return qntd