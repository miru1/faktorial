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
akce=10
if akce==0:  #  fibonacciho číslo
    f100 = fib2(100)    # zavoláme funkci fib2()
    print(f100)                # a vytiskneme její výsledek

elif akce==1:  # Proměnný počet parametrů
    PromennyPocetArg("První",1,54,"adam")

elif akce==2:  # lambda --------------------------------
    soucet=lambda a,b: a+b
    print(soucet(4,5))

elif akce==3:  #  řetezce
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

elif akce==5:  # -------------------------------------------
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
    
elif akce==6:  # doplnovaní   ------------------------------------ 
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

elif akce==7:  # funkce
    def napis_hlasku(nazev, skore):
        """Popíše skóre. Název má být přivlastňovací přídavné jméno."""

        print(nazev, 'skóre je', skore)
        if skore > 1000:
            print('Světový rekord!')
        elif skore > 100:
            print('Skvělé!')
        elif skore > 10:
            print('Ucházející.')
        elif skore > 1:
            print('Aspoň něco')
        else:
            print('Snad příště.')
            
    napis_hlasku("tvoje", 100 ) 

elif akce==8:  # funkce pro obsah obdélníka -----------
    def obsah(strana_A, strana_B):
        return strana_A * strana_B
    
    def oprav_vstup(par):
        # vraví float, ale naghradí čárku tečkou 
        ret=par.replace(',','.')
        ret=ret.replace(' ','')
        try:
            vysledek=float(ret)
        except:
            vysledek = 0    
        finally:
            return vysledek

    a=oprav_vstup(input("strana A: "))    
    b=oprav_vstup(input("strana B: "))
    print(f"obsah obdélníka o stranách {a} a {b} je ", obsah(a,b))

elif akce==9:
    from  math import pi
    def obsah_elipsy(a,b):
        return pi * a* b

    print('Obsah elipsy s poloosami 3 a 5 je', obsah_elipsy(3, 5), 'cm2')


elif akce==10:
    import sys
    print(sys.version)
    print(sys.argv)
    print(sys.exc_info())    
    print(sys.base_prefix)
    print(sys.path)
    cesty=str(sys.path)
    print(cesty.replace(',','\n'))