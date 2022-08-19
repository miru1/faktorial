from math import pi
cislo=input('zadej poloměr kruhu: ').replace(",",".")
r=float(cislo)
obvod = 2 * pi *r
obsah = pi * r *r
print(f'obvod kruhu je {obvod} cm')
print(f'jeho obsah je {obsah} cm2')
