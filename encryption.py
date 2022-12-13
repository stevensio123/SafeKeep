# Here is an example of how you might implement AES-256 bit encryption to save login credentials in Python using the cryptography library:
import app
# Import the necessary libraries
import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

from dotenv import load_dotenv

load_dotenv()

SALT = os.getenv('SECRET_KEY').encode()
print(app.config['development'].SECRET_KEY)
print(SALT)
# Generate a random salt
salt = Fernet.generate_key()

# Define the password to be encrypted
password = 'mysecretpassword'.encode('utf-8')

# Define the master password and the number of iterations to use
# for the key derivation function
master_password = b'pbkdf2:sha256:260000$I2juRBxKTf4XaW3J$b7bad70d601b1fcb7e992651d22d7db116c2aea7ab946c16df84db7bb6412fd1'
iterations = 100000

# Use PBKDF2HMAC to derive a key from the master password and salt
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=iterations
)
key = kdf.derive(master_password)
key = base64.urlsafe_b64encode(key)

# Use the key to encrypt the password
fernet = Fernet(key)
encrypted_password = fernet.encrypt(password)

# Store the encrypted password, salt, and iteration count in a database
# or other storage location

# To decrypt the password, retrieve the encrypted password, salt, and
# iteration count from the database and use them to derive the key
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=iterations
)
key = kdf.derive(master_password)

# Encode the key using URL-safe base64 encoding
key = base64.urlsafe_b64encode(key)

# Use the key to decrypt the password
fernet = Fernet(key)
decrypted_password = fernet.decrypt(encrypted_password)

# The decrypted password should match the original password
assert decrypted_password == password
# This code uses the PBKDF2HMAC key derivation function from the cryptography library to derive a
# key from the user's master password and a random salt. The password is then encrypted using this key and the Fernet symmetric encryption algorithm. The encrypted password, salt, and iteration count are stored in a database or other storage location. When the password is needed, the salt and iteration count are retrieved and used to derive the key, and the password is decrypted using the key.

# This is just an example of how AES-256 bit encryption could be used to save login credentials.
# There are many other ways to implement this, and the specific details may vary depending on your application. This code should not be considered a complete and secure solution.
# print(decrypted_password, ':', password)



def _encrypt(password: str, master_password: str) -> str:

    # convert password to byte
    password = password.encode('utf-8')
    encrypt_key = generate_key(master_password, salt=SALT)

    # Use the key to encrypt the password
    fernet = Fernet(encrypt_key)
    encrypted_password = fernet.encrypt(password)

    return encrypted_password


def generate_key(master_password: str, salt: bytes) -> bytes:

    # Use the PBKDF2 algorithm to generate a key from the password and salt
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000
    )
    key = base64.urlsafe_b64encode(kdf.derive(master_password))

    return key
  
def decrypt_password(password: str, master_password: str) -> str:
    # convert password to byte
    # password = password.decode('utf-8')
    encrypt_key = generate_key(master_password, salt=SALT)

    # Use the key to encrypt the password
    fernet = Fernet(encrypt_key)
    decrypted_password = fernet.decrypt(password)

    return decrypted_password

x = _encrypt('mysecretpassword', master_password)
print(x)
print(decrypt_password(x, master_password).decode())