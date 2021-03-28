import pyfiglet
import random
import time

def two():
    while True:
        global combinacoes
        a = random.choice(letras)
        b = random.choice(letras)
        password = a+b
        print(password)
        combinacoes +=1
        if password == senha:
            print("Senha encontrada")
            print("foram feitas {} combinações".format(combinacoes))
            break
def three():
    while True:
        global combinacoes
        a = random.choice(letras)
        b = random.choice(letras)
        c = random.choice(letras)
        password = a+b+c
        print(password)
        combinacoes +=1
        if password == senha:
            print("Senha encontrada")
            print("foram feitas {} combinações".format(combinacoes))
            break

def for1():
    while True:
        global combinacoes
        a = random.choice(letras)
        b = random.choice(letras)
        c = random.choice(letras)
        d = random.choice(letras)
        password = a+b+c+d
        print(password)
        combinacoes +=1
        if password == senha:
            print("Senha encontrada")
            print("foram feitas {} combinações".format(combinacoes))
            break

def five():
    while True:
        global combinacoes
        a = random.choice(letras)
        b = random.choice(letras)
        c = random.choice(letras)
        d = random.choice(letras)
        e = random.choice(letras)
        password = a+b+c+d+e
        print(password)
        combinacoes +=1
        if password == senha:
            print("Senha encontrada")
            print("foram feitas {} combinações".format(combinacoes))
            break

def six():
    while True:
        global combinacoes
        a = random.choice(letras)
        b = random.choice(letras)
        c = random.choice(letras)
        d = random.choice(letras)
        e = random.choice(letras)
        f = random.choice(letras)
        password = a+b+c+d+e+f
        print(password)
        combinacoes +=1
        if password == senha:
            print("Senha encontrada")
            print("foram feitas {} combinações".format(combinacoes))
            break
def seven():
    while True:
        global combinacoes
        a = random.choice(letras)
        b = random.choice(letras)
        c = random.choice(letras)
        d = random.choice(letras)
        e = random.choice(letras)
        f = random.choice(letras)
        g = random.choice(letras)
        password = a+b+c+d+e+f+g
        print(password)
        combinacoes +=1
        if password == senha:
            print("Senha encontrada")
            print("foram feitas {} combinações".format(combinacoes))
            break

def eigth():
    while True:
        global combinacoes
        a = random.choice(letras)
        b = random.choice(letras)
        c = random.choice(letras)
        d = random.choice(letras)
        e = random.choice(letras)
        f = random.choice(letras)
        g = random.choice(letras)
        h = random.choice(letras)
        password = a+b+c+d+e+f+g+h
        print(password)
        combinacoes +=1
        if password == senha:
            print("Senha encontrada")
            print("foram feitas {} combinações".format(combinacoes))
            break

def nine():
    while True:
        global combinacoes
        a = random.choice(letras)
        b = random.choice(letras)
        c = random.choice(letras)
        d = random.choice(letras)
        e = random.choice(letras)
        f = random.choice(letras)
        g = random.choice(letras)
        h = random.choice(letras)
        i = random.choice(letras)
        password = a+b+c+d+e+f+g+h+i
        print(password)
        combinacoes +=1
        if password == senha:
            print("Senha encontrada")
            print("foram feitas {} combinações".format(combinacoes))
            break

def teen():
    while True:
        global combinacoes
        a = random.choice(letras)
        b = random.choice(letras)
        c = random.choice(letras)
        d = random.choice(letras)
        e = random.choice(letras)
        f = random.choice(letras)
        g = random.choice(letras)
        h = random.choice(letras)
        i = random.choice(letras)
        j = random.choice(letras)
        password = a+b+c+d+e+f+g+h+i+j
        print(password)
        combinacoes +=1
        if password == senha:
            print("Senha encontrada")
            print("foram feitas {} combinações".format(combinacoes))
            break
        

        

bt = pyfiglet.figlet_format("Brute Force")
print("\033[1;32m"+bt)

letras= ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

numeros = [1,2,3,4,5,6,7,8,9,0]

combinacoes = 0

n = int(input("Quantidade de caracteres Minimo:2 Maximo:10 >>"))
senha = str(input(">>"))



if n == 2:
    two()
if n == 3:
    three()
if n == 4:
    for1()
if n == 5:
    five()
if n == 6:
    six()
if n == 7:
    seven()
if n == 8:
    eigth()
if n == 9:
    nine()
if n == 10:
    teen()
