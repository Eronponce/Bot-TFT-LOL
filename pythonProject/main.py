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

# Define a região com base nos pontos capturados
regiao = (comecoreal[0], comecoreal[1], finalreal[0] - comecoreal[0], finalreal[1] - comecoreal[1])
print(f"Região definida: {regiao}")

# Captura uma imagem da região selecionada
screenshot = pg.screenshot(region=regiao)
screenshot.save("regiao_selecionada.png")
print("Captura de tela da região salva como 'regiao_selecionada.png'")

# Loop para encontrar a imagem "like.png" na tela
for i in range(1000):
    attempts = 0
    found = False

    # Tentar encontrar a imagem até 3 vezes
    while attempts < 3 and not found:
        try:
            coordinates = pg.locateOnScreen('adc.png', region=regiao, confidence=0.9)
            if coordinates is not None:
                print(f"Localizado em {coordinates}")
                pg.click(coordinates[0] + 10, coordinates[1] + 10)
                found = True  # Marca como encontrado
            else:
                print(f"Tentativa {attempts + 1}: Imagem não encontrada")
                attempts += 1
                time.sleep(0.5)  # Pausa curta antes de tentar novamente
        except pg.ImageNotFoundException:
            print(f"Tentativa {attempts + 1}: Imagem não encontrada na tela")
            attempts += 1
            time.sleep(0.5)  # Pausa curta antes de tentar novamente

    # Caso não tenha encontrado após 3 tentativas, faz o scroll
    if not found:
        print("Imagem não encontrada após 3 tentativas, realizando scroll...")
    
    pg.scroll(-250)
    time.sleep(0.25)
