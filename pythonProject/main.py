import keyboard
import time
import pyautogui as pg
i = 0
condicao = 0
pg.PAUSE = 0.1


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
comecoreal = definirRegiao1()
finalreal = definirRegiao2()
regiao = (comecoreal[0],comecoreal[1], finalreal[0] - comecoreal[0] , finalreal[1] -comecoreal[1])
print(regiao)
for i in range(1000):

    coordinates = pg.locateOnScreen('like.png',region=regiao,confidence = 0.9)
    print(coordinates)
    if (coordinates != None):
        print(coordinates)
        pg.click(coordinates[0] + 20, coordinates[1] + 20)
    pg.scroll(-150)
    time.sleep(1)
