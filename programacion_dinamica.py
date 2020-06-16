def fibonacci_recursive(n):
  if n < 2:
    return 1
  return fibonacci_recursive(n-1)+fibonacci_recursive(n-2)

def fibonacci_dinamico(n, memo = {}):
  if n < 2:
    return 1
  try:
    return memo[n]
  except KeyError:
    resultado = fibonacci_dinamico(n - 1) + fibonacci_dinamico(n - 2)
    memo[n] = resultado
    return resultado

if __name__ == "__main__":
  n = int(input("escoge un numero: "))
  print(fibonacci_dinamico(n))