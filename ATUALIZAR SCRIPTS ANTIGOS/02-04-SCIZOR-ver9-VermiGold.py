import pyautogui
import time
import random
import pydirectinput

#SCRIPT WINODWS
#SCRIPT LVL 108+

#ROBO COM SCIZOR & TAUROS COM ISCA KEPT

#AJUSTE DO MAPA: CHAT ME
#LUGAR: CHAT ME
#ESTE CODIGO POSSUI PROTEÇAO CONTRA SHINY KINGLER

#PESCA,PEGA LOOT, CORRE QND BATER RED NO POKE, VAI CP HEALAR SE ESTIVER DERROTADO

#IR PARA PXG
pyautogui.keyDown('alt')

pyautogui.press('tab')

pyautogui.keyUp('alt')

#CONTADOR QUASE MORTES
quase = 0
#CONTADOR SHINY
shiny = 0
#VARIAVEL CHAT
chat = 0
#VARIAVEL NÃO ESPERA CD INICIO
cd = 0
#VARIEVEL PLAYER TELA
pl = 0


def redvida():

    #subir escada
    pydirectinput.keyDown('ctrl')
    pyautogui.moveTo(x=680, y=358)
    pyautogui.rightClick()
    time.sleep(0.5)
    pyautogui.moveTo(x=692, y=395)
    pyautogui.click()
    pydirectinput.keyUp('ctrl')

    sair = 0

    time.sleep(4)

    if pyautogui.locateCenterOnScreen('deadscizor.png'):

        sair = 1

        #SOLTAR TAUROS
        pyautogui.moveTo('tauros.png')
        pyautogui.click()

        time.sleep(0.5)

        #RIDE TAUROS
        pyautogui.moveTo(x=681, y=261)
        pyautogui.middleClick()

        time.sleep(1)

        #IR MAPA
        pyautogui.moveTo(x=1310, y=286)
        pyautogui.click()

        #IDA ATÉ CP
        time.sleep(24)

        #ENCONTRANDO NPC
        if pyautogui.pixelMatchesColor(673, 184, (221, 221, 221)):

            #CURAR
            pyautogui.moveTo(673, 184)
            pyautogui.rightClick()

            time.sleep(2.5)

            #SOLTAR TAUROS
            pyautogui.moveTo('tauros.png')
            pyautogui.click()

            time.sleep(2)

            #RIDE TAUROS
            pyautogui.moveTo(x=681, y=261)
            pyautogui.middleClick()

            time.sleep(1)

            #IR MAPA VOLTAR ESCADA
            pyautogui.moveTo(x=1218, y=80)
            pyautogui.click()

            time.sleep(26)

            #SAIR RIDE
            pyautogui.moveTo(x=681, y=261)
            pyautogui.middleClick()

            time.sleep(3.5)

            #CLICAR SCIZOR
            pyautogui.moveTo('scizorvivo.png')
            pyautogui.click()

            #IR POSIÇÃO
            pyautogui.moveTo(x=679, y=181)
            pyautogui.click()

            time.sleep(1.5)

        else:

            #SAIR JOGO
            pyautogui.moveTo(x=1342, y=12)
            pyautogui.click()

            time.sleep(1)

            #CLICAR SIM SAIR JOGO
            pyautogui.moveTo(x=569, y=409)
            pyautogui.click()

            exit()

    else:
        pass

    if sair == 0:

        #ESPERA SUMIR
        time.sleep(32)

        #descer escada
        pyautogui.moveTo(x=681, y=236)
        pyautogui.click()

        time.sleep(1.5)

        #LOOT redvida 1
        pydirectinput.keyDown('e')
        time.sleep(0.3)
        pydirectinput.keyUp('e')

        #IR POSIÇÃO
        pyautogui.moveTo(x=679, y=181)
        pyautogui.click()

        time.sleep(1.5)

        #LOOT redvida 2
        pydirectinput.keyDown('e')
        time.sleep(0.3)
        pydirectinput.keyUp('e')

    else:
        pass



def sairjogo():

    #subir escada
    pydirectinput.keyDown('ctrl')
    pyautogui.moveTo(x=680, y=358)
    pyautogui.rightClick()
    time.sleep(0.5)
    pyautogui.moveTo(x=692, y=395)
    pyautogui.click()
    pydirectinput.keyUp('ctrl')

    #IR MENU
    pyautogui.moveTo(x=683, y=35)
    pyautogui.click()

    time.sleep(1)

    #SAIR CHAR
    if pyautogui.locateCenterOnScreen('zbotaosair.png'):

        pyautogui.moveTo('zbotaosair.png')
        pyautogui.click()

        time.sleep(1)

        #CONFIRMAR
        pyautogui.moveTo(x=589, y=399)
        pyautogui.click()

        print('SAINDO JOGO FUNÇÃO SAIR JOGO')
    
    else:

        #espera deslogar sozinho (800)
        time.sleep(800)

        print('NÃO ENCONTROU BOTAO SAIR JOGO')

    #ESPERA UM POUCO (1500)
    time.sleep(1500)

    #ENCONTRAR O BOTAO JOGAR
    if pyautogui.pixelMatchesColor(486, 293, (171, 212, 141)):

        #IR PARA JOGAR
        pyautogui.moveTo(x=679, y=628)
        pyautogui.click()

        #ESPERA LOGAR
        time.sleep(30)
    
    else:

        #SAIR JOGO
        pyautogui.moveTo(x=1342, y=12)
        pyautogui.click()

        time.sleep(1)

        #CLICAR SIM SAIR JOGO
        pyautogui.moveTo(x=569, y=409)
        pyautogui.click()

        exit ()

    #COLOCAR ISCA KEPT
    pyautogui.moveTo(x=887, y=586)
    pyautogui.click()

    #descer escada
    pyautogui.moveTo(x=681, y=236)
    pyautogui.click()

    time.sleep(1)

    #IR POSIÇÃO
    pyautogui.moveTo(x=679, y=181)
    pyautogui.click()

    time.sleep(2)

    #CLICAR SCIZOR
    pyautogui.moveTo('scizorvivo.png')
    pyautogui.click()


    
def lago1():
    pyautogui.moveTo(x=810, y=287)
    pyautogui.click()


def lago2():
    pyautogui.moveTo(x=815, y=390)
    pyautogui.click()


def lago3():
    pyautogui.moveTo(x=1100, y=333)
    pyautogui.click()


def lago4():
    pyautogui.moveTo(x=975, y=375)
    pyautogui.click()


def lago5():
    pyautogui.moveTo(x=862, y=323)
    pyautogui.click()


def lago6():
    pyautogui.moveTo(x=908, y=289)
    pyautogui.click()

time.sleep(1)

#COLOCAR ISCA KEPT
pyautogui.moveTo(x=887, y=586)
pyautogui.click()

#PARE-MID
pyautogui.moveTo(x=133, y=83)
pyautogui.click()

#CHECAGEM ISCA
if pyautogui.pixelMatchesColor(272, 673, (159, 157, 253)):

   pass

else:

    #COLOCA ISCA KEPT
    pyautogui.moveTo(x=887, y=586)
    pyautogui.click()

#CICLO PESCA, ATTACK, LOOT, FUGIR

while True:

    #VERIFICAÇAO RED LIFE
    if pyautogui.pixelMatchesColor(117, 60, (158, 91, 78)) or pyautogui.locateCenterOnScreen('deadscizor.png'):

        redvida()

        quase = quase + 1
        print('O total de quase mortes foi:', quase)

        continue

    else:

        pass

    #VARIAVEL VOLTA AO COMEÇO SHINY
    sair = 0

    #VERIFICAÇAO RED LIFE
    if pyautogui.pixelMatchesColor(117, 60, (158, 91, 78)) or pyautogui.locateCenterOnScreen('deadscizor.png'):

        redvida()

        quase = quase + 1
        print('O total de quase mortes foi:', quase)

        continue

    else:

        pass

    #CICLO CHECAGEM POSIÇÃO POKE
    for posi in range(0, 2):
        #CHECAGEM POKE POSIÇÃO
        if pyautogui.pixelMatchesColor(682, 308, (213, 83, 92)) or pyautogui.pixelMatchesColor(688, 322, (67, 14, 17)) or pyautogui.pixelMatchesColor(689, 322, (78, 16, 20)):

            pass
        
        else:

            #MID POKE
            pyautogui.moveTo(x=684, y=321)
            pyautogui.middleClick()
            time.sleep(2)

            #PARE-MID
            pyautogui.moveTo(x=133, y=83)
            pyautogui.click()

            #MIRA POKE NORTE
            pydirectinput.keyDown('ctrl')
            pydirectinput.keyDown('up')
            pydirectinput.keyUp('ctrl')
            pydirectinput.keyUp('up')


    #VERIFICAÇAO RED LIFE
    if pyautogui.pixelMatchesColor(117, 60, (158, 91, 78)) or pyautogui.locateCenterOnScreen('deadscizor.png'):

        redvida()

        quase = quase + 1
        print('O total de quase mortes foi:', quase)

        continue

    else:

        pass

    #LOOT 2
    pydirectinput.keyDown('e')
    time.sleep(0.1)
    pydirectinput.keyUp('e')

    #PESCA 1
    pyautogui.moveTo(x=346, y=582)
    pyautogui.click()

    #LAGO
    #LISTA SQMs LAGO
    lagolista = [lago1, lago2, lago3, lago4, lago5, lago6]
    #JOGA ALEATORIAMENTE EM EM SQM DA LSITA
    random.choice(lagolista)()

    #CHECAGEM BATTLE YELLOW LIFE
    if pyautogui.pixelMatchesColor(1183, 445, (7, 9, 12)):

        pass
    
    else:

        #VERIFICAÇAO RED & YELLOW LIFE
        if pyautogui.pixelMatchesColor(117, 60, (158, 91, 78)) or pyautogui.pixelMatchesColor(117, 60, (142, 150, 74)) or pyautogui.locateCenterOnScreen('deadscizor.png'):

            redvida()
            quase = quase + 1
            print('O total de quase mortes foi:', quase)
            continue

    #CLICAR NO ICONE POKEBATTLE 1
    pyautogui.moveTo(x=1256, y=387)
    pyautogui.click()

    #CLICAR NO ICONE PLAYER BATTLE 1
    pyautogui.moveTo(x=1185, y=384)
    pyautogui.click()

    time.sleep(0.5)

    #CHECAGEM PLAYER
    if pyautogui.pixelMatchesColor(1183, 445, (7, 9, 12)):

        pl = 0
    
    else:

        pl = pl + 1

        if pl == 2:

            #Clica local chat
            pyautogui.moveTo(x=313, y=704)
            pyautogui.click()

            #Escreve no chat
            time.sleep(0.5)
            pyautogui.write('oi')
            pydirectinput.keyDown('enter')
            pydirectinput.keyUp('enter')

            sc = pyautogui.screenshot()
            sc.save('playerbattle.png')

            #LIMPANDO CHAT
            pyautogui.moveTo(x=1083, y=631)
            pyautogui.click()

            pl = 4


    #RETIRAR ICONE PLAYER BATTLE 2
    pyautogui.moveTo(x=1185, y=384)
    pyautogui.click()

    #CLICAR NO ICONE POKEBATTLE 2
    pyautogui.moveTo(x=1256, y=387)
    pyautogui.click()

    time.sleep(24)
    
    #VERIFICAÇAO RED LIFE
    if pyautogui.pixelMatchesColor(117, 60, (158, 91, 78)) or pyautogui.locateCenterOnScreen('deadscizor.png'):

        redvida()

        quase = quase + 1
        print('O total de quase mortes foi:', quase)

        continue

    else:

        pass

    #chat 3 
    if chat == 2:

        if pyautogui.pixelMatchesColor(242, 682, (212, 212, 1)) or pyautogui.pixelMatchesColor(243, 676, (246, 246, 0)):
            
            #Clica local chat
            pyautogui.moveTo(x=313, y=704)
            pyautogui.click()

            #Escreve no chat
            pyautogui.write('TEXTO')
            pydirectinput.keyDown('enter')
            pydirectinput.keyUp('enter')

            sc = pyautogui.screenshot()
            sc.save('chat3.png')

            #LIMPANDO CHAT
            pyautogui.moveTo(x=1083, y=631)
            pyautogui.click()

            chat = 3


    #CHAT 2
    if chat == 1:

        if pyautogui.pixelMatchesColor(242, 682, (212, 212, 1)) or pyautogui.pixelMatchesColor(243, 676, (246, 246, 0)):
            
            #Clica local chat
            pyautogui.moveTo(x=313, y=704)
            pyautogui.click()

            #Escreve no chat
            pyautogui.write('TEXTO')
            pydirectinput.keyDown('enter')
            pydirectinput.keyUp('enter')

            sc = pyautogui.screenshot()
            sc.save('chat2.png')

            #LIMPANDO CHAT
            pyautogui.moveTo(x=1083, y=631)
            pyautogui.click()

            #ATIVA CHAT 3
            chat = 2


    #CHAT 1
    if chat == 0:

        if pyautogui.pixelMatchesColor(242, 682, (212, 212, 1)) or pyautogui.pixelMatchesColor(243, 676, (246, 246, 0)):
            
            #Clica local chat
            pyautogui.moveTo(x=313, y=704)
            pyautogui.click()

            #Escreve no chat
            pyautogui.write('TEXTO')
            pydirectinput.keyDown('enter')
            pydirectinput.keyUp('enter')

            sc = pyautogui.screenshot()
            sc.save('chat1.png')

            #LIMPANDO CHAT
            pyautogui.moveTo(x=1083, y=631)
            pyautogui.click()

            #DESATIVA PROTEÇÃO PLAER BATTLE
            pl = 4

            #ATIVA CHAT 2
            chat = 1
            
        else:
            pass
    

    #8 - SWORD DANCE
    pyautogui.moveTo(x=832, y=513)
    pyautogui.click()

    #PESCA 2
    pyautogui.moveTo(x=346, y=582)
    pyautogui.click()

    #ESPERAR APARECER POKE BAT
    time.sleep(1)

    #VERIFICAÇÃO SHINY
    for sh in range(0, 2):

        #CHECAGEM SHINY
        if pyautogui.pixelMatchesColor(1183, 448, (19,52,137)) or pyautogui.locateCenterOnScreen('kingbat2.png'):
            print('------'*5)
            shiny = shiny + 1
            print('O total de shinys que apareceram eh:', shiny)
            print('------'*5)
            redvida()
            sair = 1

    #VOLTAR AO COMEÇO CASO APARECER UM SHINY (UTILIZA POR CONTA DO 'FOR')
    if sair == 1:
        continue
    else:
        pass
    
    #ATTACKs

    #6 - COMPASS SLASH
    pyautogui.moveTo(x=758, y=513)
    pyautogui.click()

    #BATTLE 1
    pyautogui.moveTo(x=1183, y=445)
    pyautogui.click()

    #4 - RED FURY
    time.sleep(1)
    pyautogui.moveTo(x=690, y=515)
    pyautogui.click()

    #VERIFICAÇAO RED LIFE
    if pyautogui.pixelMatchesColor(117, 60, (158, 91, 78)) or pyautogui.locateCenterOnScreen('deadscizor.png'):

        redvida()

        quase = quase + 1
        print('O total de quase mortes foi:', quase)

        continue

    else:

        pass

    #1 - QUICK ATTACK
    pyautogui.moveTo(x=578, y=513)
    pyautogui.click()

    #BATTLE 2 - segunda posiçao
    time.sleep(1)
    pyautogui.moveTo(x=1185, y=479)
    pyautogui.click()

    #VERIFICAÇAO RED LIFE
    if pyautogui.pixelMatchesColor(117, 60, (158, 91, 78)) or pyautogui.locateCenterOnScreen('deadscizor.png'):

        redvida()

        quase = quase + 1
        print('O total de quase mortes foi:', quase)

        continue

    else:

        pass

    #2 - IRON HEAD
    time.sleep(1)
    pyautogui.moveTo(x=614, y=514)
    pyautogui.click()

    #VOID ATTACK OR NOT 1
    if pyautogui.pixelMatchesColor(1182, 445, (7, 9, 12)):

        pass
    
    else:

        #BATTLE 1
        time.sleep(0.5)
        pyautogui.moveTo(x=1183, y=445)
        pyautogui.click()
        
        #3 - WING BLADE
        time.sleep(1)
        pyautogui.moveTo(x=653, y=514)
        pyautogui.click()

    #VERIFICAÇAO RED LIFE
    if pyautogui.pixelMatchesColor(117, 60, (158, 91, 78)) or pyautogui.locateCenterOnScreen('deadscizor.png'):

        redvida()

        quase = quase + 1
        print('O total de quase mortes foi:', quase)

        continue

    else:

        pass


    #VOID ATTAK OR NOT 2
    if pyautogui.pixelMatchesColor(1182, 445, (7, 9, 12)):

        pass
    
    else:

        #BATTLE 1
        time.sleep(0.5)
        pyautogui.moveTo(x=1183, y=445)
        pyautogui.click()

        time.sleep(6)


    #VERIFICAÇAO RED LIFE
    if pyautogui.pixelMatchesColor(117, 60, (158, 91, 78)) or pyautogui.locateCenterOnScreen('deadscizor.png'):

        redvida()

        quase = quase + 1
        print('O total de quase mortes foi:', quase)

        continue

    else:

        pass
    
    #LOOT 1
    pydirectinput.keyDown('e')
    time.sleep(0.1)
    pydirectinput.keyUp('e')

    #VERIFICAÇAO RED LIFE
    if pyautogui.pixelMatchesColor(117, 60, (158, 91, 78)) or pyautogui.locateCenterOnScreen('deadscizor.png'):

        redvida()

        quase = quase + 1
        print('O total de quase mortes foi:', quase)

        continue

    else:

        pass

    #FOME POKEMON
    if pyautogui.pixelMatchesColor(175, 84, (203, 98, 79)):

        #CLICA NA PIZZA
        time.sleep(0.5)
        pyautogui.moveTo(x=809, y=585)
        pyautogui.click()

    #VERIFICAÇAO RED LIFE
    if pyautogui.pixelMatchesColor(117, 60, (158, 91, 78)) or pyautogui.locateCenterOnScreen('deadscizor.png'):

        redvida()

        quase = quase + 1
        print('O total de quase mortes foi:', quase)

        continue

    else:

        pass

    #chat 3 
    if chat == 2:

        if pyautogui.pixelMatchesColor(242, 682, (212, 212, 1)) or pyautogui.pixelMatchesColor(243, 676, (246, 246, 0)):
            
            #Clica local chat
            pyautogui.moveTo(x=313, y=704)
            pyautogui.click()

            #Escreve no chat
            pyautogui.write('TEXTO')
            pydirectinput.keyDown('enter')
            pydirectinput.keyUp('enter')

            sc = pyautogui.screenshot()
            sc.save('chat3.png')

            #LIMPANDO CHAT
            pyautogui.moveTo(x=1083, y=631)
            pyautogui.click()

            chat = 3


    #CHAT 2
    if chat == 1:

        if pyautogui.pixelMatchesColor(242, 682, (212, 212, 1)) or pyautogui.pixelMatchesColor(243, 676, (246, 246, 0)):
            
            #Clica local chat
            pyautogui.moveTo(x=313, y=704)
            pyautogui.click()

            #Escreve no chat
            pyautogui.write('TEXTO')
            pydirectinput.keyDown('enter')
            pydirectinput.keyUp('enter')

            sc = pyautogui.screenshot()
            sc.save('chat2.png')

            #LIMPANDO CHAT
            pyautogui.moveTo(x=1083, y=631)
            pyautogui.click()

            #ATIVA CHAT 3
            chat = 2


    #CHAT 1
    if chat == 0:

        if pyautogui.pixelMatchesColor(242, 682, (212, 212, 1)) or pyautogui.pixelMatchesColor(243, 676, (246, 246, 0)):
            
            #Clica local chat
            pyautogui.moveTo(x=313, y=704)
            pyautogui.click()

            #Escreve no chat
            pyautogui.write('TEXTO')
            pydirectinput.keyDown('enter')
            pydirectinput.keyUp('enter')

            sc = pyautogui.screenshot()
            sc.save('chat1.png')

            #LIMPANDO CHAT
            pyautogui.moveTo(x=1083, y=631)
            pyautogui.click()

            #DESATIVA PROTEÇÃO PLAER BATTLE
            pl = 4

            #ATIVA CHAT 2
            chat = 1
            
        else:
            pass
     
    
    #chat 6 FINAL
    if chat == 5:

        if pyautogui.pixelMatchesColor(242, 682, (212, 212, 1)) or pyautogui.pixelMatchesColor(243, 676, (246, 246, 0)):
            
            #Clica local chat
            pyautogui.moveTo(x=313, y=704)
            pyautogui.click()

            #Escreve no chat
            pyautogui.write('TEXTO')
            pydirectinput.keyDown('enter')
            pydirectinput.keyUp('enter')

            chat = 4

            sc = pyautogui.screenshot()
            sc.save('chat6.png')

            #LIMPANDO CHAT
            pyautogui.moveTo(x=1083, y=631)
            pyautogui.click()


    #chat 5 
    if chat == 4:

        if pyautogui.pixelMatchesColor(242, 682, (212, 212, 1)) or pyautogui.pixelMatchesColor(243, 676, (246, 246, 0)):
            
            #Clica local chat
            pyautogui.moveTo(x=313, y=704)
            pyautogui.click()

            #Escreve no chat
            pyautogui.write('TEXTO')
            pydirectinput.keyDown('enter')
            pydirectinput.keyUp('enter')

            chat = 5

            sc = pyautogui.screenshot()
            sc.save('chat5.png')

            #LIMPANDO CHAT
            pyautogui.moveTo(x=1083, y=631)
            pyautogui.click()

    
        pass

   
        pass


    #chat 4 SEMI FINAL
    if chat == 3:

        if pyautogui.pixelMatchesColor(242, 682, (212, 212, 1)) or pyautogui.pixelMatchesColor(243, 676, (246, 246, 0)):
            
            #Clica local chat
            pyautogui.moveTo(x=313, y=704)
            pyautogui.click()

            #Escreve no chat
            pyautogui.write('TEXTO')
            pydirectinput.keyDown('enter')
            pydirectinput.keyUp('enter')

            sc = pyautogui.screenshot()
            sc.save('chat4.png')

            chat = 4

            #LIMPANDO CHAT
            pyautogui.moveTo(x=1083, y=631)
            pyautogui.click()

            sairjogo()


    #VERIFICAÇAO RED LIFE
    if pyautogui.pixelMatchesColor(117, 60, (158, 91, 78)) or pyautogui.locateCenterOnScreen('deadscizor.png'):

        redvida()

        quase = quase + 1
        print('O total de quase mortes foi:', quase)

        continue

    else:

        pass

    #SAIR DA PXG CASO CAIR NET OU DEAD, PUXA COR FUNDO LATERAL ESQUERDA POKE
    if pyautogui.pixelMatchesColor(7, 31, (21, 23, 26)):

        pass

    else:

        #CAPTURA A TELA
        sc = pyautogui.screenshot()
        sc.save('fimbotnet.png')

        #300 - espera voltar net
        time.sleep(300)

        #CLICAR BOTÃO JOGAR CIMA
        pyautogui.moveTo(x=762, y=78)
        pyautogui.click()

        time.sleep(1)

        #CLICAR BOTÃO JOGAR AZUL
        pyautogui.moveTo(x=687, y=642)
        pyautogui.click()
        
        #35 - espera entrar sever
        time.sleep(35)

        #CHECAGEM BOTÃO VERMELHO
        if pyautogui.pixelMatchesColor(777, 478, (171, 51, 26)):

            sc = pyautogui.screenshot()
            sc.save('fimbotnet2.png')

            #CLICAR BOTÃO CANCELAR
            pyautogui.moveTo(793, 476)
            pyautogui.click()

            #MINIMIZA
            pyautogui.moveTo(x=1242, y=14)
            time.sleep(1.5)
            pyautogui.click()

            print('PROBLEMA NET OU SERVER')

            exit()
    
        #CHECAGEM MADEIRA
        if pyautogui.pixelMatchesColor(550, 237, (135, 92, 52)):

            #CLICAR SCIZOR
            pyautogui.moveTo('scizorvivo.png')
            pyautogui.click()

            #COLOCAR ISCA KEPT
            pyautogui.moveTo(x=887, y=586)
            pyautogui.click()
        
        else:

            #SAIR JOGO
            pyautogui.moveTo(x=1342, y=12)
            pyautogui.click()

            time.sleep(1)

            #CLICAR SIM SAIR JOGO
            pyautogui.moveTo(x=569, y=409)
            pyautogui.click()

            print('NÃO ESTÁ NA POSIÇÃO CORRETA')

            exit()

