import random

soucet=0
volba="A"

while  volba=="A":
    karta=random.randint(1,10)
    soucet=soucet+karta
    Aprint("vytáhl jsi si kartu=",karta, " součet máš = ",soucet)
 
    if soucet==21:
        print("vyhlrál's!")
        volba="N"
    elif soucet>21:
        print("přetáhl jsi hombré")    
        volba="N"
    else:
        volba=input("ještě kartu [A/N]: ")    

