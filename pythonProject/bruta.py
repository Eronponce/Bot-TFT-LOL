
import keyboard
import mouse
import pyautogui as pg
import textract
coordinates = None

ativo = True
Loop = True
pg.PAUSE = 0.1
def comp():
    print("Inicio")

    for i in range(2):
        print("Final")
        coordinates = pg.locateOnScreen('Malphite.png', region=regiao)
        print(regiao)
        print(coordinates)
        if(coordinates != None):
            pg.moveTo(coordinates[0], coordinates[1],_pause=False)
            print("malph")
            mouse.click()

        coordinates = pg.locateOnScreen('Skarner.png', region=regiao)
        if (coordinates != None):
            pg.moveTo(coordinates[0], coordinates[1],_pause=False)
            mouse.click()


        coordinates = pg.locateOnScreen('Jax.png', region=regiao)
        if(coordinates != None):
            pg.moveTo(coordinates[0], coordinates[1],_pause=False)
            mouse.click()


        coordinates = pg.locateOnScreen('Syfen.png', region=regiao)
        if(coordinates != None):
            pg.moveTo(coordinates[0] , coordinates[1],_pause=False)
            mouse.click()


        coordinates = pg.locateOnScreen('Olaf.png', region=regiao)
        if(coordinates != None):
            pg.moveTo(coordinates[0], coordinates[1],_pause=False)
            mouse.click()

        coordinates = pg.locateOnScreen('Sylas.png', region=regiao)
        print(regiao)
        print(coordinates)
        if (coordinates != None):
            pg.moveTo(coordinates[0], coordinates[1],_pause=False)
            mouse.click()

def compra():
    comp()
    pg.moveTo(comprareal,_pause=False)
    print("feito")
    mouse.click()


# def dinheiro():
#  image   print(textract.process("screenshot.png"))


def definirRegiao1():
    comeco = []
    while True:
        if keyboard.is_pressed("q"):
            comeco = pg.position()
            print("Feito 1")
            break
    return comeco
def definirRegiao2():
    final = []
    while True:
        if keyboard.is_pressed("w"):
            final = pg.position()
            print("Feito 2")
            break

    return final
def definirCompra():
    compra= []
    while True:
        if keyboard.is_pressed("e"):
            compra = pg.position()
            print("Feito 3")
            break
    return compra

#Defini a regiao que irá interagir
comecoreal = definirRegiao1()
finalreal = definirRegiao2()
comprareal = definirCompra()
regiao = (comecoreal[0],comecoreal[1], finalreal[0] - comecoreal[0] , finalreal[1] -comecoreal[1])
print(regiao)
while True:
    if(keyboard.read_key() == 'y'):
        compra()
    if(keyboard.read_key() == 'i'):
        print("ta aq")
        break
    if (keyboard.read_key() == 'p'):
        dinheiro()
