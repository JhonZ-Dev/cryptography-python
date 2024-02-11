from cryptography.fernet import Fernet

def generar_clave():
    """
    Genera una clave para la encriptación.
    """
    return Fernet.generate_key()
def encriptar_datos(datos, clave):
    """
    Encripta los datos utilizando una clave proporcionada.
    """
    cipher_suite = Fernet(clave)
    return cipher_suite.encrypt(datos.encode())
def desencriptar_datos(datos_encriptados, clave):
    """
    Desencripta los datos encriptados utilizando la clave.
    """
    cipher_suite = Fernet(clave)
    return cipher_suite.decrypt(datos_encriptados).decode()
# Ejemplo de uso
clave = generar_clave()
print("Clave de encriptación generada:", clave.decode())
