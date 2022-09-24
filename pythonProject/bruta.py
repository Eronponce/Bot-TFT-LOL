
import keyboard
import mouse
import pyautogui as pg
import textract
coordinates = None
regiao = (500,950,1000,200)
ativo = True
Loop = True
pg.PAUSE = 0.1
def comp():
    for i in range(2):
        coordinates = pg.locateOnScreen('Malphite.png', region=regiao)
        if(coordinates != None):
            pg.moveTo(coordinates[0], coordinates[1],_pause=False)
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
        if (coordinates != None):
            pg.moveTo(coordinates[0], coordinates[1],_pause=False)
            mouse.click()

def compra():
    comp()
    pg.moveTo(362, 990,_pause=False)
    print("feito")
    mouse.click()


def dinheiro():
    image =  pg.screenshot(region=(340, 980, 25, 25))
    image.save("screenshot.png")
    print(textract.process("screenshot.png"))
while(ativo):
    if(keyboard.read_key() == 'y'):
      compra()
    if(keyboard.read_key() == 'i'):
        print("ta aq")
        break
    if (keyboard.read_key() == 'p'):
        dinheiro()
