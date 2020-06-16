def morral(tamano_moral, pesos, valores, n):
  if n == 0 or tamano_moral == 0:
    return 0
  print(f"    Indice:{n} | Morral: {tamano_moral} --> peso: {pesos[n - 1]} -- valor: {valores[n - 1]} :: {pesos}")
  if pesos[n - 1] > tamano_moral:
    return morral(tamano_moral, pesos, valores, n - 1)
  maxValue = max(valores[n - 1] + morral(tamano_moral - pesos[n - 1], pesos, valores, n-1),
    morral(tamano_moral, pesos, valores, n-1))
  return maxValue

if __name__ == '__main__':
  pesos = [12, 2, 1, 4, 1]
  valores = [4, 2, 1, 10, 2]
  tamano_morral = 15
  n = len(valores)

  result = morral(tamano_morral, pesos, valores, n)
  print(result)