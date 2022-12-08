import random
import string
from flask import Blueprint

pgenerator = Blueprint('pgenerator', __name__)

from . import views

def pgen(length):
    #get a string of all characters
    char_seq = str(string.printable)
    password =''

    for len in range(length):
        random_char = random.choice(char_seq)
        password += random_char
            
        #reshuffle the list of chars in the generated password 
        passwordlist = list(password)
        random.shuffle(passwordlist)
        final_password = ''.join(passwordlist)
    return final_password