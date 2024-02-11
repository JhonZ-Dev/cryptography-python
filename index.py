from cryptography.fernet import Fernet

def generar_clave():
    """
    Genera una clave para la encriptación.
    """
    return Fernet.generate_key()