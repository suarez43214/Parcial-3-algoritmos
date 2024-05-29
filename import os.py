import os

def contar_lineas(archivo):
   with open(archivo, 'r') as f:
       lineas = f.readlines()
   return len(lineas)

def contar_palabras(archivo):
   with open(archivo, 'r') as f:
       texto = f.read()
   palabras = texto.split()
   return len(palabras)
def contar_caracteres(archivo):
   with open(archivo, 'r') as f:
       texto = f.read()
   return len(texto)
def contar_palabra_especifica(archivo, palabra):
   with open(archivo, 'r') as f:
       texto = f.read()
   palabras = texto.split()
   return palabras.count(palabra)
def generar_informe(archivo_entrada, archivo_salida, palabra):
   lineas = contar_lineas(archivo_entrada)
   palabras = contar_palabras(archivo_entrada)
   caracteres = contar_caracteres(archivo_entrada)
   palabra_especifica = contar_palabra_especifica(archivo_entrada, palabra)
   with open(archivo_salida, 'w') as f:
       f.write(f"Lineas totales: {lineas}\n")
       f.write(f"Palabras totales: {palabras}\n")
       f.write(f"Caracteres totales: {caracteres}\n")
       f.write(f"Frecuencia de la palabra '{palabra}': {palabra_especifica}\n")
if __name__ == "__main__":
 
   archivo_entrada = "archivo.txt"  
   archivo_salida = "informe.txt"  
   palabra = "especial"  

   if not os.path.isfile(archivo_entrada):
       print(f"Error: El archivo '{archivo_entrada}' no existe.")

   else:
       generar_informe(archivo_entrada, archivo_salida, palabra)
       print(f"Informe generado en {archivo_salida}")
    