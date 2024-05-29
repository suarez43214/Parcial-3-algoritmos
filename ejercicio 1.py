import random
import string
 
def generar_clave(longitud=10):
    if longitud < 8:
        raise ValueError("La clave debe ser igual o mayor a 8 caracteres.")
    
    
    letras_mayusculas = string.ascii_uppercase
    letras_minusculas = string.ascii_lowercase
    digitos = string.digits
    caracteres_especiales = string.punctuation
    
    contraseña = [
        random.choice(letras_minusculas),
        random.choice(letras_mayusculas),
        random.choice(digitos),
        random.choice(caracteres_especiales)
    ]
    
    todos_los_caracteres = letras_mayusculas + letras_minusculas + digitos + caracteres_especiales
    contraseña += random.choices(todos_los_caracteres, k=longitud-4)
    
    random.shuffle(contraseña)
    
    contraseña = ''.join(contraseña)
    
    return contraseña
 
def guardar_contraseña(contraseña, archivo='contraseña.txt'):
    with open(archivo, 'w') as file:
        file.write(contraseña)
    print(f"Contraseña guardada en {archivo}")
 
if __name__ == "__main__":
    clave_generada = generar_clave(10)
    print(f"Contraseña generada: {clave_generada}")
    guardar_contraseña(clave_generada)