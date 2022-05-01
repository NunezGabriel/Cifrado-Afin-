
# *Implementar el Cifrado Afın dentro del anillo Z27. Colocar un enlace a su repositorio
# en GitHub. El repositorio debe contener un README.md con una breve descripcion del
# programa y las instrucciones para su ejecucion.
#   .Utilizando la clave {a, b} = {4, 7}:
#    – Cifrar ELEMENTALMIQUERIDOWATSON
#    – Descifrar OKHFSNKFNWFCWJHSNCHQYWFSWF

# *El siguiente mensaje SLBCMVRBSHZBT~NSRQVVMSZBVH~NBVRQVLALHZBT~NSRQVWQAXLZW~NAQFQV
#  fue encriptado utilizando el Cifrado Afın dentro del anillo Z 27. Implemente un programa
#  que le permita descifrar el mensaje. El programa debe estar adjunto en el mismo repositorio del Cifrado Afın. 

def Alg_euclidesExt(a, b): 
    if b == 0:
        return (a, 1, 0)
    else:
        (d, dx, dy) = Alg_euclidesExt(b, a % b)
        (x, y) = (dy, dx - a//b * dy)
        return (d, x, y)

def inverso_M(a, n):
    (mcd, x, y) = Alg_euclidesExt(a, n)
    if mcd == 1:
        return x % n
    return None

abecedario = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

def cifrar(mensaje1, clave):
    if not inverso_M(clave[0], 27):
        return None
    mensaje2 = ""
    for letra in mensaje1:
        indice = (clave[0] * abecedario.find(letra) + clave[1]) % 27
        mensaje2 += abecedario[indice]
    return mensaje2

def descifrar(mensaje1, clave):
    inverso = inverso_M(clave[0], 27)
    if not inverso:
        return None
    mensaje2 = ""    
    for letra in mensaje1:
        indice = (inverso * (abecedario.find(letra) - clave[1])) % 27
        mensaje2 += abecedario[indice]
    return mensaje2

clave = [4, 7]

print("|_________________Por metodo Afin_____________________|")
print()
print("*****************************************************")
print("Cifrar ELEMENTALMIQUERIDOWATSON")
print("-RESPUESTA:")
print(cifrar("ELEMENTALMIQUERIDOWATSON", clave))
print("*****************************************************")

print("Descifrar OKHFSNKFNWFCWJHSNCHQYWFSWF")
print("-RESPUESTA:")
print(descifrar("OKHFSNKFNWFCWJHSNCHQYWFSWF", clave))
print("*****************************************************")

print("Descifrar SLBCMVRBSHZBTÑSRQVVMSZBVHÑBVRQVLALHZBTÑSRQVWQAXLZWÑAQFQV:")
print("-RESPUESTA:")
print(descifrar("SLBCMVRBSHZBTÑSRQVVMSZBVHÑBVRQVLALHZBTÑSRQVWQAXLZWÑAQFQV", [23, 17]))
