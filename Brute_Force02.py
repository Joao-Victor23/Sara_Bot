import pyfiglet
import os
import time

os.system("clear")

figlet = pyfiglet.figlet_format("Brute Force")
print(figlet)

print("Author    :  João Victor")


print("")
print("")

senha = input(">>")

print("[                    ] 0% ")
time.sleep(1)
print("[=====               ] 25%")
time.sleep(1)
print("[==========          ] 50%")
time.sleep(1)
print("[===============     ] 75%")
time.sleep(1)
print("[====================] 100%")
time.sleep(1)


letras = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","5","6","7","8","9"]

combinacoes = 0

for i1 in letras:
    for i2 in letras:
        for i3 in letras:
            for i4 in letras:
            	for i5 in letras:
            		for i6 in letras:
            			for i7 in letras:
            				for i8 in letras:
            					password = i1+i2+i3+i4+i5+i6+i7+i8
            					print(password)
            					if password == senha:
            						print("sua senha foi encontrada!")
            						exit()
