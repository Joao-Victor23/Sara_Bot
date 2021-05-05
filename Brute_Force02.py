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
time.sleep(2)
print("[=====               ] 25%")
time.sleep(2)
print("[==========          ] 50%")
time.sleep(2)
print("[===============     ] 75%")
time.sleep(2)
print("[====================] 100%")
time.sleep(2)


letras = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",'ba','be','bi','bo','bu','ca','ce','ci','co','cu','da','de','di','do','du','fa','fe','fi','fo','fu','ga','ge','gi','go','gu','ha','he','hi','ho','ia','ie','io','iu','hu','ja','je','ji','jo','ju','ka','ke','ki','ko','ku','la','le','li','lo','lu','ma','me','mi','mo','mu','na','ne','ni','no','nu','pa','pe','pi','po','pu','qu','ra','re','ri','ro','ru','sa','se','si','so','su','ta','te','ti','to','tu','va','ve','vi','vo','vu','wa','we','wi','wo','wu','xa','xe','xi','xo','xu','za','ze','zi','zo','zu', 'cha','che','chi','cho','chu','lha', 'lhe', 'lhi','lho', 'lhu', 'nha','nhe','nhi','nho','nhu','rra','rre','rri','rro','rru','ssa','sse','ssi','sso','ssu','qua','que','qui','quo']

combinacoes = 0

for i2 in letras:
    for i3 in letras:
        for i4 in letras:
            for i5 in letras:
                password = i2+i3+i4+i5
                combinacoes +=1
                print(password)
print("Foram geradas cerca de {} senhas.".format(combinacoes))
