from flask_login import login_required
from flask import Blueprint, flash ,redirect, render_template, request, url_for
from . import pgenerator
import random


@pgenerator.route('/pgenerator', methods=['GET', 'POST'])
def pgenerate(): 
    if request.method == "POST":
        length = int(request.form.get("length"))
        
        if length >= 8 and length <= 40:
            password = pgen(length)
            return render_template('pgenerator.html',password=password)
        
    
    return render_template('pgenerator.html',password=pgen(int(13)))  #set 13 as the default length of generated password



def pgen(length):
    #A string of all usable characters
    char_seq = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&'()-?@[]^_`~"
    password =''

    for len in range(int(length)):
        random_char = random.choice(char_seq)
        password += random_char
            
        #reshuffle the list of chars in the generated password 
        passwordlist = list(password)
        random.shuffle(passwordlist)
        final_password = ''.join(passwordlist)
    return final_password