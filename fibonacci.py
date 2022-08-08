def fib2(n): # vrátí Fibonacciho rozvoj do čísla n
     """Vrátí seznam obsahující Fibonacciho rozvoj do čísla n."""
     vysledek = []
     a, b = 0, 1
     while b < n:
         vysledek.append(b)    # viz níže
         a, b = b, a+b
     return vysledek

def PromennyPocetArg(par1, *viceArg):
    #    print(format % viceArg)
    i=1
    for arg in viceArg:
        print(i,arg)
        i+=1

#--------------------- start programu --------------------
akce=2
if akce==0:
    f100 = fib2(100)    # zavoláme funkci fib2()
    print(f100)                # a vytiskneme její výsledek

elif akce==1:
    PromennyPocetArg("První",1,54,"adam")

elif akce==2:  # lambda
    soucet=lambda a,b: a+b
    print(soucet(4,5))
