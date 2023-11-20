import pyautogui
import pydirectinput
import time

pyautogui.keyDown('alt')

pyautogui.press('tab')

pyautogui.keyUp('alt')

REGION = (650, 336, 45, 356)

#time.sleep(3)


#ENCONTRA TEST HUMAN
while True:

    #ENTROU HUMAN TEST
    tempo = 1

    peixe = pyautogui.locateOnScreen('peixeg.png', confidence=0.8, region=REGION, grayscale= True)
    barra = pyautogui.locateOnScreen('pontabarra.png', confidence=0.8, region=REGION)

    #SAIR DA PXG CASO CAIR NET OU DEAD, PUXA COR IGRENAGEM LADO DIREITO
    if pyautogui.pixelMatchesColor(1225, 87, (204, 204, 204)):

        print('caiu')

    if peixe != None and barra != None: 

        if barra.top > peixe.top:
            
            pydirectinput.keyDown('space')

        else:
            
            pydirectinput.keyUp('space')
    
    else:
        #desbuga a tecla espaço 1
        pydirectinput.keyDown('space')
        time.sleep(0.2)
        pydirectinput.keyUp('space')

time.sleep(0.5)

#desbuga a tecla espaço 2
pydirectinput.keyDown('space')
time.sleep(0.2)
pydirectinput.keyUp('space')
