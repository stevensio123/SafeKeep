from flask_login import login_required
from flask import Blueprint, flash ,redirect, render_template, request, url_for
from . import pgenerator
import random
import string

@pgenerator.route('/pgenerator', methods=['GET', 'POST'])
def pgenerate():
    
    #default value of Filters
    asciiFilter = False
    lowerFilter = False
    upperFilter = False
    puncFilter = False
    digitsFilter = False
    
    if request.method == "POST":
        
        if not request.form.get("asciiF"):
            asciiFilter = True
        if not request.form.get("lowerF"):
            lowerFilter = True
        if not request.form.get("upperF"):
            upperFilter = True
        if not request.form.get("puncF"):
            puncFilter = True
        if not request.form.get("digitsF"):
            digitsFilter = True
            
        length = int(request.form.get("length"))
        
        if length >= 8 and length <= 40:
            password = pgen(length,asciiFilter,lowerFilter,upperFilter,puncFilter,digitsFilter)
            
            return render_template('pgenerator.html',password=password)

    
    password = pgen(int(13),asciiFilter,lowerFilter,upperFilter,puncFilter,digitsFilter)
    return render_template('pgenerator.html',password=password)  #set 13 as the default length of generated password



def pgen(length,asciiFilter,lowerFilter,upperFilter,puncFilter,digitsFilter):
 
    password =''
    #All usable characters
    chars = string.ascii_letters + string.hexdigits + string.punctuation
    #Add selected filters into the filter list:
    filter = ''
    if asciiFilter == True:
        filter += string.ascii_letters
    if lowerFilter == True:
        filter += string.ascii_lowercase
    if upperFilter == True:
        filter += string.ascii_uppercase
    if puncFilter == True:
        filter += string.punctuation
    if digitsFilter == True:
        filter += string.digits
    
    
    #maketrans to create a mapping for removing the filtered characters inside chars
    filters = chars.maketrans('', '', filter)
    #translate to use the mapping
    char_seq = chars.translate(filters)
    
    
    #create random chars for the selected length
    for len in range(int(length)):
        random_char = random.choice(char_seq)
        password += random_char
            
        #reshuffle the list of chars in the generated password 
        passwordlist = list(password)
        random.shuffle(passwordlist)
        final_password = ''.join(passwordlist)
    return final_password