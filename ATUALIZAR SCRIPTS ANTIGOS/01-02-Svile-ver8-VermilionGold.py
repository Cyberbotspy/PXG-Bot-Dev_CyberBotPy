import pyautogui
import random
import time
import pydirectinput

#SCRIPT WINDOWS
#SCRIPT LVL 130+ COM SH VILE

#ROBO COM SHINY VILEPLUME COM ISCA KEPT

#CODIGO QUE DERROTA O SHINY E JOGA BALL NELE
#AJUSTE MAPA: CHAT ME
#LUGAR: CHAT ME

#IR PARA PXG
pyautogui.keyDown('alt')

pyautogui.press('tab')

pyautogui.keyUp('alt')

#VARIAVEL PULA LOOT INICIO
pegarloot = 0
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

#FUNÇÃO PEGA LOOT
def loot():

    #LOOT
    pydirectinput.keyDown('e')
    time.sleep(0.3)
    pydirectinput.keyUp('e')


#FUNÇÃO VIDA BAIXA
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

    if pyautogui.pixelMatchesColor(52, 63, (120, 120, 120)):

        sair = 1

        print('ENTROU DEAD POKE REDVIDA')

        #SOLTAR TAUROS
        pyautogui.moveTo('tauros.png')
        pyautogui.click()

        time.sleep(0.5)

        #RIDE TAUROS
        pyautogui.moveTo(x=681, y=261)
        pyautogui.middleClick()

        time.sleep(2.5)

        #IR MAPA
        pyautogui.moveTo(x=1310, y=286)
        pyautogui.click()

        #IDA ATÉ CP
        time.sleep(25)

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

            time.sleep(2.5)

            #IR MAPA VOLTAR ESCADA
            pyautogui.moveTo(x=1218, y=80)
            pyautogui.click()

            time.sleep(25)

            #SAIR RIDE
            pyautogui.moveTo(x=681, y=261)
            pyautogui.middleClick()

            time.sleep(3.5)

            #CLICAR VILEPLUME
            pyautogui.moveTo('vilepoke.png')
            pyautogui.click()

            #IR POSIÇÃO
            pyautogui.moveTo(x=679, y=181)
            pyautogui.click()

            time.sleep(1.5)

        else:

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


#FUNÇÃO SAIR JOGO CHAT
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

        exit()

    #COLOCAR ISCA KEPT
    pyautogui.moveTo(x=887, y=586)
    pyautogui.click()

    #PARE-MID
    pyautogui.moveTo(x=133, y=83)
    pyautogui.click()

    #descer escada
    pyautogui.moveTo(x=681, y=236)
    pyautogui.click()

    time.sleep(1)

    #IR POSIÇÃO
    pyautogui.moveTo(x=679, y=181)
    pyautogui.click()

    time.sleep(2)

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

    #CHECAGEM COR X
    if pyautogui.pixelMatchesColor(723, 232, (185, 137, 90)):

        #CLICAR VILEPLUME
        pyautogui.moveTo('vilepoke.png')
        pyautogui.click()

        #COLOCAR ISCA KEPT
        pyautogui.moveTo(x=887, y=586)
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
    global pl

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

                #INICAR FUNÇÃO SAIR JOGO
                sairjogo()


#FUNÇÕES LAGO
def lago1():

    #CHAMA O VALOR DA VARIAVEL PARA FUNÇÃO
    global fish

    #LAGO 1 POSI 1
    if fish == 5:

        pyautogui.moveTo(x=808, y=277)
        pyautogui.click()

        fish = 0

    #LAGO 1 POSI 2
    if fish == 4:

        pyautogui.moveTo(x=852, y=266)
        pyautogui.click()

        fish = fish + 1

    #LAGO 1 POSI 3
    if fish == 3:

        pyautogui.moveTo(x=901, y=259)
        pyautogui.click()

        fish = fish + 1

    #LAGO 1 POSI 4
    if fish == 2:

        pyautogui.moveTo(x=959, y=258)
        pyautogui.click()

        fish = fish + 1

    #LAGO 1 POSI 5
    if fish == 1:

        pyautogui.moveTo(x=1009, y=259)
        pyautogui.click()

        fish = fish + 1

    #LAGO 1 POSI 6
    if fish == 0:

        pyautogui.moveTo(x=1058, y=258)
        pyautogui.click()

        fish = fish + 1


def lago2():

    #CHAMA O VALOR DA VARIAVEL PARA FUNÇÃO
    global fish

    #LAGO 1 POSI 1
    if fish == 5:

        pyautogui.moveTo(x=806, y=324)
        pyautogui.click()

        fish = 0

    #LAGO 1 POSI 2
    if fish == 4:

        pyautogui.moveTo(x=865, y=319)
        pyautogui.click()

        fish = fish + 1

    #LAGO 1 POSI 3
    if fish == 3:

        pyautogui.moveTo(x=918, y=319)
        pyautogui.click()

        fish = fish + 1

    #LAGO 1 POSI 4
    if fish == 2:

        pyautogui.moveTo(x=987, y=320)
        pyautogui.click()

        fish = fish + 1

    #LAGO 1 POSI 5
    if fish == 1:

        pyautogui.moveTo(x=1036, y=318)
        pyautogui.click()

        fish = fish + 1

    #LAGO 1 POSI 6
    if fish == 0:

        pyautogui.moveTo(x=1083, y=311)
        pyautogui.click()

        fish = fish + 1


def lago3():

    #CHAMA O VALOR DA VARIAVEL PARA FUNÇÃO
    global fish

    #LAGO 1 POSI 1
    if fish == 5:

        pyautogui.moveTo(x=804, y=379)
        pyautogui.click()

        fish = 0

    #LAGO 1 POSI 2
    if fish == 4:

        pyautogui.moveTo(x=857, y=378)
        pyautogui.click()

        fish = fish + 1

    #LAGO 1 POSI 3
    if fish == 3:

        pyautogui.moveTo(x=902, y=378)
        pyautogui.click()

        fish = fish + 1

    #LAGO 1 POSI 4
    if fish == 2:

        pyautogui.moveTo(x=958, y=378)
        pyautogui.click()

        fish = fish + 1

    #LAGO 1 POSI 5
    if fish == 1:

        pyautogui.moveTo(x=1008, y=377)
        pyautogui.click()

        fish = fish + 1

    #LAGO 1 POSI 6
    if fish == 0:

        pyautogui.moveTo(x=1054, y=376)
        pyautogui.click()

        fish = fish + 1


time.sleep(1)

#COLOCAR ISCA KEPT
pyautogui.moveTo(x=887, y=586)
pyautogui.click()

#PARE-MID
pyautogui.moveTo(x=133, y=83)
pyautogui.click()

#CHECAGEM ISCA (CHECA FINAL FRASE)
if pyautogui.pixelMatchesColor(585, 679, (7, 7, 7)):

   pass

else:

    #COLOCA ISCA KEPT
    pyautogui.moveTo(x=887, y=586)
    pyautogui.click()


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

    #LOOT GERAL
    loot()

    #ESPERA CD
    if cd == 1:
        
        #SE CONTIVER ALGO NA PRIMEIRA POSI NO BAT / ESPERA 10s
        if pyautogui.pixelMatchesColor(1182, 445, (7, 9, 12)):

            #SE NAO TIVER NADA
            time.sleep(10)

        else:

            #SE TIVER POKE BAT
            
            #ENQUANTO TIVER UM POKEMON NO BATTLE ELE EXECUTA VERIFICAÇÃO REDLIFE
            while pyautogui.pixelMatchesColor(1182, 445, (7, 9, 12)) == False:

                #SOMATORIA VARIVEL PARA SAIR WHILE
                battleplayer = battleplayer + 1

                #CLICAR BATTLE 1
                pyautogui.moveTo(x=1183, y=445)
                pyautogui.click()

                #VERIFICAÇAO RED & YELLOW LIFE
                if pyautogui.pixelMatchesColor(117, 60, (158, 91, 78)) or pyautogui.pixelMatchesColor(52, 63, (120, 120, 120)) or pyautogui.pixelMatchesColor(1338, 409, (7, 9, 12)):

                    redvida()
                    quase = quase + 1
                    print('O total de quase mortes foi:', quase)
                    sair = 1

                #5 - LEAF BLADE
                time.sleep(1)
                pyautogui.moveTo(x=704, y=514)
                pyautogui.click()

                #5 - RAZOR LEAF
                time.sleep(1)
                pyautogui.moveTo(x=633, y=514)
                pyautogui.click()

                #4 - MAGIC LEAF
                time.sleep(1)
                pyautogui.moveTo(x=667, y=515)
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

    #PESCA 1
    pyautogui.moveTo(x=346, y=582)
    pyautogui.click()

    #LAGO
    #LISTA SQMs LAGO
    lagolista = [lago1, lago2, lago3]
    #JOGA ALEATORIAMENTE EM EM SQM DA LSITA
    random.choice(lagolista)()

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
    for posi in range(0, 2):

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

    #CHAMA FUNÇÃO RESPOSTA CHAT
    resposta()


    #ESPERA PESCA
    time.sleep(26)


    #CHAMA FUNÇÃO RESPOSTA CHAT
    resposta()


    #ESPERA CD 1
    while pyautogui.pixelMatchesColor(562, 523, (34, 96, 12)) or pyautogui.pixelMatchesColor(559, 527, (16, 42, 10)):
        
        time.sleep(1.5)

        #SAIR DA PXG CASO CAIR NET OU DEAD, PUXA COR IGRENAGEM LADO DIREITO
        if pyautogui.pixelMatchesColor(1225, 87, (204, 204, 204)):

            caiunet()
            cd = 0
            continue

    #PESCA 2
    pyautogui.moveTo(x=346, y=582)
    pyautogui.click()

    #1 - ABSORB SEED RAIN
    time.sleep(1)
    pyautogui.moveTo(x=560, y=518)
    pyautogui.click()

    #VERIFICICAÇAO SHINY
    for s in range(0, 3):

        #VERIFICA COR E POKE SH KINGLER BAT
        if pyautogui.pixelMatchesColor(1183, 448, (19,52,137)):

            #CONTANDO OS SHINY
            shiny = shiny + 1
            print('-----'*20)
            print('O total de shinys que apareceram eh:', shiny)
            print('-----'*20)

            #9 - SOLZIN
            time.sleep(1)
            pyautogui.moveTo(x=847, y=513)
            pyautogui.click()
            
            #SELECIONAR SHINY KINGLER BATTLE (BAT 1)
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
                if pyautogui.pixelMatchesColor(117, 60, (158, 91, 78)) or pyautogui.pixelMatchesColor(117, 60, (142, 150, 74)) or pyautogui.pixelMatchesColor(52, 63, (120, 120, 120)) or pyautogui.pixelMatchesColor(1338, 409, (7, 9, 12)):

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
                if pyautogui.pixelMatchesColor(117, 60, (158, 91, 78)) or pyautogui.pixelMatchesColor(117, 60, (142, 150, 74)) or pyautogui.pixelMatchesColor(52, 63, (120, 120, 120)) or pyautogui.pixelMatchesColor(1338, 409, (7, 9, 12)):

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
                if pyautogui.pixelMatchesColor(117, 60, (158, 91, 78)) or pyautogui.pixelMatchesColor(117, 60, (142, 150, 74)) or pyautogui.pixelMatchesColor(52, 63, (120, 120, 120)) or pyautogui.pixelMatchesColor(1338, 409, (7, 9, 12)):

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
        

            #PEGA LOOT SHINY
            loot()

            #JOGAR BALL

            #BALL 4
            if pyautogui.pixelMatchesColor(718, 270, (13, 30, 68)):

                time.sleep(1)
                pyautogui.moveTo(x=391, y=584)
                pyautogui.click()
                time.sleep(1)
                pyautogui.moveTo(x=727, y=278)
                pyautogui.click()

            #ball 5
            if pyautogui.pixelMatchesColor(718, 315, (13, 30,68)):

                time.sleep(1)
                pyautogui.moveTo(x=391, y=584)
                pyautogui.click()
                time.sleep(1)
                pyautogui.moveTo(x=726, y=322)
                pyautogui.click()

            #ball 6
            if pyautogui.pixelMatchesColor(672, 315, (21, 52, 122)):

                time.sleep(1)
                pyautogui.moveTo(x=391, y=584)
                pyautogui.click()
                time.sleep(1)
                pyautogui.moveTo(x=681, y=318)
                pyautogui.click()

            #ball 7
            if pyautogui.pixelMatchesColor(626, 329, (198, 198, 198)) or pyautogui.pixelMatchesColor(608, 342, (23, 84, 221)) or pyautogui.pixelMatchesColor(613, 316, (9, 38, 84)) or pyautogui.pixelMatchesColor(616, 299, (17, 55, 142)):
                time.sleep(1)
                pyautogui.moveTo(x=391, y=584)
                pyautogui.click()
                time.sleep(1)
                pyautogui.moveTo(x=634, y=324)
                pyautogui.click()

            #ball 8
            if pyautogui.pixelMatchesColor(627, 268, (21, 56, 136)):
                time.sleep(1)
                pyautogui.moveTo(x=391, y=584)
                pyautogui.click()
                time.sleep(1)
                pyautogui.moveTo(x=637, y=280)
                pyautogui.click()

            #FAZ COM QUE NAO PEGUE LOOT DE NOVO
            pergarloot = 3
            sair = 1

            time.sleep(10)

        else:
            pass

    
    #VOLTA INIICO DO CODIGO
    if sair == 1:
        continue
    

    #VERIFICAÇAO QFISH
    for a in range(0,2):
        
        #PUXA COR QFISH
        if pyautogui.pixelMatchesColor(1186, 446, (67, 85, 113)) or pyautogui.pixelMatchesColor(1186, 445, (77, 98, 129)) or pyautogui.pixelMatchesColor(1186, 444, (103, 127, 162)):

            #6 - PETAL BLIZARD
            time.sleep(1)
            pyautogui.moveTo(x=780, y=511)
            pyautogui.click()

            time.sleep(3.5)

            loot()

            #FAZ COM QUE NAO PEGUE LOOT DE NOVO
            pegarloot = 3

            #SE CONTIVER ALGO NA PRIMEIRA POSI NO BAT / ESPERA 20s
            if pyautogui.pixelMatchesColor(1182, 445, (7, 9, 12)):

                #SE NAO TIVER NADA
                time.sleep(20)

            else:

                #SE TIVER POKE NO BAT

                #CLICAR BATTLE 1
                pyautogui.moveTo(x=1183, y=445)
                pyautogui.click()

                #5 - RAZOR LEAF
                time.sleep(1)
                pyautogui.moveTo(x=633, y=514)
                pyautogui.click()

                #4 - MAGIC LEAF
                time.sleep(1)
                pyautogui.moveTo(x=667, y=515)
                pyautogui.click()

                #5 - LEAF BLADE
                time.sleep(1)
                pyautogui.moveTo(x=704, y=514)
                pyautogui.click()
                
                #ENQUANTO TIVER UM POKEMON NO BATTLE ELE EXECUTA VERIFICAÇÃO REDLIFE
                while pyautogui.pixelMatchesColor(1182, 445, (7, 9, 12)) == False:

                    battleplayer = battleplayer + 1

                    #VERIFICAÇAO RED & YELLOW LIFE
                    if pyautogui.pixelMatchesColor(117, 60, (158, 91, 78)) or pyautogui.pixelMatchesColor(52, 63, (120, 120, 120)) or pyautogui.pixelMatchesColor(1338, 409, (7, 9, 12)):

                        redvida()
                        quase = quase + 1
                        print('O total de quase mortes foi:', quase)

                    #CLICAR BATTLE 1
                    pyautogui.moveTo(x=1183, y=445)
                    pyautogui.click()

                    #5 - RAZOR LEAF
                    time.sleep(1)
                    pyautogui.moveTo(x=633, y=514)
                    pyautogui.click()

                    #VERIFICAÇAO RED & YELLOW LIFE
                    if pyautogui.pixelMatchesColor(117, 60, (158, 91, 78)) or pyautogui.pixelMatchesColor(52, 63, (120, 120, 120)) or pyautogui.pixelMatchesColor(1338, 409, (7, 9, 12)):

                        redvida()
                        quase = quase + 1
                        print('O total de quase mortes foi:', quase)

                    #4 - MAGIC LEAF
                    time.sleep(1)
                    pyautogui.moveTo(x=667, y=515)
                    pyautogui.click()

                    #5 - LEAF BLADE
                    time.sleep(1)
                    pyautogui.moveTo(x=704, y=514)
                    pyautogui.click()


                    #SE TIVER ALGUEM DO LADO (protec player)
                    if battleplayer == 45:

                        print('sistema entrou no protec player, a contagem parou em', battleplayer)
                        break
                        
            #VOLTA AO COMEÇO QUANDO O SCRIPT QFISH TERMINAR
            continue

        else:
            pass


    #VERIFICAÇAO RED & YELLOW LIFE
    if pyautogui.pixelMatchesColor(117, 60, (158, 91, 78)) or pyautogui.pixelMatchesColor(52, 63, (120, 120, 120)):

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
