import pyautogui
import random
import time
import pydirectinput

#SCRIPT WINDOWS
#SCRIPT LVL 120+ COM SH VILE

#ROBO COM SHINY VILEPLUME SEM ISCA

#CODIGO QUE DERROTA O SHINY GIANT MAGIKARP E JOGA BALL NELE
#LUGAR: CHAT ME

#IR PARA PXG
pyautogui.keyDown('alt')

pyautogui.press('tab')

pyautogui.keyUp('alt')

#VARIAVEL CONTAGEM QUASE MORTES
quase = 0
#VARIAVEL CONTAGEM SHINY
shiny = 0
#VARIAVEL CHAT
chat = 0
#VARIAVEL PLAYER
pl = 0
#VARIVEL ESPERA CD
cd = 0
#VARIAVEL PESCA
fish = 0
#AJUDA PESCA
fishz = 0
#REGIÃO MINI GAME PEIXE
REGION = (650, 336, 45, 356)

#FUNÇÃO PEGA LOOT
def loot():

    #LOOT
    pydirectinput.keyDown('e')
    time.sleep(0.3)
    pydirectinput.keyUp('e')


#FUNÇÃO VIDA BAIXA
def redvida():

    global sair

    #subir escada
    pydirectinput.keyDown('ctrl')
    pyautogui.moveTo(x=679, y=130)
    pyautogui.rightClick()
    time.sleep(0.5)
    pyautogui.moveTo(x=694, y=169)
    pyautogui.click()
    pydirectinput.keyUp('ctrl')

    sair = 0

    time.sleep(4)

    #SE O POKE MORRER
    if pyautogui.pixelMatchesColor(52, 63, (120, 120, 120)) or pyautogui.pixelMatchesColor(1338, 409, (7, 9, 12)):

        sair = 1

        print('ENTROU DEAD POKE REDVIDA')

        #SELECIONAR REVIVE
        pyautogui.moveTo(x=771, y=581)
        pyautogui.click()

        #MOVER PARA O SH VILE
        pyautogui.moveTo(x=35, y=50)
        pyautogui.click()
        
        time.sleep(1)

        #MOVER MOUSE PARA NÃO BUGAR
        pyautogui.moveTo(x=730, y=239)

        time.sleep(1)

        #CLICAR VILEPLUME
        pyautogui.moveTo('vilepoke.png')
        pyautogui.click()

        #descer escada
        pyautogui.moveTo(x=681, y=236)
        pyautogui.click()

        time.sleep(1.5)

        #IR POSIÇÃO
        pyautogui.moveTo(x=676, y=421)
        pyautogui.click()

        time.sleep(3.5)


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
        pyautogui.moveTo(x=676, y=421)
        pyautogui.click()

        time.sleep(3)


#FUNÇÃO SAIR JOGO CHAT
def sairjogo():

    #subir escada
    pydirectinput.keyDown('ctrl')
    pyautogui.moveTo(x=679, y=130)
    pyautogui.rightClick()
    time.sleep(0.5)
    pyautogui.moveTo(x=694, y=169)
    pyautogui.click()
    pydirectinput.keyUp('ctrl')

    #IR MENU
    pyautogui.moveTo(x=683, y=35)
    pyautogui.click()

    time.sleep(3)

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

        exit()

    #descer escada
    pyautogui.moveTo(x=681, y=236)
    pyautogui.click()

    time.sleep(1)

    #IR POSIÇÃO
    pyautogui.moveTo(x=676, y=421)
    pyautogui.click()

    time.sleep(3)

    #CLICAR VILEPLUME
    pyautogui.moveTo('vilepoke.png')
    pyautogui.click()


#FUNÇÃO VOLTAR PXG QND CAIR NET
def caiunet():

    #CAPTURAR A TELA
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

        print('PROBLEMA NET OU SERVER')

        exit()

    #CHECAGEM COR X LADO DIREITO
    if pyautogui.pixelMatchesColor(958, 254, (106, 106, 105)):

        #CLICAR VILEPLUME
        pyautogui.moveTo('vilepoke.png')
        pyautogui.click()
    
    else:

        #CAPTURA A TELA ERRO NET
        sc = pyautogui.screenshot()
        sc.save('fimbotnet-ou-dead.png')

        #SAIR JOGO
        pyautogui.moveTo(x=1342, y=12)
        pyautogui.click()

        time.sleep(1)

        #CLICAR SIM SAIR JOGO
        pyautogui.moveTo(x=569, y=409)
        pyautogui.click()

        print('SAIU DO JOGO')

        exit()


#FUNÇAO CHAT
def resposta():

    global chat
    global x
    global y
    global pessoa
    global pl
    global pessoa2
    global pessoa3
    global pessoa4
    global pessoa5
    global pessoa6

    #chat 3
    if chat == 2:

        if pyautogui.pixelMatchesColor(242, 682, (212, 212, 1)) or pyautogui.pixelMatchesColor(243, 676, (246, 246, 0)):
            
            #CLICAR NO ICONE POKEBATTLE 1
            pyautogui.moveTo(x=1256, y=387)
            pyautogui.click()

            #CLICAR NO ICONE PLAYER BATTLE 1
            pyautogui.moveTo(x=1185, y=384)
            pyautogui.click()

            time.sleep(1)

            x, y = 1184, 443
            pessoa3 = pyautogui.pixel (x,y)

            #CHECAGEM PLAYER
            if pessoa == pessoa4:

                #Clica local chat
                pyautogui.moveTo(x=313, y=704)
                pyautogui.click()

                sc = pyautogui.screenshot()
                sc.save('chat3.png')

                #Escreve no chat
                pyautogui.write('TEXTO')
                pydirectinput.keyDown('enter')
                pydirectinput.keyUp('enter')

                time.sleep(3.5)

                #Clica local chat
                pyautogui.moveTo(x=313, y=704)
                pyautogui.click()

                #Escreve no chat
                pyautogui.write('TEXTO')
                pydirectinput.keyDown('enter')
                pydirectinput.keyUp('enter')

                #LIMPANDO CHAT
                pyautogui.moveTo(x=1083, y=631)
                pyautogui.click()

                #CLICAR NO ICONE PLAYER BATTLE 1
                pyautogui.moveTo(x=1185, y=384)
                pyautogui.click()

                #CLICAR NO ICONE POKEBATTLE 1
                pyautogui.moveTo(x=1256, y=387)
                pyautogui.click()

                #ATIVA CHAT 4
                chat = 3

            else:

                #CLICAR NO ICONE PLAYER BATTLE 1
                pyautogui.moveTo(x=1185, y=384)
                pyautogui.click()

                #CLICAR NO ICONE POKEBATTLE 1
                pyautogui.moveTo(x=1256, y=387)
                pyautogui.click()
                
                #SE NAO FOR O MESMO PLAYER NA TELA ELE VOLTA A FUNCAO CHAT
                chat = 0
                resposta()

            
    #CHAT 2
    if chat == 1:

        if pyautogui.pixelMatchesColor(242, 682, (212, 212, 1)) or pyautogui.pixelMatchesColor(243, 676, (246, 246, 0)):
            
            #CLICAR NO ICONE POKEBATTLE 1
            pyautogui.moveTo(x=1256, y=387)
            pyautogui.click()

            #CLICAR NO ICONE PLAYER BATTLE 1
            pyautogui.moveTo(x=1185, y=384)
            pyautogui.click()

            time.sleep(1)

            x, y = 1184, 443
            pessoa2 = pyautogui.pixel (x,y)

            #CHECAGEM PLAYER
            if pessoa == pessoa2:

                sc = pyautogui.screenshot()
                sc.save('chat2.png')

                #Clica local chat
                pyautogui.moveTo(x=313, y=704)
                pyautogui.click()

                #Escreve no chat
                pyautogui.write('TEXTO')
                pydirectinput.keyDown('enter')
                pydirectinput.keyUp('enter')

                time.sleep(3.5)

                #Clica local chat
                pyautogui.moveTo(x=313, y=704)
                pyautogui.click()

                #Escreve no chat
                pyautogui.write('TEXTO')
                pydirectinput.keyDown('enter')
                pydirectinput.keyUp('enter')

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

            else:

                #CLICAR NO ICONE PLAYER BATTLE 1
                pyautogui.moveTo(x=1185, y=384)
                pyautogui.click()

                #CLICAR NO ICONE POKEBATTLE 1
                pyautogui.moveTo(x=1256, y=387)
                pyautogui.click()
                
                #SE NAO FOR O MESMO PLAYER NA TELA ELE VOLTA A FUNCAO CHAT
                chat = 0
                resposta()


    #CHAT 1
    if chat == 0:

        #CHECA COR CHAT
        if pyautogui.pixelMatchesColor(242, 682, (212, 212, 1)) or pyautogui.pixelMatchesColor(243, 676, (246, 246, 0)):

            #CLICAR NO ICONE POKEBATTLE 1
            pyautogui.moveTo(x=1256, y=387)
            pyautogui.click()

            #CLICAR NO ICONE PLAYER BATTLE 1
            pyautogui.moveTo(x=1185, y=384)
            pyautogui.click()

            #ARMAZENA NA MEMORIA A COR DO PESONAGEM DA PESSOA NO BAT
            x, y = 1184, 443
            pessoa = pyautogui.pixel (x,y)

            #CHECAGEM PLAYER
            if pyautogui.pixel(x,y) == pessoa:

                sc = pyautogui.screenshot()
                sc.save('chat1.png')

                #Clica local chat
                pyautogui.moveTo(x=313, y=704)
                pyautogui.click()

                #Escreve no chat
                pyautogui.write('TEXTO')
                pydirectinput.keyDown('enter')
                pydirectinput.keyUp('enter')

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

                #ATIVA CHAT 2 (1)
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

            time.sleep(1)

            x, y = 1184, 443
            pessoa6 = pyautogui.pixel (x,y)

            #CHECAGEM PLAYER
            if pessoa == pessoa6:

                #Clica local chat
                pyautogui.moveTo(x=313, y=704)
                pyautogui.click()

                #print tela
                sc = pyautogui.screenshot()
                sc.save('chat6.png')
            
                #Escreve no chat
                pyautogui.write('TEXTO')
                pydirectinput.keyDown('enter')
                pydirectinput.keyUp('enter')

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

            else:

                #CLICAR NO ICONE PLAYER BATTLE 1
                pyautogui.moveTo(x=1185, y=384)
                pyautogui.click()

                #CLICAR NO ICONE POKEBATTLE 1
                pyautogui.moveTo(x=1256, y=387)
                pyautogui.click()
                
                #SE NAO FOR O MESMO PLAYER NA TELA ELE VOLTA A FUNCAO CHAT
                chat = 0
                resposta()


    #chat 5 
    if chat == 4:

        if pyautogui.pixelMatchesColor(242, 682, (212, 212, 1)) or pyautogui.pixelMatchesColor(243, 676, (246, 246, 0)):
            
            #CLICAR NO ICONE POKEBATTLE 1
            pyautogui.moveTo(x=1256, y=387)
            pyautogui.click()

            #CLICAR NO ICONE PLAYER BATTLE 1
            pyautogui.moveTo(x=1185, y=384)
            pyautogui.click()

            time.sleep(1)

            x, y = 1184, 443
            pessoa5 = pyautogui.pixel (x,y)

            #CHECAGEM PLAYER
            if pessoa == pessoa5:

                #Clica local chat
                pyautogui.moveTo(x=313, y=704)
                pyautogui.click()

                #print tela
                sc = pyautogui.screenshot()
                sc.save('chat5.png')

                #Escreve no chat
                pyautogui.write('TEXTO')
                pydirectinput.keyDown('enter')
                pydirectinput.keyUp('enter')

                #LIMPANDO CHAT
                pyautogui.moveTo(x=1083, y=631)
                pyautogui.click()

                #CLICAR NO ICONE PLAYER BATTLE 1
                pyautogui.moveTo(x=1185, y=384)
                pyautogui.click()

                #CLICAR NO ICONE POKEBATTLE 1
                pyautogui.moveTo(x=1256, y=387)
                pyautogui.click()

                #ATIVA CHAT 6 FINAL
                chat = 5

            else:

                #CLICAR NO ICONE PLAYER BATTLE 1
                pyautogui.moveTo(x=1185, y=384)
                pyautogui.click()

                #CLICAR NO ICONE POKEBATTLE 1
                pyautogui.moveTo(x=1256, y=387)
                pyautogui.click()
                
                #SE NAO FOR O MESMO PLAYER NA TELA ELE VOLTA A FUNCAO CHAT
                chat = 0
                resposta()


    #chat 4 SEMI FINAL
    if chat == 3:

        if pyautogui.pixelMatchesColor(242, 682, (212, 212, 1)) or pyautogui.pixelMatchesColor(243, 676, (246, 246, 0)):
            
            #CLICAR NO ICONE POKEBATTLE 1
            pyautogui.moveTo(x=1256, y=387)
            pyautogui.click()

            #CLICAR NO ICONE PLAYER BATTLE 1
            pyautogui.moveTo(x=1185, y=384)
            pyautogui.click()

            time.sleep(1)

            x, y = 1184, 443
            pessoa4 = pyautogui.pixel (x,y)

            #CHECAGEM PLAYER
            if pessoa == pessoa4:

                #Clica local chat
                pyautogui.moveTo(x=313, y=704)
                pyautogui.click()

                #print tela
                sc = pyautogui.screenshot()
                sc.save('chat4.png')

                #Escreve no chat
                pyautogui.write('TEXTO')
                pydirectinput.keyDown('enter')
                pydirectinput.keyUp('enter')

                #LIMPANDO CHAT
                pyautogui.moveTo(x=1083, y=631)
                pyautogui.click()

                #CLICAR NO ICONE PLAYER BATTLE 1
                pyautogui.moveTo(x=1185, y=384)
                pyautogui.click()

                #CLICAR NO ICONE POKEBATTLE 1
                pyautogui.moveTo(x=1256, y=387)
                pyautogui.click()

                #ATIVA CHAT 5
                chat = 4

                #INICAR FUNÇÃO SAIR JOGO
                sairjogo()

            else:

                #CLICAR NO ICONE PLAYER BATTLE 1
                pyautogui.moveTo(x=1185, y=384)
                pyautogui.click()

                #CLICAR NO ICONE POKEBATTLE 1
                pyautogui.moveTo(x=1256, y=387)
                pyautogui.click()
                
                #SE NAO FOR O MESMO PLAYER NA TELA ELE VOLTA A FUNCAO CHAT
                chat = 0
                resposta()


#FUNÇÃO LAGO 1
def lago1():

    #CHAMA O VALOR DA VARIAVEL PARA FUNÇÃO
    global fish
    #CHAMA VARIAVEL AJUDA PESCA
    global fishz

    #LAGO 1 POSI 1
    if fish == 3 and fishz == 0:

        pyautogui.moveTo(x=594, y=286)
        pyautogui.click()

        fish = fish + 1
        fishz = 1

    #LAGO 1 POSI 2
    if fish == 2 and fishz == 0:

        pyautogui.moveTo(x=592, y=326)
        pyautogui.click()

        fish = fish + 1
        fishz = 1

    #LAGO 1 POSI 3
    if fish == 1 and fishz == 0:

        pyautogui.moveTo(x=593, y=376)
        pyautogui.click()

        fish = fish + 1
        fishz = 1

    #LAGO 1 POSI 4
    if fish == 0 and fishz == 0:

        pyautogui.moveTo(x=592, y=418)
        pyautogui.click()

        fish = fish + 1
        fishz = 1

    #LAGO 1 POSI 5
    if fish == 4 and fishz == 0:

        pyautogui.moveTo(x=591, y=464)
        pyautogui.click()

        fish = 0
        fishz = 1


#FUNLÇÃO LAGO 2
def lago2():

    #CHAMA O VALOR DA VARIAVEL PARA FUNÇÃO
    global fish
    #CHAMA VARIAVEL AJUDA PESCA
    global fishz

    #LAGO 1 POSI 1
    if fish == 3 and fishz == 0:

        pyautogui.moveTo(x=679, y=372)
        pyautogui.click()

        fish = fish + 1
        fishz = 1

    #LAGO 1 POSI 2
    if fish == 2 and fishz == 0:

        pyautogui.moveTo(x=681, y=420)
        pyautogui.click()

        fish = fish + 1
        fishz = 1

    #LAGO 1 POSI 3
    if fish == 1 and fishz == 0:

        pyautogui.moveTo(x=685, y=468)
        pyautogui.click()

        fish = fish + 1
        fishz = 1

    #LAGO 1 POSI 4
    if fish == 0 and fishz == 0:

        pyautogui.moveTo(x=679, y=372)
        pyautogui.click()

        fish = fish + 1
        fishz = 1

    #LAGO 1 POSI 5
    if fish == 4 and fishz == 0:

        pyautogui.moveTo(x=685, y=468)
        pyautogui.click()

        fish = 0
        fishz = 1


time.sleep(1)

#COLOCAR ISCA GOLD
pyautogui.moveTo(x=887, y=586)
pyautogui.click()

#PARE-MID
pyautogui.moveTo(x=133, y=83)
pyautogui.click()

#CHECAGEM ISCA (CHECA FINAL FRASE)
if pyautogui.pixelMatchesColor(585, 679, (7, 7, 7)):

    #COLOCA ISCA GOLD
    pyautogui.moveTo(x=887, y=586)
    pyautogui.click()

else:

    pass

#CICLO PESCA, ATTACK, LOOT, FUGIR

while True:

    #SAIR DA PXG CASO CAIR NET OU DEAD, PUXA COR IGRENAGEM LADO DIREITO
    if pyautogui.pixelMatchesColor(1225, 87, (204, 204, 204)):

        caiunet()
        cd = 0
        continue

    #VARIAVEL VOLTA AO COMEÇO SHINY
    sair = 0
    #VARIAVAL PROTEC PLAYER
    battleplayer = 0
    #AJUDA PESCA
    fishz = 0

    #VERIFICAÇAO RED & YELLOW LIFE
    if pyautogui.pixelMatchesColor(117, 60, (158, 91, 78)) or pyautogui.pixelMatchesColor(117, 60, (142, 150, 74)) or pyautogui.pixelMatchesColor(52, 63, (120, 120, 120)) or pyautogui.pixelMatchesColor(1338, 409, (7, 9, 12)):

        redvida()
        quase = quase + 1
        print('O total de quase mortes foi:', quase)
        continue

    #LOOT GERAL
    loot()

    #PESCA 1
    pyautogui.moveTo(x=346, y=582)
    pyautogui.click()

    #LAGO
    #LISTA SQMs LAGO
    lagolista = [lago1, lago2]
    #JOGA ALEATORIAMENTE EM EM SQM DA LSITA
    random.choice(lagolista)()

    #ESPERA CD
    if cd == 1:
        
        #SE CONTIVER ALGO NA PRIMEIRA POSI NO BAT
        if pyautogui.pixelMatchesColor(1182, 445, (7, 9, 12)):

            #SE NAO TIVER NADA
            pass

        else:

            #SE TIVER POKE BAT
            
            #ENQUANTO TIVER UM POKEMON NO BATTLE ELE EXECUTA VERIFICAÇÃO REDLIFE
            while pyautogui.pixelMatchesColor(1182, 445, (7, 9, 12)) == False and pyautogui.pixelMatchesColor(1180, 474, (7, 9, 12)) == True:
                
                #ATACAR BAT 1
                if battleplayer == 0:

                    #CLICAR BATTLE 1
                    time.sleep(1)
                    pyautogui.moveTo(x=1183, y=445)
                    pyautogui.click()

                    #2 - SEED ABSORB
                    time.sleep(1)
                    pyautogui.moveTo(x=597, y=514)
                    pyautogui.click()


                #SOMATORIA VARIVEL PARA SAIR WHILE
                battleplayer = battleplayer + 1

                #VERIFICAÇAO RED & YELLOW LIFE
                if pyautogui.pixelMatchesColor(117, 60, (158, 91, 78)) or pyautogui.pixelMatchesColor(52, 63, (120, 120, 120)) or pyautogui.pixelMatchesColor(1338, 409, (7, 9, 12)):

                    redvida()
                    quase = quase + 1
                    print('O total de quase mortes foi:', quase)
                    sair = 1
                    
                #4 - MAGIC LEAF
                time.sleep(1)
                pyautogui.moveTo(x=667, y=515)
                pyautogui.click()

                #5 - LEAF BLADE
                time.sleep(1)
                pyautogui.moveTo(x=704, y=514)
                pyautogui.click()

                #5 - RAZOR LEAF
                time.sleep(1)
                pyautogui.moveTo(x=633, y=514)
                pyautogui.click()

                #SE TIVER ALGUEM DO LADO (protec player)
                if battleplayer == 45:
                    print('sistema entrou no protec player, a contagem parou em', battleplayer)
                    break


    #VOLTAR AO COMEÇO (UTILIZA POR CONTA DO 'WHILE')
    if sair == 1:
        continue

    #ESPERA CD NA VOLTA
    cd = 1

    #LOOT GERAL 2
    loot()

    #CLICAR NO ICONE POKEBATTLE 1
    pyautogui.moveTo(x=1256, y=387)
    pyautogui.click()

    #CLICAR NO ICONE PLAYER BATTLE 1
    pyautogui.moveTo(x=1185, y=384)
    pyautogui.click()

    time.sleep(0.5)

    #CHECAGEM PLAYER PARADO
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

            #TIRA PRINT DA TELA
            sc = pyautogui.screenshot()
            sc.save('playerbattle.png')

            #LIMPANDO CHAT
            pyautogui.moveTo(x=1083, y=631)
            pyautogui.click()

            #DESATIVA PROTEÇÃO PLAYER
            pl = 4


    #RETIRAR ICONE PLAYER BATTLE 2
    pyautogui.moveTo(x=1185, y=384)
    pyautogui.click()

    #CLICAR NO ICONE POKEBATTLE 2
    pyautogui.moveTo(x=1256, y=387)
    pyautogui.click()

    #CICLO CHECAGEM POSIÇÃO POKE
    for posi in range(0, 4):

        #CHECAGEM POKE POSIÇÃO
        if pyautogui.pixelMatchesColor(690, 321, (230, 249, 53)) or pyautogui.pixelMatchesColor(685, 323, (229, 250, 81)) or pyautogui.pixelMatchesColor(686, 321, (231, 249, 63)):

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


    #FOME POKEMON
    if pyautogui.pixelMatchesColor(175, 84, (203, 98, 79)):

        #CLICA NA PIZZA
        time.sleep(0.5)
        pyautogui.moveTo(x=809, y=585)
        pyautogui.click()

    #ESPERAR QUALQUER MSG
    time.sleep(4)

    #CHECAGEM PESCA LAGO, CHECA COR CHAPEU VERMELHO
    if pyautogui.pixelMatchesColor(661, 259, (115, 0, 0)) or pyautogui.pixelMatchesColor(673, 260, (217, 178, 134)):

        pass

    else:
        
        #REMOVE PESCA BUGADA
        pyautogui.moveTo(7, 31)
        pyautogui.click()

        #VOLTA NO INICIO
        continue

    #CHAMA FUNÇÃO RESPOSTA CHAT
    resposta()

    #ESPERA PESCA 16
    time.sleep(16)

    #CHAMA FUNÇÃO RESPOSTA CHAT
    resposta()

    #ESPERA CD 1
    while pyautogui.pixelMatchesColor(562, 523, (34, 96, 12)) or pyautogui.pixelMatchesColor(559, 527, (16, 42, 10)):
        
        time.sleep(1.5)

        #SAIR DA PXG CASO CAIR NET OU DEAD, PUXA COR IGRENAGEM LADO DIREITO
        if pyautogui.pixelMatchesColor(1225, 87, (204, 204, 204)):

            caiunet()
            cd = 0
            sair = 1
            break

    #VOLTA INICIO CODIGO
    if sair == 1:
        continue

    #PESCA 2
    pyautogui.moveTo(x=346, y=582)
    pyautogui.click()

    time.sleep(1.3)

    #ENCONTRA TEST HUMAN
    while pyautogui.pixelMatchesColor(683, 543, (17, 17, 17)) == False:

        peixe = pyautogui.locateOnScreen('peixeg.png', confidence=0.7, region=REGION, grayscale= True)
        barra = pyautogui.locateOnScreen('barra.png', confidence=0.8, region=REGION)

        if peixe != None and barra != None:

            if barra.top > peixe.top:

                pydirectinput.keyDown('space') 

            else:
                
                pydirectinput.keyUp('space')
                
        else:

            pydirectinput.keyDown('space')
            time.sleep(0.2)
            pydirectinput.keyUp('space')

    time.sleep(0.5)

    #VERIFICAÇÃO SHINY
    for s in range(0, 3):

        #VERIFICA COR E POKE SH KINGLER BAT
        if pyautogui.pixelMatchesColor(1178, 448, (175, 160, 6)) or pyautogui.pixelMatchesColor(1178, 448, (163, 141, 3)) or pyautogui.pixelMatchesColor(1178, 448, (195, 186, 8)):
            
            #CONTANDO OS SHINY
            shiny = shiny + 1
            print('-----'*20)
            print('O total de shinys que apareceram eh:', shiny)
            print('-----'*20)

            #ESPERA DESCER O SH CASO ESTIVER NO TOPO
            time.sleep(3)

            #9 - SOLZIN
            time.sleep(1)
            pyautogui.moveTo(x=847, y=513)
            pyautogui.click()
            
            #SELECIONAR SHINY MAGI BATTLE (BAT 1)
            time.sleep(0.5)
            pyautogui.moveTo(x=1183, y=445)
            pyautogui.click()

            #7 - PETAL BLIZARD
            time.sleep(1)
            pyautogui.moveTo(x=780, y=511)
            pyautogui.click()

            #8 - DORMIR
            time.sleep(1)
            pyautogui.moveTo(x=810, y=514)
            pyautogui.click()

            #1 - ABSORB SEED RAIN
            time.sleep(1)
            pyautogui.moveTo(x=560, y=518)
            pyautogui.click()

            #4 - MAGIC LEAF
            time.sleep(1)
            pyautogui.moveTo(x=667, y=515)
            pyautogui.click()

            #5 - LEAF BLADE
            time.sleep(1)
            pyautogui.moveTo(x=704, y=514)
            pyautogui.click()

            #6 - FOLHA FRONTAL
            time.sleep(1)
            pyautogui.moveTo(742, 517)
            pyautogui.click()

            #3 - RAZOR LEAF
            time.sleep(1)
            pyautogui.moveTo(x=633, y=514)
            pyautogui.click()

            #2 - SEED ABSORB
            time.sleep(1)
            pyautogui.moveTo(x=597, y=514)
            pyautogui.click()

            time.sleep(2)

            #ENQUANTO TIVER UM POKEMON NO BATTLE ELE EXECUTA VERIFICAÇÃO REDLIFE
            while pyautogui.pixelMatchesColor(1182, 445, (7, 9, 12)) == False:

                print('entrou no cd while SHINY')
                battleplayer = battleplayer + 1

                #ATTKS

                #4 - MAGIC LEAF
                time.sleep(1)
                pyautogui.moveTo(x=667, y=515)
                pyautogui.click()

                #VERIFICAÇAO RED & YELLOW LIFE
                if pyautogui.pixelMatchesColor(117, 60, (158, 91, 78)) or pyautogui.pixelMatchesColor(52, 63, (120, 120, 120)) or pyautogui.pixelMatchesColor(1338, 409, (7, 9, 12)):

                    redvida()
                    quase = quase + 1
                    print('O total de quase mortes foi:', quase)
                    sair = 1

                #SAI DO LOOP CASO SAIR FOR IGUAL 1
                if sair == 1:
                    break
        
                #5 - LEAF BLADE
                time.sleep(1)
                pyautogui.moveTo(x=704, y=514)
                pyautogui.click()

                #VERIFICAÇAO RED & YELLOW LIFE
                if pyautogui.pixelMatchesColor(117, 60, (158, 91, 78)) or pyautogui.pixelMatchesColor(52, 63, (120, 120, 120)) or pyautogui.pixelMatchesColor(1338, 409, (7, 9, 12)):

                    redvida()
                    quase = quase + 1
                    print('O total de quase mortes foi:', quase)
                    sair = 1
                
                #SAI DO LOOP CASO SAIR FOR IGUAL 1
                if sair == 1:
                    break

                #5 - RAZOR LEAF
                time.sleep(1)
                pyautogui.moveTo(x=633, y=514)
                pyautogui.click()

                #VERIFICAÇAO RED & YELLOW LIFE
                if pyautogui.pixelMatchesColor(117, 60, (158, 91, 78)) or pyautogui.pixelMatchesColor(52, 63, (120, 120, 120)) or pyautogui.pixelMatchesColor(1338, 409, (7, 9, 12)):

                    redvida()
                    quase = quase + 1
                    print('O total de quase mortes foi:', quase)
                    sair = 1
                
                #SAI DO LOOP CASO SAIR FOR IGUAL 1
                if sair == 1:

                    break

                #SE TIVER ALGUEM DO LADO (protec player)
                if battleplayer == 55:

                    print('sistema entrou no protec player, a contagem parou em', battleplayer)
                    break

            time.sleep(2)
        

            #PEGA LOOT SHINY
            loot()

            #JOGAR BALL

            #BALL 2
            if pyautogui.pixelMatchesColor(657, 211, (254, 255, 109)) or pyautogui.pixelMatchesColor(685, 215, (115, 199, 240)):

                time.sleep(1)
                pyautogui.moveTo(x=391, y=584)
                pyautogui.click()
                time.sleep(1)
                pyautogui.moveTo(657, 211)
                pyautogui.click()


            #BALL 3
            if pyautogui.pixelMatchesColor(702, 211, (254, 255, 109)) or pyautogui.pixelMatchesColor(730, 216, (174, 226, 247)):

                time.sleep(1)
                pyautogui.moveTo(x=391, y=584)
                pyautogui.click()
                time.sleep(1)
                pyautogui.moveTo(702, 211)
                pyautogui.click()


            #BALL 4
            if pyautogui.pixelMatchesColor(704, 257, (245, 249, 74)) or pyautogui.pixelMatchesColor(724, 258, (118, 193, 234)):

                time.sleep(1)
                pyautogui.moveTo(x=391, y=584)
                pyautogui.click()
                time.sleep(1)
                pyautogui.moveTo(x=727, y=278)
                pyautogui.click()

            #ball 5
            if pyautogui.pixelMatchesColor(706, 304, (247, 253, 17)) or pyautogui.pixelMatchesColor(728, 306, (63, 170, 229)):

                time.sleep(1)
                pyautogui.moveTo(x=391, y=584)
                pyautogui.click()
                time.sleep(1)
                pyautogui.moveTo(x=726, y=322)
                pyautogui.click()

            #ball 7
            if pyautogui.pixelMatchesColor(602, 326, (247, 253, 17)) or pyautogui.pixelMatchesColor(600, 298, (236, 216, 0)):
                time.sleep(1)
                pyautogui.moveTo(x=391, y=584)
                pyautogui.click()
                time.sleep(1)
                pyautogui.moveTo(x=634, y=324)
                pyautogui.click()

            #ball 8
            if pyautogui.pixelMatchesColor(601, 280, (247, 253, 17)) or pyautogui.pixelMatchesColor(610, 256, (252, 254, 80)):
                time.sleep(1)
                pyautogui.moveTo(x=391, y=584)
                pyautogui.click()
                time.sleep(1)
                pyautogui.moveTo(x=637, y=280)
                pyautogui.click()

            #VOLTA AO INICIO DO CODIGO
            sair = 1


    #VOLTA INICIO CODIGO
    if sair == 1:
        continue
    
    #VERIFICA SE TEM POKE NA POSI 4
    if pyautogui.pixelMatchesColor(1183, 531, (7, 9, 12)) == True:

        #SE NAO TIVER PASSA
        pass

    else:

        #SE O BAT 4 CONTIVER POKE
        while pyautogui.pixelMatchesColor(1183, 531, (7, 9, 12)) == False:

            time.sleep(0.1)

            #SAIR DA PXG CASO CAIR NET OU DEAD, PUXA COR IGRENAGEM LADO DIREITO
            if pyautogui.pixelMatchesColor(1225, 87, (204, 204, 204)):

                caiunet()
                cd = 0
                sair = 1
                break

    #VOLTA INICIO CODIGO
    if sair == 1:
        continue

    #VERIFICAÇAO RED & YELLOW LIFE
    if pyautogui.pixelMatchesColor(117, 60, (158, 91, 78)) or pyautogui.pixelMatchesColor(117, 60, (142, 150, 74)) or pyautogui.pixelMatchesColor(52, 63, (120, 120, 120)) or pyautogui.pixelMatchesColor(1338, 409, (7, 9, 12)):

        redvida()
        quase = quase + 1
        print('O total de quase mortes foi:', quase)
        continue
    
    #CHAMA FUNÇÃO RESPOSTA CHAT
    resposta()
    
    #SAIR DA PXG CASO CAIR NET OU DEAD, PUXA COR IGRENAGEM LADO DIREITO
    if pyautogui.pixelMatchesColor(1225, 87, (204, 204, 204)):

        caiunet()
        cd = 0
        continue

