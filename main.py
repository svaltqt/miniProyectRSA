from abc import ABC
from dataclasses import asdict
import math
from ntpath import join



def public_key(n,e):
    key = (n,e)
    return key

def private_key(fi,e):
    i = 2
    d = (i * fi + 1 )/e
    return d

def translate(text):
    ABC = (' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
             'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

    encoded = []
    for char in text:
        for i in ABC:
            if i == char:
                encoded.append(ABC.index(i))
    #encoded = "".join(map(str, encoded))
    return encoded

def validation_e(fi_n):
    e = int(input('choose a number between ' + ' 1 ' + ' y ' + str(fi_n) + ": "))

def crypted():
    pass

def decripyted():
    pass

def run():

    text = input("Type the secret phrase: ")
    text.lower()

    check_text = translate(text)
    
    #print(check_text)

    p = int(input('Digita el primer primo: '))
    q = int(input('Digita el segundo primo: '))
    n = p*q
    fi_n = (p-1) * (q-1)
    #e = int(input('choose a number between ' + ' 1 ' + ' y ' + str(fi_n) + ": "))
    e = validation_e(fi_n)
    #while e > 1 and e < fi_n:
     #   asd =  math.gcd(n,e)
      #  if asd == 1:

    pu_key = public_key(n,e)
    priv_key = private_key(fi_n,e)

    menu = """
    1. Crypted
    2. DeCrypted
    """

    opction = int(input(menu))

    #print('Clave publica es: ' + str(pu_key) + "\n La clave privada es: " + str(priv_key) + '\n FI es igual a:  ' + str(fi_n)+ '\n El valor de Euler es: ' + str(e) )

if __name__ == '__main__':
    run()