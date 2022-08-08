# výpočet faktoriálu

# načtení čísla ze vstupu a kontrola
x=int(input("zadej číslo pro výpočet: "))
if x<0:
    print("chybné čísli musí být větší 0")
elif x==0:
    print("faktoriál 0! je 1")    
else:
    f=1
    for i in range(1,x+1):
        f=f*i
    print(" faktorial ",x, "! je ", f)
#endif
