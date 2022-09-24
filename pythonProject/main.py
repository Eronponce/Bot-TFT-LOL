import csv
import time
import pyautogui as pg
i = 0
condicao = 0

with open("./Frases.csv", 'r') as file:
  csvreader = csv.reader(file)
  for i in range(1000):
    condicao = 0
    while condicao != 30 :
        try:
            coordinates = pg.locateOnScreen('bruiser.png', confidence = 0.5)
            print(coordinates)
            cor = pg.pixel(int(coordinates[0])+20,int(coordinates[1])+20)
            if cor == (245, 245, 245):
                pg.click(coordinates[0] + 20, coordinates[1] + 20)
                time.sleep(1)
            else:
                condicao = condicao + 1
        except:
            print("nao encontrado")
            condicao = condicao + 1

        pg.scroll(-200)
        time.sleep(1)

    time.sleep(1)
    pg.click(325, 16)
    time.sleep(1)
    pg.click(1270, 125)
    time.sleep(1)
    pg.click(1635, 208)
    time.sleep(7)