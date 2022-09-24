import csv
import time
import pyautogui as pg
i = 0
condicao = 0

with open("./Frases.csv", 'r') as file:
  csvreader = csv.reader(file)
  for i in range(1000):
    try:
        coordinates = pg.locateOnScreen('adiciona.png', confidence = 0.5)
        print(coordinates)
        pg.click((coordinates[0])+20,int(coordinates[1])+20)
    except:
        print("nao encontrado")
    pg.scroll(-50)
    time.sleep(1)