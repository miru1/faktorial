from math import pi
obsah = 0
a = 30

def obsah_elipsy(a, b):
  #  global obsah
    obsah = pi * a * b  # Přiřazení do `obsah`
    a = a + 3  # Přiřazení do `a`
    return obsah

def square(n):
    n *= n
    return n

print("obsah_elipsy: ",obsah_elipsy(a, 20))
print("obsah: ",obsah)
print(f"A: {a}")
x=4
x=square(x)
print("x=",x)
print("hello".capitalize().replace("l","j",1))