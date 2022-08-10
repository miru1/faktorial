def is_num_Float(n):
    try:
        float (n)
    except ValueError:
        return "NO"    
    else:
        return "YES"     

def is_num_Int(n):
    try:
        int (n)
    except ValueError:
        return "NO"    
    else:
        return "YES"    
    

x=input("zadej číslo: ")
print("typ: ",type(x))
print("I=",isinstance(x,int),is_num_Int(x))
print("F=",isinstance(x,float),is_num_Float(x))
print("S=",isinstance(x,str))
print(len)


# testuj vstup na celé číslo
try:
    a=int(input("zadej dalčí číslo: "))
except ValueError:
    print("Chybné zadání!")    
else:
    print("výsledek=", a**2)    
finally:
    print("konec programu")    
