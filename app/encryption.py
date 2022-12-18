# Here is an example of how you might implement AES-256 bit encryption to save login credentials in Python using the cryptography library:

# Import the necessary libraries
import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

from dotenv import load_dotenv

load_dotenv()

SALT = os.getenv('SECRET_KEY').encode()


def encrypt_credential(password: str, master_password: str) -> str:

    # convert password to byte
    password = password.encode('utf-8')
    encrypt_key = generate_key(master_password, salt=SALT)

    # Use the key to encrypt the password
    fernet = Fernet(encrypt_key)
    encrypted_password = fernet.encrypt(password)

    return encrypted_password


def generate_key(master_password: str, salt: bytes) -> bytes:

    # convert to byte
    master_password = master_password.encode('utf-8')

    # Use the PBKDF2 algorithm to generate a key from the password and salt
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000
    )
    key = base64.urlsafe_b64encode(kdf.derive(master_password))

    return key
  
def decrypt_credential(password: str, master_password: str) -> str:
    # convert password to byte
    # password = password.decode('utf-8')
    encrypt_key = generate_key(master_password, salt=SALT)

    # Use the key to encrypt the password
    fernet = Fernet(encrypt_key)
    decrypted_password = fernet.decrypt(password)

    return decrypted_password

