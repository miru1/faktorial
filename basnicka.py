def readFile():
    print('poslechni si básničku')
    print()

    i=0
    with open('basnicka.txt',encoding='UTF-8') as soubor:
        for radek in soubor:
            i+=1
            nrad=radek.replace("\n","")
            print(f'{i}: {nrad}')


    print('libilo se?')

def writeFile():
    with open('druha-basnicka.txt', mode='w', encoding='utf-8') as soubor:
        print('Naše staré hodiny', file=soubor)
        print('Bijí', 2+2, 'hodiny', file=soubor)

def grafika():
    import pyglet
    window = pyglet.window.Window()
    pyglet.app.run()
    print('Hotovo!')        

# writeFile()        
grafika()