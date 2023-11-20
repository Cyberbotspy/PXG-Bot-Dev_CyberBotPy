import pyautogui

# 0,732, 1100, 33
#REGIONMAR1 = (790, 428, 72, 60)
#REGIONMAR2 = (766, 320, 204, 144)
#REGIONMAR3 = (726, 387, 194, 93)
####
#REGIONMAR2 = (831, 417, 81, 72)
#REGCHAT = (220, 646, 325, 46)
#REGBAT = (1164, 400, 198, 149)
#REGPV = (255, 612, 531, 45)

while True:

    regiao = pyautogui.locateOnScreen('reg.png', confidence=0.8)
   
    print(regiao)
    
