def sumar_con_manejo_errores(a, b):
  """
  Esta función suma dos números con manejo de errores.

  Parámetros:
    a: El primer número a sumar.
    b: El segundo número a sumar.

  Retorno:
    La suma de los dos números o None si hay un error.
  """
  try:
    a = float(a)
    b = float(b)
    return a + b
  except ValueError:
    print("Error: Los valores deben ser números.")
    return None

# Ejemplo de uso
resultado = sumar_con_manejo_errores(5, "hola")
if resultado is not None:
  print(f"La suma es: {resultado}")