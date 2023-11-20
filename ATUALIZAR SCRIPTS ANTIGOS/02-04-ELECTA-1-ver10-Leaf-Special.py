import pyautogui
import time
import random
import pydirectinput

#SCRIPT WINODWS
#SCRIPT LVL 112+

#ROBO COM ELECTABUZ & TAUROS COM ISCA ESPECIAL

#AJUSTE DO MAPA: CHAT ME
#LUGAR: CHAT ME
#ESTE CODIGO POSSUI PROTEÇAO CONTRA SHINY POLITOED

#PESCA, PEGA LOOT, CORRE QND BATER RED NO POKE, VAI CP HEALAR SE ESTIVER DERROTADO

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

    #descer escada
    pyautogui.moveTo(x=681, y=308)
    pyautogui.click()

    sair = 0

    time.sleep(4)

    if pyautogui.pixelMatchesColor(52, 63, (120, 120, 120)) or pyautogui.locateCenterOnScreen('electadead.png'):

        sair = 1

        print('USOU REVIVE')

        #ESPERA SUMIR
        time.sleep(32)

        #SELECIONAR REVIVE
        pyautogui.moveTo(x=771, y=581)
        pyautogui.click()

        #MOVER PARA O ELECTABUZZ
        pyautogui.moveTo(x=35, y=50)
        pyautogui.click()
        
        time.sleep(1)

        #MOVER MOUSE PARA NÃO BUGAR
        pyautogui.moveTo(x=730, y=239)

        time.sleep(1)

        #CLICAR ELECTABUZ
        pyautogui.moveTo('electa.png')
        pyautogui.click()

        time.sleep(1)

        #SUBIR ESCADA
        pyautogui.moveTo(x=676, y=224)
        pyautogui.click()

        time.sleep(1.5)

        #CHECAGEM SHINY 2
        if pyautogui.pixelMatchesColor(1185, 447, (128, 127, 115)) or pyautogui.pixelMatchesColor(1183, 447, (210, 211, 203)):

            sc = pyautogui.screenshot()
            sc.save('shiny-escada-2.png')

            redvida()

    else:
        pass

    if sair == 0:

        #ESPERA SUMIR
        time.sleep(32)

        #subir escada
        pyautogui.moveTo(x=676, y=224)
        pyautogui.click()

        time.sleep(1.5)

        #LOOT redvida
        pydirectinput.keyDown('e')
        time.sleep(0.3)
        pydirectinput.keyUp('e')

        #CHECAGEM SHINY 3
        if pyautogui.pixelMatchesColor(1185, 447, (128, 127, 115)) or pyautogui.pixelMatchesColor(1183, 447, (210, 211, 203)):

            sc = pyautogui.screenshot()
            sc.save('shiny-escada-2.png')

            redvida()


def sairjogo():

    #descer escada
    pyautogui.moveTo(x=681, y=308)
    pyautogui.click()

    #IR MENU
    pyautogui.moveTo(x=683, y=35)
    pyautogui.click()

    time.sleep(1)

    #SAIR DO CHAR
    if pyautogui.locateCenterOnScreen('zbotaosair.png'):

        #IR BOTAO SAIR
        pyautogui.moveTo('zbotaosair.png')
        pyautogui.click()

        time.sleep(1)

        #CONFIRMAR
        pyautogui.moveTo(x=589, y=399)
        pyautogui.click()

        print('SAINDO JOGO FUNÇÃO SAIR JOGO')

        time.sleep(3)

        #SE ALGO DER ERRADO AO SAIR
        if pyautogui.pixelMatchesColor(792, 179, (5, 25, 55)):

            sc = pyautogui.screenshot()
            sc.save('failsair.png')

            #SAIR JOGO
            pyautogui.moveTo(x=1342, y=12)
            pyautogui.click()

            time.sleep(1)

            #CLICAR SIM SAIR JOGO
            pyautogui.moveTo(x=569, y=409)
            pyautogui.click()

            exit()

    
    else:

        print('NÃO ENCONTROU BOTAO SAIR JOGO')

        #espera deslogar sozinho (800)
        time.sleep(800)


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

        exit()

    #COLOCAR ISCA ESPECIAL
    pyautogui.moveTo(x=1000, y=585)
    pyautogui.click()

    #subir escada
    pyautogui.moveTo(x=676, y=224)
    pyautogui.click()

    time.sleep(1)

    #CLICAR ELECTABUZ
    pyautogui.moveTo('electa.png')
    pyautogui.click()

    #CLICAR NO ICONE POKEBATTLE 1
    pyautogui.moveTo(x=1256, y=387)
    pyautogui.click()

    #CLICAR NO ICONE PLAYER BATTLE 1
    pyautogui.moveTo(x=1185, y=384)
    pyautogui.click()

    time.sleep(0.5)

    #CHECAGEM PLAYER
    if pyautogui.pixelMatchesColor(1183, 445, (7, 9, 12)):

        #CLICAR NO ICONE PLAYER BATTLE 1
        pyautogui.moveTo(x=1185, y=384)

        #CLICAR NO ICONE POKEBATTLE 1
        pyautogui.moveTo(x=1256, y=387)
        pyautogui.click()
    
    else:

        #CLICAR NO ICONE PLAYER BATTLE 1
        pyautogui.moveTo(x=1185, y=384)

        #CLICAR NO ICONE POKEBATTLE 1
        pyautogui.moveTo(x=1256, y=387)
        pyautogui.click()

        print('PLAYER POR PERTO OU NO LUGAR')

        sc = pyautogui.screenshot()
        sc.save('playertela.png')

        #SAIR JOGO
        pyautogui.moveTo(x=1342, y=12)
        pyautogui.click()

        time.sleep(1)

        #CLICAR SIM SAIR JOGO
        pyautogui.moveTo(x=569, y=409)
        pyautogui.click()

        exit()



def lago1():
    pyautogui.moveTo(x=1096, y=512)
    pyautogui.click()


def lago2():
    pyautogui.moveTo(x=1145, y=511)
    pyautogui.click()


time.sleep(1)

#COLOCAR ISCA SPECIAL
pyautogui.moveTo(x=1000, y=585)
pyautogui.click()

#PARE-MID
pyautogui.moveTo(x=133, y=83)
pyautogui.click()

#CHECAGEM ISCA
if pyautogui.pixelMatchesColor(272, 673, (159, 157, 253)):

   pass

else:

    #COLOCA ISCA SPECIAL
    pyautogui.moveTo(x=1000, y=585)
    pyautogui.click()

#CICLO PESCA, ATTACK, LOOT, FUGIR

while True:

    #VARIAVEL VOLTA AO COMEÇO SHINY
    sair = 0
    #VARIAVAL PROTEC PLAYER
    battleplayer = 0
    #VARIAVEL MENSAGEMCD
    mensagemcd = 1

    #CHECAGEM BATTLE YELLOW LIFE
    if pyautogui.pixelMatchesColor(1183, 445, (7, 9, 12)):

        pass
    
    else:

        #VERIFICAÇAO RED & YELLOW LIFE
        if pyautogui.pixelMatchesColor(117, 60, (158, 91, 78)) or pyautogui.pixelMatchesColor(117, 60, (142, 150, 74)) or pyautogui.pixelMatchesColor(52, 63, (120, 120, 120)) or pyautogui.pixelMatchesColor(1338, 409, (7, 9, 12)):
            redvida()
            quase = quase + 1
            print('O total de quase mortes foi:', quase)
            continue

    #LOOT 2
    pydirectinput.keyDown('e')
    time.sleep(0.1)
    pydirectinput.keyUp('e')

    #CHECAGEM BATTLE YELLOW LIFE 1
    if pyautogui.pixelMatchesColor(1183, 445, (7, 9, 12)):

        pass
    
    else:

        #VERIFICAÇAO RED & YELLOW LIFE
        if pyautogui.pixelMatchesColor(117, 60, (158, 91, 78)) or pyautogui.pixelMatchesColor(117, 60, (142, 150, 74)) or pyautogui.pixelMatchesColor(52, 63, (120, 120, 120)) or pyautogui.pixelMatchesColor(1338, 409, (7, 9, 12)):

            redvida()
            quase = quase + 1
            print('O total de quase mortes foi:', quase)
            continue

    #ESPERA CD
    if cd == 1:
        
        #SE CONTIVER ALGO NA PRIMEIRA POSI NO BAT ESPERA 10s
        if pyautogui.pixelMatchesColor(1182, 445, (7, 9, 12)):

            time.sleep(10)

        else:
            
            #ENQUANTO TIVER UM POKEMON NO BATTLE ELE EXECUTA VERIFICAÇÃO REDLIFE
            while pyautogui.pixelMatchesColor(1182, 445, (7, 9, 12)) == False:

                #FAZER COM QUE TRANSMITA SOMENTE UMA MENSAGEM
                if mensagemcd == 1:

                    print('entrou no while poke bat')
                    mensagemcd = 0

                #SOMATORIA VARIVEL PARA SAIR WHILE
                battleplayer = battleplayer + 1

                #VERIFICAÇAO RED & YELLOW LIFE
                if pyautogui.pixelMatchesColor(117, 60, (158, 91, 78)) or pyautogui.pixelMatchesColor(117, 60, (142, 150, 74)) or pyautogui.pixelMatchesColor(52, 63, (120, 120, 120)) or pyautogui.pixelMatchesColor(1338, 409, (7, 9, 12)):

                    redvida()
                    quase = quase + 1
                    print('O total de quase mortes foi:', quase)
                    sair = 1

                #SE TIVER ALGUEM DO LADO (protec player)
                if battleplayer == 45:
                    print('sistema entrou no protec player, a contagem parou em', battleplayer)
                    break

    #VOLTAR AO COMEÇO (UTILIZA POR CONTA DO 'FOR')
    if sair == 1:
        continue
    else:
        pass

    #ESPERA CD NA VOLTA
    cd = 1

    #PESCA 1
    pyautogui.moveTo(x=346, y=582)
    pyautogui.click()

    #LAGO
    #LISTA SQMs LAGO
    lagolista = [lago1, lago2]
    #JOGA ALEATORIAMENTE EM EM SQM DA LSITA
    random.choice(lagolista)()

     #CHECAGEM BATTLE YELLOW LIFE 2
    if pyautogui.pixelMatchesColor(1183, 445, (7, 9, 12)):

        pass
    
    else:

        #VERIFICAÇAO RED & YELLOW LIFE
        if pyautogui.pixelMatchesColor(117, 60, (158, 91, 78)) or pyautogui.pixelMatchesColor(117, 60, (142, 150, 74)) or pyautogui.pixelMatchesColor(52, 63, (120, 120, 120)) or pyautogui.pixelMatchesColor(1338, 409, (7, 9, 12)):

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
            pyautogui.write('TEXTO')
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

    #CHECAGEM BATTLE YELLOW LIFE 3
    if pyautogui.pixelMatchesColor(1183, 445, (7, 9, 12)):

        pass
    
    else:

        #VERIFICAÇAO RED & YELLOW LIFE
        if pyautogui.pixelMatchesColor(117, 60, (158, 91, 78)) or pyautogui.pixelMatchesColor(117, 60, (142, 150, 74)) or pyautogui.pixelMatchesColor(52, 63, (120, 120, 120)) or pyautogui.pixelMatchesColor(1338, 409, (7, 9, 12)):

            redvida()
            quase = quase + 1
            print('O total de quase mortes foi:', quase)
            continue

    #CICLO CHECAGEM POSIÇÃO POKE
    for posi in range(0, 2):

        #CHECAGEM POKE POSIÇÃO
        if pyautogui.pixelMatchesColor(678, 222, (215, 193, 3)) or pyautogui.pixelMatchesColor(681, 222, (75, 38, 13)) or pyautogui.pixelMatchesColor(691, 222, (179, 152, 6)):

            pass
        
        else:

            #MID POKE
            pyautogui.moveTo(x=681, y=241)
            pyautogui.middleClick()
            time.sleep(2)

            #PARE-MID
            pyautogui.moveTo(x=133, y=83)
            pyautogui.click()
            
            #MIRA POKE SUL
            pydirectinput.keyDown('ctrl')
            pydirectinput.keyDown('down')
            pydirectinput.keyUp('ctrl')
            pydirectinput.keyUp('down')      


    #FOME POKEMON
    if pyautogui.pixelMatchesColor(175, 84, (203, 98, 79)):

        #CLICA NA PIZZA
        pyautogui.moveTo(x=809, y=585)
        pyautogui.click() 
    
    
    
    #chat 3
    if chat == 2:

        if pyautogui.pixelMatchesColor(242, 682, (212, 212, 1)) or pyautogui.pixelMatchesColor(243, 676, (246, 246, 0)):
            
            #CLICAR NO ICONE POKEBATTLE 1
            pyautogui.moveTo(x=1256, y=387)
            pyautogui.click()

            #CLICAR NO ICONE PLAYER BATTLE 1
            pyautogui.moveTo(x=1185, y=384)
            pyautogui.click()

            #CHECAGEM PLAYER
            if pyautogui.pixelMatchesColor(1183, 445, (7, 9, 12)):

                sc = pyautogui.screenshot()
                sc.save('era-chat3.png')

                #LIMPANDO CHAT
                pyautogui.moveTo(x=1083, y=631)
                pyautogui.click()

                #CLICAR NO ICONE PLAYER BATTLE 1
                pyautogui.moveTo(x=1185, y=384)
                pyautogui.click()

                #CLICAR NO ICONE POKEBATTLE 1
                pyautogui.moveTo(x=1256, y=387)
                pyautogui.click()

            else:

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

                #CLICAR NO ICONE PLAYER BATTLE 1
                pyautogui.moveTo(x=1185, y=384)
                pyautogui.click()

                #CLICAR NO ICONE POKEBATTLE 1
                pyautogui.moveTo(x=1256, y=387)
                pyautogui.click()

                chat = 3


    #CHAT 2
    if chat == 1:

        if pyautogui.pixelMatchesColor(242, 682, (212, 212, 1)) or pyautogui.pixelMatchesColor(243, 676, (246, 246, 0)):
            
            #CLICAR NO ICONE POKEBATTLE 1
            pyautogui.moveTo(x=1256, y=387)
            pyautogui.click()

            #CLICAR NO ICONE PLAYER BATTLE 1
            pyautogui.moveTo(x=1185, y=384)
            pyautogui.click()

            #CHECAGEM PLAYER
            if pyautogui.pixelMatchesColor(1183, 445, (7, 9, 12)):

                sc = pyautogui.screenshot()
                sc.save('era-chat2.png')

                #LIMPANDO CHAT
                pyautogui.moveTo(x=1083, y=631)
                pyautogui.click()

                #CLICAR NO ICONE PLAYER BATTLE 1
                pyautogui.moveTo(x=1185, y=384)
                pyautogui.click()

                #CLICAR NO ICONE POKEBATTLE 1
                pyautogui.moveTo(x=1256, y=387)
                pyautogui.click()

            else:

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

                #CLICAR NO ICONE PLAYER BATTLE 1
                pyautogui.moveTo(x=1185, y=384)
                pyautogui.click()

                #CLICAR NO ICONE POKEBATTLE 1
                pyautogui.moveTo(x=1256, y=387)
                pyautogui.click()

                #ATIVA CHAT 3
                chat = 2


    #CHAT 1
    if chat == 0:

        if pyautogui.pixelMatchesColor(242, 682, (212, 212, 1)) or pyautogui.pixelMatchesColor(243, 676, (246, 246, 0)):
            
            #CLICAR NO ICONE POKEBATTLE 1
            pyautogui.moveTo(x=1256, y=387)
            pyautogui.click()

            #CLICAR NO ICONE PLAYER BATTLE 1
            pyautogui.moveTo(x=1185, y=384)
            pyautogui.click()

            #CHECAGEM PLAYER
            if pyautogui.pixelMatchesColor(1183, 445, (7, 9, 12)):

                sc = pyautogui.screenshot()
                sc.save('era-chat1.png')

                #LIMPANDO CHAT
                pyautogui.moveTo(x=1083, y=631)
                pyautogui.click()

                #CLICAR NO ICONE PLAYER BATTLE 1
                pyautogui.moveTo(x=1185, y=384)
                pyautogui.click()

                #CLICAR NO ICONE POKEBATTLE 1
                pyautogui.moveTo(x=1256, y=387)
                pyautogui.click()

            else:

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

                #CLICAR NO ICONE PLAYER BATTLE 1
                pyautogui.moveTo(x=1185, y=384)
                pyautogui.click()

                #CLICAR NO ICONE POKEBATTLE 1
                pyautogui.moveTo(x=1256, y=387)
                pyautogui.click()

                #DESATIVA PROTEÇÃO PLAER BATTLE
                pl = 4

                #ATIVA CHAT 2
                chat = 1
    


    #ESPERA SAIR MENSAGEM
    time.sleep(4)

    #CHECAGEM PESCA LAGO
    if pyautogui.pixelMatchesColor(680, 258, (188, 91, 53)) or pyautogui.pixelMatchesColor(649, 271, (107, 47, 28)) or pyautogui.pixelMatchesColor(660, 279, (85, 38, 22)):

        pass

    else:

        #INFORMA O ERRO
        print('PESCA FALHOU')

        #CAPTURA TELA
        sc = pyautogui.screenshot()
        sc.save('failpesca.png')

        #REMOVE PESCA BUGADA
        pyautogui.moveTo(7, 31)
        pyautogui.click()

        #VOLTA NO INICIO
        continue


    #ESPERA TEMPO PESCA
    time.sleep(22)
    
    
    #VERIFICAÇAO RED LIFE
    if pyautogui.pixelMatchesColor(117, 60, (158, 91, 78)) or pyautogui.pixelMatchesColor(52, 63, (120, 120, 120)) or pyautogui.pixelMatchesColor(1338, 409, (7, 9, 12)):

        redvida()

        quase = quase + 1
        print('O total de quase mortes foi:', quase)

        continue

    else:

        pass

    
    #chat 3
    if chat == 2:

        if pyautogui.pixelMatchesColor(242, 682, (212, 212, 1)) or pyautogui.pixelMatchesColor(243, 676, (246, 246, 0)):
            
            #CLICAR NO ICONE POKEBATTLE 1
            pyautogui.moveTo(x=1256, y=387)
            pyautogui.click()

            #CLICAR NO ICONE PLAYER BATTLE 1
            pyautogui.moveTo(x=1185, y=384)
            pyautogui.click()

            #CHECAGEM PLAYER
            if pyautogui.pixelMatchesColor(1183, 445, (7, 9, 12)):

                sc = pyautogui.screenshot()
                sc.save('era-chat3.png')

                #LIMPANDO CHAT
                pyautogui.moveTo(x=1083, y=631)
                pyautogui.click()

                #CLICAR NO ICONE PLAYER BATTLE 1
                pyautogui.moveTo(x=1185, y=384)
                pyautogui.click()

                #CLICAR NO ICONE POKEBATTLE 1
                pyautogui.moveTo(x=1256, y=387)
                pyautogui.click()

            else:

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

                #CLICAR NO ICONE PLAYER BATTLE 1
                pyautogui.moveTo(x=1185, y=384)
                pyautogui.click()

                #CLICAR NO ICONE POKEBATTLE 1
                pyautogui.moveTo(x=1256, y=387)
                pyautogui.click()

                chat = 3


    #CHAT 2
    if chat == 1:

        if pyautogui.pixelMatchesColor(242, 682, (212, 212, 1)) or pyautogui.pixelMatchesColor(243, 676, (246, 246, 0)):
            
            #CLICAR NO ICONE POKEBATTLE 1
            pyautogui.moveTo(x=1256, y=387)
            pyautogui.click()

            #CLICAR NO ICONE PLAYER BATTLE 1
            pyautogui.moveTo(x=1185, y=384)
            pyautogui.click()

            #CHECAGEM PLAYER
            if pyautogui.pixelMatchesColor(1183, 445, (7, 9, 12)):

                sc = pyautogui.screenshot()
                sc.save('era-chat2.png')

                #LIMPANDO CHAT
                pyautogui.moveTo(x=1083, y=631)
                pyautogui.click()

                #CLICAR NO ICONE PLAYER BATTLE 1
                pyautogui.moveTo(x=1185, y=384)
                pyautogui.click()

                #CLICAR NO ICONE POKEBATTLE 1
                pyautogui.moveTo(x=1256, y=387)
                pyautogui.click()

            else:

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

                #CLICAR NO ICONE PLAYER BATTLE 1
                pyautogui.moveTo(x=1185, y=384)
                pyautogui.click()

                #CLICAR NO ICONE POKEBATTLE 1
                pyautogui.moveTo(x=1256, y=387)
                pyautogui.click()

                #ATIVA CHAT 3
                chat = 2


    #CHAT 1
    if chat == 0:

        if pyautogui.pixelMatchesColor(242, 682, (212, 212, 1)) or pyautogui.pixelMatchesColor(243, 676, (246, 246, 0)):
            
            #CLICAR NO ICONE POKEBATTLE 1
            pyautogui.moveTo(x=1256, y=387)
            pyautogui.click()

            #CLICAR NO ICONE PLAYER BATTLE 1
            pyautogui.moveTo(x=1185, y=384)
            pyautogui.click()

            #CHECAGEM PLAYER
            if pyautogui.pixelMatchesColor(1183, 445, (7, 9, 12)):

                sc = pyautogui.screenshot()
                sc.save('era-chat1.png')

                #LIMPANDO CHAT
                pyautogui.moveTo(x=1083, y=631)
                pyautogui.click()

                #CLICAR NO ICONE PLAYER BATTLE 1
                pyautogui.moveTo(x=1185, y=384)
                pyautogui.click()

                #CLICAR NO ICONE POKEBATTLE 1
                pyautogui.moveTo(x=1256, y=387)
                pyautogui.click()

            else:

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

                #CLICAR NO ICONE PLAYER BATTLE 1
                pyautogui.moveTo(x=1185, y=384)
                pyautogui.click()

                #CLICAR NO ICONE POKEBATTLE 1
                pyautogui.moveTo(x=1256, y=387)
                pyautogui.click()

                #DESATIVA PROTEÇÃO PLAER BATTLE
                pl = 4

                #ATIVA CHAT 2
                chat = 1
    

    #ESPERA CD 2
    while pyautogui.pixelMatchesColor(784, 506, (31, 38, 47)) or pyautogui.pixelMatchesColor(784, 523, (68, 67, 5)):

        time.sleep(1.5)


    #PESCA 2
    pyautogui.moveTo(x=346, y=582)
    pyautogui.click()

    #5 - ELETRICFY
    time.sleep(1)
    pyautogui.moveTo(x=722, y=512)
    pyautogui.click()

    #VERIFICAÇÃO SHINY
    for sh in range(0, 3):

        #CHECAGEM SHINY
        if pyautogui.pixelMatchesColor(1185, 447, (128, 127, 115)) or pyautogui.pixelMatchesColor(1183, 447, (210, 211, 203)):

            print('------'*5)
            shiny = shiny + 1
            print('O total de shinys que apareceram eh:', shiny)
            print('------'*5)
            redvida()
            sair = 1


    #VOLTAR AO COMEÇO CASO APARECER UM SHINY (UTILIZA POR CONTA DO 'FOR')
    if sair == 1:
        continue
    
    #ATTACKs

    #6 - DISCHARGE
    time.sleep(1)
    pyautogui.moveTo(x=759, y=515)
    pyautogui.click()

    #7 - MAMARAGAN
    time.sleep(1)
    pyautogui.moveTo(x=796, y=512)
    pyautogui.click()

    #4 - THUNDER WRATH
    time.sleep(1)
    pyautogui.moveTo(x=688, y=516)
    pyautogui.click()

    #VERIFICAÇAO RED LIFE
    if pyautogui.pixelMatchesColor(117, 60, (158, 91, 78)) or pyautogui.pixelMatchesColor(52, 63, (120, 120, 120)) or pyautogui.pixelMatchesColor(1338, 409, (7, 9, 12)):

        redvida()

        quase = quase + 1
        print('O total de quase mortes foi:', quase)

        continue

    time.sleep(1)

    #VOID ATTACK OR NOT 1
    if pyautogui.pixelMatchesColor(1182, 445, (7, 9, 12)):

        pass
    
    else:

        #BATTLE 1
        time.sleep(0.5)
        pyautogui.moveTo(x=1183, y=445)
        pyautogui.click()

        #3 - THUNDER PUNCH
        pyautogui.moveTo(x=616, y=511)
        pyautogui.click()


    #VERIFICAÇAO RED LIFE
    if pyautogui.pixelMatchesColor(117, 60, (158, 91, 78)) or pyautogui.pixelMatchesColor(52, 63, (120, 120, 120)) or pyautogui.pixelMatchesColor(1338, 409, (7, 9, 12)):

        redvida()

        quase = quase + 1
        print('O total de quase mortes foi:', quase)

        continue

    else:

        pass

    #VOID ATTACK OR NOT 2
    if pyautogui.pixelMatchesColor(1182, 445, (7, 9, 12)):

        pass
    
    else:

        #BATTLE 1
        time.sleep(0.5)
        pyautogui.moveTo(x=1183, y=445)
        pyautogui.click()
        
        #3 - THUNDER BOLT
        pyautogui.moveTo(x=651, y=512)
        pyautogui.click()


    #VERIFICAÇAO RED LIFE
    if pyautogui.pixelMatchesColor(117, 60, (158, 91, 78)) or pyautogui.pixelMatchesColor(52, 63, (120, 120, 120)) or pyautogui.pixelMatchesColor(1338, 409, (7, 9, 12)):

        redvida()

        quase = quase + 1
        print('O total de quase mortes foi:', quase)

        continue

    else:

        pass

    #VOID ATTACK OR NOT 3
    if pyautogui.pixelMatchesColor(1182, 445, (7, 9, 12)):

        pass
    
    else:

        #BATTLE 1
        time.sleep(0.5)
        pyautogui.moveTo(x=1183, y=445)
        pyautogui.click()
        
        #1 - LOW KICK
        pyautogui.moveTo(x=578, y=512)
        pyautogui.click()


    #VERIFICAÇAO RED LIFE
    if pyautogui.pixelMatchesColor(117, 60, (158, 91, 78)) or pyautogui.pixelMatchesColor(52, 63, (120, 120, 120)) or pyautogui.pixelMatchesColor(1338, 409, (7, 9, 12)):

        redvida()

        quase = quase + 1
        print('O total de quase mortes foi:', quase)

        continue

    else:

        pass

     #chat 3
    if chat == 2:

        if pyautogui.pixelMatchesColor(242, 682, (212, 212, 1)) or pyautogui.pixelMatchesColor(243, 676, (246, 246, 0)):
            
            #CLICAR NO ICONE POKEBATTLE 1
            pyautogui.moveTo(x=1256, y=387)
            pyautogui.click()

            #CLICAR NO ICONE PLAYER BATTLE 1
            pyautogui.moveTo(x=1185, y=384)
            pyautogui.click()

            #CHECAGEM PLAYER
            if pyautogui.pixelMatchesColor(1183, 445, (7, 9, 12)):

                sc = pyautogui.screenshot()
                sc.save('era-chat3.png')

                #LIMPANDO CHAT
                pyautogui.moveTo(x=1083, y=631)
                pyautogui.click()

                #CLICAR NO ICONE PLAYER BATTLE 1
                pyautogui.moveTo(x=1185, y=384)
                pyautogui.click()

                #CLICAR NO ICONE POKEBATTLE 1
                pyautogui.moveTo(x=1256, y=387)
                pyautogui.click()

            else:

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

                #CLICAR NO ICONE PLAYER BATTLE 1
                pyautogui.moveTo(x=1185, y=384)
                pyautogui.click()

                #CLICAR NO ICONE POKEBATTLE 1
                pyautogui.moveTo(x=1256, y=387)
                pyautogui.click()

                chat = 3


    #CHAT 2
    if chat == 1:

        if pyautogui.pixelMatchesColor(242, 682, (212, 212, 1)) or pyautogui.pixelMatchesColor(243, 676, (246, 246, 0)):
            
            #CLICAR NO ICONE POKEBATTLE 1
            pyautogui.moveTo(x=1256, y=387)
            pyautogui.click()

            #CLICAR NO ICONE PLAYER BATTLE 1
            pyautogui.moveTo(x=1185, y=384)
            pyautogui.click()

            #CHECAGEM PLAYER
            if pyautogui.pixelMatchesColor(1183, 445, (7, 9, 12)):

                sc = pyautogui.screenshot()
                sc.save('era-chat2.png')

                #LIMPANDO CHAT
                pyautogui.moveTo(x=1083, y=631)
                pyautogui.click()

                #CLICAR NO ICONE PLAYER BATTLE 1
                pyautogui.moveTo(x=1185, y=384)
                pyautogui.click()

                #CLICAR NO ICONE POKEBATTLE 1
                pyautogui.moveTo(x=1256, y=387)
                pyautogui.click()

            else:

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

                #CLICAR NO ICONE PLAYER BATTLE 1
                pyautogui.moveTo(x=1185, y=384)
                pyautogui.click()

                #CLICAR NO ICONE POKEBATTLE 1
                pyautogui.moveTo(x=1256, y=387)
                pyautogui.click()

                #ATIVA CHAT 3
                chat = 2


    #CHAT 1
    if chat == 0:

        if pyautogui.pixelMatchesColor(242, 682, (212, 212, 1)) or pyautogui.pixelMatchesColor(243, 676, (246, 246, 0)):
            
            #CLICAR NO ICONE POKEBATTLE 1
            pyautogui.moveTo(x=1256, y=387)
            pyautogui.click()

            #CLICAR NO ICONE PLAYER BATTLE 1
            pyautogui.moveTo(x=1185, y=384)
            pyautogui.click()

            #CHECAGEM PLAYER
            if pyautogui.pixelMatchesColor(1183, 445, (7, 9, 12)):

                sc = pyautogui.screenshot()
                sc.save('era-chat1.png')

                #LIMPANDO CHAT
                pyautogui.moveTo(x=1083, y=631)
                pyautogui.click()

                #CLICAR NO ICONE PLAYER BATTLE 1
                pyautogui.moveTo(x=1185, y=384)
                pyautogui.click()

                #CLICAR NO ICONE POKEBATTLE 1
                pyautogui.moveTo(x=1256, y=387)
                pyautogui.click()

            else:

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

                #CLICAR NO ICONE PLAYER BATTLE 1
                pyautogui.moveTo(x=1185, y=384)
                pyautogui.click()

                #CLICAR NO ICONE POKEBATTLE 1
                pyautogui.moveTo(x=1256, y=387)
                pyautogui.click()

                #DESATIVA PROTEÇÃO PLAER BATTLE
                pl = 4

                #ATIVA CHAT 2
                chat = 1
        
        
    #chat 6 FINAL
    if chat == 5:

        if pyautogui.pixelMatchesColor(242, 682, (212, 212, 1)) or pyautogui.pixelMatchesColor(243, 676, (246, 246, 0)):
            
            #CLICAR NO ICONE POKEBATTLE 1
            pyautogui.moveTo(x=1256, y=387)
            pyautogui.click()

            #CLICAR NO ICONE PLAYER BATTLE 1
            pyautogui.moveTo(x=1185, y=384)
            pyautogui.click()

            #CHECAGEM PLAYER
            if pyautogui.pixelMatchesColor(1183, 445, (7, 9, 12)):

                sc = pyautogui.screenshot()
                sc.save('era-chat6.png')

                #LIMPANDO CHAT
                pyautogui.moveTo(x=1083, y=631)
                pyautogui.click()

                #CLICAR NO ICONE PLAYER BATTLE 1
                pyautogui.moveTo(x=1185, y=384)
                pyautogui.click()

                #CLICAR NO ICONE POKEBATTLE 1
                pyautogui.moveTo(x=1256, y=387)
                pyautogui.click()

            else:

                #Clica local chat
                pyautogui.moveTo(x=313, y=704)
                pyautogui.click()

                #Escreve no chat
                pyautogui.write('TEXTO')
                pydirectinput.keyDown('enter')
                pydirectinput.keyUp('enter')

                sc = pyautogui.screenshot()
                sc.save('chat6.png')

                #LIMPANDO CHAT
                pyautogui.moveTo(x=1083, y=631)
                pyautogui.click()

                #CLICAR NO ICONE PLAYER BATTLE 1
                pyautogui.moveTo(x=1185, y=384)
                pyautogui.click()

                #CLICAR NO ICONE POKEBATTLE 1
                pyautogui.moveTo(x=1256, y=387)
                pyautogui.click()

                #ativa chat 5
                chat = 4


    #chat 5 
    if chat == 4:

        if pyautogui.pixelMatchesColor(242, 682, (212, 212, 1)) or pyautogui.pixelMatchesColor(243, 676, (246, 246, 0)):
            
            #CLICAR NO ICONE POKEBATTLE 1
            pyautogui.moveTo(x=1256, y=387)
            pyautogui.click()

            #CLICAR NO ICONE PLAYER BATTLE 1
            pyautogui.moveTo(x=1185, y=384)
            pyautogui.click()

            #CHECAGEM PLAYER
            if pyautogui.pixelMatchesColor(1183, 445, (7, 9, 12)):

                sc = pyautogui.screenshot()
                sc.save('era-chat5.png')

                #LIMPANDO CHAT
                pyautogui.moveTo(x=1083, y=631)
                pyautogui.click()

                #CLICAR NO ICONE PLAYER BATTLE 1
                pyautogui.moveTo(x=1185, y=384)
                pyautogui.click()

                #CLICAR NO ICONE POKEBATTLE 1
                pyautogui.moveTo(x=1256, y=387)
                pyautogui.click()

            else:

                #Clica local chat
                pyautogui.moveTo(x=313, y=704)
                pyautogui.click()

                #Escreve no chat
                pyautogui.write('TEXTO')
                pydirectinput.keyDown('enter')
                pydirectinput.keyUp('enter')

                #ATIVA CHAT 6
                chat = 5

                sc = pyautogui.screenshot()
                sc.save('chat5.png')

                #LIMPANDO CHAT
                pyautogui.moveTo(x=1083, y=631)
                pyautogui.click()

                #CLICAR NO ICONE PLAYER BATTLE 1
                pyautogui.moveTo(x=1185, y=384)
                pyautogui.click()

                #CLICAR NO ICONE POKEBATTLE 1
                pyautogui.moveTo(x=1256, y=387)
                pyautogui.click()


    #chat 4 SEMI FINAL
    if chat == 3:

        if pyautogui.pixelMatchesColor(242, 682, (212, 212, 1)) or pyautogui.pixelMatchesColor(243, 676, (246, 246, 0)):
            
            #CLICAR NO ICONE POKEBATTLE 1
            pyautogui.moveTo(x=1256, y=387)
            pyautogui.click()

            #CLICAR NO ICONE PLAYER BATTLE 1
            pyautogui.moveTo(x=1185, y=384)
            pyautogui.click()

            #CHECAGEM PLAYER
            if pyautogui.pixelMatchesColor(1183, 445, (7, 9, 12)):

                sc = pyautogui.screenshot()
                sc.save('era-chat4.png')

                #LIMPANDO CHAT
                pyautogui.moveTo(x=1083, y=631)
                pyautogui.click()

                #CLICAR NO ICONE PLAYER BATTLE 1
                pyautogui.moveTo(x=1185, y=384)
                pyautogui.click()

                #CLICAR NO ICONE POKEBATTLE 1
                pyautogui.moveTo(x=1256, y=387)
                pyautogui.click()

            else:

                #Clica local chat
                pyautogui.moveTo(x=313, y=704)
                pyautogui.click()

                #Escreve no chat
                pyautogui.write('TEXTO')
                pydirectinput.keyDown('enter')
                pydirectinput.keyUp('enter')

                sc = pyautogui.screenshot()
                sc.save('chat4.png')

                #ATIVA CHAT 5
                chat = 4

                #LIMPANDO CHAT
                pyautogui.moveTo(x=1083, y=631)
                pyautogui.click()

                #CLICAR NO ICONE PLAYER BATTLE 1
                pyautogui.moveTo(x=1185, y=384)
                pyautogui.click()

                #CLICAR NO ICONE POKEBATTLE 1
                pyautogui.moveTo(x=1256, y=387)
                pyautogui.click()

                #INICAR FUNÇÃO SAIR JOGO
                sairjogo()


    #VERIFICAÇAO RED LIFE
    if pyautogui.pixelMatchesColor(117, 60, (158, 91, 78)) or pyautogui.pixelMatchesColor(52, 63, (120, 120, 120)) or pyautogui.pixelMatchesColor(1338, 409, (7, 9, 12)):

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
        
        #35 - espera entrar server
        time.sleep(35)

        #CHECAGEM BOTÃO VERMELHO
        if pyautogui.pixelMatchesColor(777, 478, (171, 51, 26)):

            #CLICAR BOTÃO CANCELAR
            pyautogui.moveTo(793, 476)
            pyautogui.click()

            #MINIMIZA
            pyautogui.moveTo(x=1242, y=14)
            time.sleep(1.5)
            pyautogui.click()

            #CAPTURA A TELA
            sc = pyautogui.screenshot()
            sc.save('ver1problem.png')

            print('PROBLEMA NET OU SERVER')

            exit()
    
        #CHECAGEM BALDE DE LIXO ESQUERDO
        if pyautogui.pixelMatchesColor(456, 460, (130, 61, 36)):

            #CLICAR ELECTABUZ
            pyautogui.moveTo('electa.png')
            pyautogui.click()

            #COLOCAR ISCA ESPECIAL
            pyautogui.moveTo(x=1000, y=585)
            pyautogui.click()
        
        else:

            #SAIR JOGO
            pyautogui.moveTo(x=1342, y=12)
            pyautogui.click()

            time.sleep(1)

            #CLICAR SIM SAIR JOGO
            pyautogui.moveTo(x=569, y=409)
            pyautogui.click()

            #CAPTURA A TELA
            sc = pyautogui.screenshot()
            sc.save('ver2problem.png')

            print('NÃO ESTÁ NA POSIÇÃO CORRETA')

            exit()

