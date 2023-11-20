import pyautogui
import random
import time
import pydirectinput

#SCRIPT WINDOWS PC
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
#REGIÃO MINI GAME PEIXE
REGION = (667, 336, 30, 356)
#VARIAVEL TEMPO HUMAN TEST
tempo = 0
#VARIAVEL CALCULA FALHAS HUMAN TEST
falhou = 0
#VARIAVEL NAO MOSTRA TEMPO CASO FALHAS HUMAN TEST
humanfail = 0

#FUNÇÃO PEGA LOOT
def loot():

    #LOOT
    pydirectinput.keyDown('e')
    time.sleep(0.3)
    pydirectinput.keyUp('e')


#FUNÇÃO VIDA BAIXA OU POKE DEAD
def redvida():

    #TORNAR GLOBAL VARIAL SAIR
    global sair
    #UTILIZANDO PARA ATTACAR UMA VEZ COM A VIC
    global battleplayer

    sair = 1

    #SE O POKE MORRER
    if pyautogui.pixelMatchesColor(52, 63, (120, 120, 120)) or pyautogui.pixelMatchesColor(1338, 409, (7, 9, 12)):

        sc = pyautogui.screenshot()
        sc.save('CHECAR-RED.png')

        sair = 0

        print('ENTROU DEAD POKE REDVIDA')

        #SELECIONAR REVIVE
        pyautogui.moveTo(x=771, y=581)
        pyautogui.click()

        #MOVER PARA O SH VILE
        pyautogui.moveTo(x=35, y=50)
        pyautogui.click()

        time.sleep(1)

        #CLICAR VILEPLUME
        pyautogui.moveTo(32, 53)
        pyautogui.click()

        time.sleep(2)


    #CHAMA POKE RESERVA
    if sair == 1:

        #SE LOCALIZAR A VIC NA TELA CONTINUA
        if pyautogui.locateCenterOnScreen('vic.png'):
            
            #SELECIONAR VICTRIBEL
            pyautogui.moveTo('vic.png')
            pyautogui.click()

            time.sleep(1.5)

            #ENQUANTO TIVER UM POKEMON NO BATTLE ELE TENTA DERROTAR
            while pyautogui.pixelMatchesColor(1182, 445, (7, 9, 12)) == False and pyautogui.pixelMatchesColor(1180, 474, (7, 9, 12)) == True:
                
                print('ENTROU BATTLE VIC')

                sc = pyautogui.screenshot()
                sc.save('CHECAR-VIC.png')

                #SOMENTE ATACAR UMA VEZ
                if battleplayer == 0:

                    #ATTK 0 - BUF ATK
                    pydirectinput.keyDown('0')
                    time.sleep(0.2)
                    pydirectinput.keyUp('0')

                    #ATTK 8 - LEAF STORM
                    pydirectinput.keyDown('8')
                    time.sleep(0.2)
                    pydirectinput.keyUp('8')

                    battleplayer = 1

                #ATTK 3 - MAGIC LEAF
                pydirectinput.keyDown('3')
                time.sleep(0.2)
                pydirectinput.keyUp('3')

                #ATTK 1 - RAZOR LEAF
                pydirectinput.keyDown('1')
                time.sleep(0.2)
                pydirectinput.keyUp('1')

                #SOMATORIA VARIVEL PARA SAIR WHILE
                battleplayer = battleplayer + 1

                #SE TIVER ALGUEM DO LADO (protec player)
                if battleplayer == 45:
                    print('sistema entrou no protec player, a contagem parou em', battleplayer)
                    break

            #DAR POTION VIC
            pyautogui.moveTo(x=656, y=584)
            pyautogui.click()

            time.sleep(8)

            #VOLTAR SH PLUME
            pyautogui.moveTo('vilepoke.png')
            pyautogui.click()

        #SE NAO LOCALIZAR A VIC NA TELA BATE REVIVE
        else:

            #CASO BUGAR BATE REVIVE

            print('BATEU REVIVE')

            sc = pyautogui.screenshot()
            sc.save('bateu-revive-ver.png')
            
            #VOLTAR POKE PARA A BALL
            pyautogui.moveTo(x=35, y=50)
            pyautogui.click()

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

            #ENQUANTO TIVE POKE NO BAT ELE ATK
            while pyautogui.pixelMatchesColor(1182, 445, (7, 9, 12)) == False and pyautogui.pixelMatchesColor(1180, 474, (7, 9, 12)) == True:
                    
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

                #SOMATORIA VARIVEL PARA SAIR WHILE
                battleplayer = battleplayer + 1

                #SE TIVER ALGUEM DO LADO (protec player)
                if battleplayer == 45:
                    print('sistema entrou no protec player, a contagem parou em', battleplayer)
                    break


#FUNÇÃO SAIR JOGO CHAT
def sairjogo():

    #CTRL + Q PARA DAR DISPLAY DO MENU SAIR
    pydirectinput.keyDown('ctrl')
    pydirectinput.keyDown('q')
    pydirectinput.keyUp('ctrl')
    pydirectinput.keyUp('q')

    time.sleep(2)

    #CONFIRMAR SAIR
    pydirectinput.keyUp('enter')
    pydirectinput.keyDown('enter')

    time.sleep(2.5)
    
    #SAIR CHAR
    if pyautogui.pixelMatchesColor(759, 196, (139, 139, 139)) == True:


        #espera deslogar sozinho (800)
        time.sleep(800)

        print('NÃO ENCONTROU BOTAO SAIR JOGO')
        

    #ESPERA UM POUCO (1hr)
    time.sleep(3600)

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
    if pyautogui.pixelMatchesColor(759, 196, (139, 139, 139)) or pyautogui.pixelMatchesColor(759, 196, (151, 151, 151)):

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
    
    #CHAT 1
    if chat == 0:

        #CHECA COR CHAT
        if pyautogui.pixelMatchesColor(242, 682, (212, 212, 1)) or pyautogui.pixelMatchesColor(243, 676, (246, 246, 0)):

            sc = pyautogui.screenshot()
            sc.save('chat1.png')

            sairjogo()

            #DESATIVA PROTEÇÃO PLAER BATTLE
            pl = 4

            #ATIVA CHAT 2 (1)
            chat = 0



#FUNÇÕES BASICAS LAGO
def lago1():
    pyautogui.moveTo(x=359, y=138)
    pyautogui.click()


def lago2():
    pyautogui.moveTo(x=318, y=180)
    pyautogui.click()


time.sleep(1)

#COLOCAR ISCA
#pyautogui.moveTo(x=887, y=586)
#pyautogui.click()

#PARE-MID
pyautogui.moveTo(x=133, y=83)
pyautogui.click()

#CHECAGEM ISCA (CHECA FINAL FRASE)
#if pyautogui.pixelMatchesColor(585, 679, (7, 7, 7)):

    #COLOCA ISCA
    #pyautogui.moveTo(x=887, y=586)
    #pyautogui.click()

#else:

    #pass

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
    #VOLTANDO VARIAVEL TEMPO
    tempo = 0
    #VOLTANDO VARIAVEL FALHA HUMAN TEST
    humanfail = 0

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

    #CICLO CHECAGEM POSIÇÃO POKE
    for posi in range(0, 2):

        #CHECAGEM POKE POSIÇÃO
        if pyautogui.pixelMatchesColor(693, 313, (145, 145, 146)) == True:

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

    #RESTAURAR VIDA BONECO
    if pyautogui.pixelMatchesColor(343, 554, (69, 151, 69)) or pyautogui.pixelMatchesColor(341, 556, (161, 161, 0)):

        #CLICA NO HAMBUGUER
        time.sleep(0.5)
        pyautogui.moveTo(850, 585)
        pyautogui.click()

        sc = pyautogui.screenshot()
        sc.save('CHECAR-VIDA-BONECO.png')

    #ESPERAR QUALQUER MSG
    time.sleep(4)

    #CHECAGEM PESCA LAGO
    if pyautogui.pixelMatchesColor(658, 272 ,(98, 96, 101)) or pyautogui.pixelMatchesColor(649, 271, (107, 47, 28)):

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
    time.sleep(12)

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

        #SAI E VOLTA DO JOGO CASO HOUVER PLAYER NA TELA
        if pl == 1: 

            sc = pyautogui.screenshot()
            sc.save('PLAYER-TELA.png')

            sairjogo()
            sair = 1


    #RETIRAR ICONE PLAYER BATTLE 2
    pyautogui.moveTo(x=1185, y=384)
    pyautogui.click()

    #CLICAR NO ICONE POKEBATTLE 2
    pyautogui.moveTo(x=1256, y=387)
    pyautogui.click()

    #VOLTAR AO COMEÇO (UTILIZA POR CONTA DO 'WHILE')
    if sair == 1:
        continue

    #SAIR DA PXG CASO CAIR NET OU DEAD, PUXA COR IGRENAGEM LADO DIREITO
    if pyautogui.pixelMatchesColor(1225, 87, (204, 204, 204)):

        caiunet()
        cd = 0
        continue

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

    #CALCULA TEMPO GASTO
    inicio = time.time()

    #ENCONTRA TEST HUMAN
    while pyautogui.pixelMatchesColor(683, 543, (17, 17, 17)) == False:

        #ENTROU HUMAN TEST
        tempo = 1

        peixe = pyautogui.locateOnScreen('peixeg.png', confidence=0.8, region=REGION, grayscale= True)
        barra = pyautogui.locateOnScreen('pontabarra.png', confidence=0.8, region=REGION)

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

    #temp
    pydirectinput.keyDown('space')
    time.sleep(0.2)
    pydirectinput.keyUp('space')

    #MOSTRA O TEMPO DE EXECUÇÃO DO HUMAN TEST
    if tempo == 1:
        
        #VERIFICAR SE FALHOU
        if pyautogui.pixelMatchesColor(1178, 448, (7, 9, 12)):

            print('HUMAN FAIL')
            falhou = falhou + 1
            print('O TOTAL DE VEZES QUE FALHOU FOI DE:', falhou)
            humanfail = 1

        #MOSTRA TEMPO CASO NÃO FALHA HUMAN TEST
        if humanfail == 0:

            fim = time.time()
            resultado = int(fim - inicio)
            
            #CRIA E ABRE O ARQUIVO ARQ01.TXT NO MODO DE ESCRITA
            arquivo = open('tempo.txt','a')

            #DEFINE A VARIAVEL TEXTO COM STRING E ESCREVE NO TXT, AO FINAL DA UM ESPAÇO
            arquivo.write(str(resultado) + '\n')

            #SALVA O ARQUIVO
            arquivo.close()

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

            #BALL 4 DIA
            if pyautogui.pixelMatchesColor(702, 256, (252, 254, 80)) or pyautogui.pixelMatchesColor(729, 260, (77, 176, 231)):

                time.sleep(1)
                pyautogui.moveTo(x=391, y=584)
                pyautogui.click()
                time.sleep(1)
                pyautogui.moveTo(718, 276)
                pyautogui.click()

            #ball 5 DIA
            if pyautogui.pixelMatchesColor(703, 301, (250, 254, 52)) or pyautogui.pixelMatchesColor(728, 303, (210, 234, 246)):

                time.sleep(1)
                pyautogui.moveTo(x=391, y=584)
                pyautogui.click()
                time.sleep(1)
                pyautogui.moveTo(724, 327)
                pyautogui.click()

            #ball 7 DIA
            if pyautogui.pixelMatchesColor(612, 301, (250, 254, 52)) or pyautogui.pixelMatchesColor(631, 303, (139, 212, 244)) or pyautogui.pixelMatchesColor(601, 315, (224, 238, 226)):
                time.sleep(1)
                pyautogui.moveTo(x=391, y=584)
                pyautogui.click()
                time.sleep(1)
                pyautogui.moveTo(635, 325)
                pyautogui.click()

            #ball 8 DIA
            if pyautogui.pixelMatchesColor(613, 256, (241, 248, 44)) or pyautogui.pixelMatchesColor(630, 256, (139, 209, 242)) or pyautogui.pixelMatchesColor(604, 271, (236, 236, 14)):
                time.sleep(1)
                pyautogui.moveTo(x=391, y=584)
                pyautogui.click()
                time.sleep(1)
                pyautogui.moveTo(633, 283)
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
    
    #SAIR DA PXG CASO CAIR NET OU DEAD, PUXA COR IGRENAGEM LADO DIREITO
    if pyautogui.pixelMatchesColor(1225, 87, (204, 204, 204)):

        caiunet()
        cd = 0
        continue

