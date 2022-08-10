def fib2(n): # vrátí Fibonacciho rozvoj do čísla n
     """Vrátí seznam obsahující Fibonacciho rozvoj do čísla n."""
     vysledek = []
     a, b = 0, 1
     while b < n:
         vysledek.append(b)    # viz níže
         a, b = b, a+b
     return vysledek

def PromennyPocetArg(par1, *viceArg):
#== proměnný počet argumentů ======================
    #    print(format % viceArg)
    i=1
    for arg in viceArg:
        print(i,arg)
        i+=1

#--------------------- start programu --------------------
akce=7
if akce==0:  #  fibonacciho číslo
    f100 = fib2(100)    # zavoláme funkci fib2()
    print(f100)                # a vytiskneme její výsledek

elif akce==1:  # Proměnný počet parametrů
    PromennyPocetArg("První",1,54,"adam")

elif akce==2:  # lambda --------------------------------
    soucet=lambda a,b: a+b
    print(soucet(4,5))

elif akce==3: #  řetezce
    print("C:\nahon")
    print("C:\\nahon")
    print("""toto je dlouhý text
přes více 
řádků""")
    print("1. řádek\n"+
    "druhý řádek"+'\n'
    "třetí řádek ----------")
    print("jiné fornmátování: 1. řádek\n"+
          "druhý řádek"+'\n'
          "třetí řádek")
elif akce==4:  # vestavěná funkce f
    print(f'{print}')
    print(len(f'{print}'))         

elif akce==5:    # -------------------------------------------
    retezec="čokoláda"
    print("řeteyec         :",retezec)  
    print("druhý znak      :",retezec[1])  # druhý znak
    print("první 4-ři znaky:",retezec[:4]) 
    print("od 5-tého dozadu:",retezec[5:]) 
    print("poslední 3 znaky:",retezec[len(retezec)-3:]) 
    print("první 3         :",retezec[:3]) 
    print("od 3 dál        :",retezec[3:]) 
    print("od druhého po 4 :",retezec[2:5])
    print("",retezec[0:len(retezec)])
    print("",retezec[0:999])
    print("obsahuje o      :", "o" in retezec)
    print("neobsahuje x    :", "x" not in retezec)
    print("na velká        :",retezec.upper())
    
elif akce==6: # doplnovaní   ------------------------------------ 
    sablona="""
Milý {jméno}    
Váš výsledek je {soucet}

S pozdravem {podpis} """
    jmeno="Adam"
    soucet=54
    podpis="Berta"
    hlaska=f'jméno={jmeno}'
    print(hlaska)
    print(sablona.format(jméno=jmeno,soucet=soucet,podpis="Helga") )