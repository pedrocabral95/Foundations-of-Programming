from parte1 import e_palavra
from itertools import permutations

#Pedro Miguel Alves Cabral , ist190767 , Fundamentos da Programacao , 2Projeto


'''
###################TAD_palavra potencial##########################
Este TAD sera usado para representar as palavras propostas pelos jogadores, de acordo com a gramatica definida
'''

def cria_palavra_potencial(cad_car,letras):

    '''
    ######## Criador ###########
    A funcao cria_palavra_potencial(cad_car,letras) recebe dois argumentos, uma palavra potencial e um tuplo de letras que define o conjunto de palavras a descobrir.
    Se a palavra proposta nao estiver conforme a gramatica ou se possuir algum caracter invalido ou caracter que nao esteja no tuplo de letras, sera gerado um erro.
    Em caso contrario, devolde a palavra inserida.
    ###> try_word = cria_palavra('LA', ('A','E', 'L'))
    ###> try_word
    ###> 'LA'
    ############################
    '''

    if not isinstance(cad_car,str) or not isinstance(letras,tuple):
        raise ValueError('cria_palavra_potencial:argumentos invalidos.')
    #Verifica se a cadeia de caracteres  ou tuplo de letras tem algum caracter nao permitido ----->letras minusculas e caracteres especiais

    for i in range(len(letras)):

        if len(letras[i]) > 1:
            raise ValueError('cria_palavra_potencial:argumentos invalidos.')

        elif not 64 < ord(letras[i]) < 91:
            raise ValueError('cria_palavra_potencial:argumentos invalidos.')

    for i in range(len(cad_car)):

        if not 64 < ord(cad_car[i]) < 91:
            raise ValueError('cria_palavra_potencial:argumentos invalidos.')


    if len(cad_car) > len(letras):
        raise ValueError('cria_palavra_potencial:a palavra nao e valida.')

    #Verifica a quantidade de letras presente na cadeia de caracteres
    # verifica se tem algum caracter diferente do fornecido

    for i in cad_car:

        if i not in letras:
            raise ValueError('cria_palavra_potencial:a palavra nao e valida.')


     #Exclui letras repetidas a mais na cadeia de caracters dada a quantidade no conjunto letras
     #Verifica a quantidade de letras presente num conjunto dado

    letras_em_comum = {}

    for i in range(len(letras)):

        if letras[i] in letras_em_comum:
            letras_em_comum[letras[i]] = letras_em_comum[letras[i]] + 1

        else:
            letras_em_comum[letras[i]]= 1

    cad_car_em_comum = {}

    for i in range(len(cad_car)):

        if cad_car[i] in cad_car_em_comum:
            cad_car_em_comum[cad_car[i]] = cad_car_em_comum[cad_car[i]] + 1

        else:
            cad_car_em_comum[cad_car[i]]= 1

    #compara a quantidade de letras na cadeia de caracteres e no tuplo de letras
    #se tiver letras a mais na cadeia de caracteres do que no conjunto dado, levanta erro

    for i in cad_car_em_comum:

        if i in letras_em_comum:
            if cad_car_em_comum[i] > letras_em_comum[i]:
                raise ValueError('cria_palavra_potencial:a palavra nao e valida.')

    return cad_car

def palavra_tamanho(palavra_potencial):

    '''
    ######### Seletor ##########
    A funcao palavra_tamanho(palavra_potencial) recebe uma palavra potencial e devolve o inteiro correspondente ao tamanho da palavra_potencial.
    ###> try_word = 'LA'
    ###> palavra_tamanho(try_word)
    ###> 2
    ############################
    '''
    return len(palavra_potencial)

def e_palavra_potencial(universal):

    '''
    ####### Reconhecedor ########
    A funcao e_palavra_potencial(universal) recebe um argumento universal e retorna True se for do tipo palavra_potencial, em contrario retorna False.
    ###> try_word = 'LA'
    ###> e_palavra_potencial(try_word)
    ###> True
    #############################
    '''
    #Verifica se e string e verifica se tem algum caracter diferente de letra maiuscula e se e string

    if isinstance(universal,str):

        for i in range(len(universal)):

            if not (64 < ord(universal[i]) < 91):
                return False

        return True

    else:

        return False


def palavras_potenciais_iguais(p1,p2):

    '''
    ######### Teste ##########
    A funcao palavras_potenciais_iguais(p1,p2) recebe duas palavras potenciais e verifica se sao iguais e devolve True se forem iguais e False se nao forem.
    ###> try_word = 'LA'
    ###> palavras_potenciais_iguais(try_word,'LA')
    ###> True
    ###> palavras_potenciais_iguais(try_word,'AL')
    ###> False
    #############################
    '''

    # Verifica se palavras sao iguais soh se tiver
    if isinstance(p1,str) and isinstance(p2,str) and palavra_tamanho(p1) == palavra_tamanho(p2) and p1 == p2:
        return True

    else:
        return False

def palavra_potencial_menor(p1,p2):

    '''
    ###### Teste ############
    A funcao palavra_potencial_menor(p1,p2) recebe duas palavras potenciais e verifica qual e a menor alfabeticamente.
    Se p1 < p2 retorna True, em contrario retorna False.
    ###> palavra_potencial_menor('META','NETA')
    ###> True
    ###> palavra_potencial_menor('METADE','META')
    ###> False
    ########################
    '''

    # Verificacao das palavras, importante ver se sao validas ou  se tem caracteres invalidos.
    if isinstance(p1,str) and isinstance(p2,str):

        for i in range(len(p1)):

            if not (64 < ord(p1[i]) < 91):
                return False

        for i in range(len(p1)):

            if not (64 < ord(p1[i]) < 91):
                return False

        # como as palavras sao do mesmo tamanho nao ha restricoes em termos de indice.
        # verifica se a letra de p1 e maior que a letra  de p2, atraves da ordem definida pela tabela de ASCII
        #Quando a p1 eh menor alfabeticamente do que p2, retorn True i == tam:

        if len(p1) == len(p2):
            i = 0
            tam = len(p2) -1

            while  i != tam:

                if ord(p1[i]) > ord(p2[i]):
                    return False

                elif ord(p1[i]) < ord(p2[i]):
                    return True

                elif ord(p1[i]) == ord(p2[i]):
                    i += 1

            return False    #i == tam:

        # como o tamanho de p1 e superior ao tamanho de p2 , o limite de verificacao e o tamnho de p2, devido aos indices.

        elif len(p1) > len(p2):
            i = 0
            tam = len(p2) -1

            while  i != tam:

                if ord(p1[i]) > ord(p2[i]):
                    return False

                elif ord(p1[i]) < ord(p2[i]):
                    return True

                elif ord(p1[i]) == ord(p2[i]):
                    i += 1

            return False        #i == tam:

        # como o tamanho de p2 e superior ao tamanho de p1 , o limite de verificacao e o tamnho de p1 por causa dos indices.

        elif len(p1) < len(p2):
            i = 0
            tam = len(p1) -1
            while  i != tam:

                if ord(p1[i]) > ord(p2[i]):
                    return False

                elif ord(p1[i]) < ord(p2[i]):
                    return True

                elif ord(p1[i]) == ord(p2[i]):
                    i += 1

            return True

    else:
        return False



def palavra_potencial_para_cadeia(p):
    '''
    ######  Trasnformador  ############
    A funcao palavra_potencial_para_cadeia(p) recebe uma palavra potencial e retorna uma string.
    ###> try_word = 'LA'
    ###> palavra_potencial_para_cadeia(try_word)
    ###> 'LA'
    ########################
    '''
    return p

#TAD Conjunto de pAlavras
'''
O TAD Conjunto_palavras vai ser utilizado geralmente para guardar conjuntos de palavras potenciais,
Este TAD contem 7 funcoes, cria_conjunto_palavras, numero_palavras, subconjunto_por_tamanho, acrescenta_palavras, e_conjunto_palavras, conjuntos_palavras_iguais e conjunto_palavras_para_cadeia.
'''

def cria_conjunto_palavras():
    '''
     ######## Criador ###########
    A funcao cria_conjunto_palavras() nao recebe nenhum argumento e devolve uma conjunto de palavras vazio
    ###> c =  cria_conjunto_palavras()
    ###> c
    ###> []
    ############################
    '''

    return []

def numero_palavras(p):
    '''
    ######### Seletor ##########
    A funcao numero_palavras(p) recebe um conjunto de palavras p e devolve um inteiro de numero de palavras contidas no conjunto.
    ###> c = ['A','E','ALE']
    ###> numero_palavras(c)
    ###> 3
    ############################
    '''
    return len(p)


def subconjunto_por_tamanho(conjunto,numero):
    '''

    ######### Transformador ##########
    A funcao subconjunto_por_tamanho(conjunto,numero) recebe dois argumentos, um conjunto e um numero.
    Retorna uma lista como as palavras do tamanho respetivo ao numero inserido.
    ###> c = ['A','E','L','LA','LE','LAE']
    ###> subconjunto_por_tamanho(c,2)
    ###> ['LA','LE']
    ############################
    '''


    a = cria_conjunto_palavras()

    # percorre o conjunto e seleciona o elemento(conjunto[n]) com o tamanho 'pedido'.

    for n in range(numero_palavras(conjunto)):

        if palavra_tamanho(conjunto[n]) == numero:

            if not conjunto[n] in a:
                a += [conjunto[n]]

    #ordena a lista

    sorted(a)

    return a

def acrescenta_palavra(conjunto,palavra_potencial):
    '''
    ####### Transformador #######
    A funcao acrescentea_palavra(conjunto,palavra_potencial) recebe dois argumentos, um conjunto e uma pontencial.
    Tem como objetivo acrescentar uma palavra ao conjunto.
    Esta funcao nao retorna nada.
    Se for introduzido algum argumento invalido, levanta erro
    ###> c = ['A','E','L']
    ###> subconjunto_por_tamanho(c,'ELA')
    ###> ['A','E','L','ELA']
    #############################
    '''

    if not isinstance(conjunto,list) or not isinstance(palavra_potencial,str):
        raise ValueError('acrescenta_palavra:argumentos invalidos.')

    #Verifica se a cadeia de caracteres tem algum caracter nao permitido, ou seja , letras minusculas e caracteres especiais

    for i in range(len(palavra_potencial)):

        if not 64 < ord(palavra_potencial[i]) < 91 :
            raise ValueError('acrescenta_palavra:argumentos invalidos.')


    # junta a palavra_potencial ao conjunto, apenas se nao estiver no conjunto

    if not palavra_potencial in conjunto:
        conjunto += [palavra_potencial]


def e_conjunto_palavras(conjunto):
    '''
   ####### Reconhecedor ########
   A funcao e_conjunto_palavras(conjunto) recebe como argumento um conjunto.
   Se for um conjunto de palavras potenciais retorna True, else retorna False.
   ###> c = ['A','E','L']
   ###> e_conjunto_palavras(c)
   ###> True
   ###> c = ['A','E','2']
   ###> e_conjunto_palavras(c)
   ###> False
   #############################
   '''


    if isinstance(conjunto,list):

        for palavra in range(len(conjunto)):

            if not e_palavra_potencial(conjunto[palavra]):
                return False

        return True


    return False

def conjuntos_palavras_iguais(p1,p2):

    '''
   ####### Teste ##############
   A funcao conjuntos_palavras_iguais(p1,p2) recebe como argumento dois conjuntos.
   Se os conjuntos de palavras forem iguais retorna True, else retorna False.
   ###> c = ['A','E','L']
   ###> c1 = ['A','E','I']
   ###> e_conjunto_palavras(c,c1)
   ###> False
   ###> c1 = ['A','E','L']
   ###> e_conjunto_palavras(c,c1)
   ###> True
   #############################
   '''
    if isinstance(p1,list) and isinstance(p2,list) and len(p1)==len(p2) and sorted(p1) == sorted(p2):
        return True

    return False

def conjunto_palavras_para_cadeia(c):
    '''
    ####### Transformador ##############
    A funcao conjunto_palavras_para_cadeia(c) recebe como argumento um conjunto.
    Se o conjunto for vazio -> [] retorna '[]'.
    Retorna o tamanho da palavra seguido '->' e o conjunto de palavras com o tamanho referido como string.
    ###> c = ['ALALALALAAL','ELA','LE']
    ###> conjunto_palavras_para_cadeia(c)
    ###> '[2->[LE];3->[ELA];11->[ALALALALAAL]]'
    ####################################

    '''

    save_tam = {}

    # organiza as palavras no conjunto por tamanho.

    for i in c:

        tamanho = palavra_tamanho(i)
        pal_str = palavra_potencial_para_cadeia(i)

        if tamanho not in save_tam:
            save_tam[tamanho] = [pal_str]

        else:
            save_tam[tamanho].append(pal_str)

    # ordenar as listas de palavras correspondentes as chaves

    for e in save_tam:
        save_tam[e].sort()

    fim = ''

    # ordena lista de tamanhos
    save_fixe = sorted(save_tam)

    # para cada tamanho e conjunto de palavras com o tamanho referido adiciona numa string.

    for i in save_fixe:

        if i != save_fixe[-1]:
            fim +=  str(i) + '->' + '[' + ', '.join(save_tam[i]) + '];'

        # ultimo elemento
        else:
            fim +=  str(i) + '->' + '[' + ', '.join(save_tam[i]) + ']'

    fim_fim = '[' + fim + ']'

    return fim_fim


#TAD Jogador
def cria_jogador(jogador):
    '''
    ####### Construtor ##############
    A funcao cria_jogador(jogador) recebe como argumento uma cadeia de caracteres e retorna um jogador.
    Se nao for do tipo str , levanta errro.
    ###> j = cria_jogador('MALUCO')
    ###> j
    ###> ['JOGADOR', 'MALUCO', 'PONTOS=', 0, 'VALIDAS=', [], 'INVALIDAS=', []]
    #############################
    '''

    if not isinstance(jogador,str):
        raise ValueError('cria_jogador:argumento invalido.')

    else:

        pontos = 0

        conjunto1 = cria_conjunto_palavras()

        conjunto2 = cria_conjunto_palavras()

        jogador = ['JOGADOR', jogador , 'PONTOS=', pontos , 'VALIDAS=', conjunto1 ,'INVALIDAS=', conjunto2 ]

        return jogador


def jogador_nome(jogador):

    '''
    ####### Seletor ##############
    A funcao jogador_nome(jogador) recebe como argumento um jogador e retorna o seu nome.
    ###> j = cria_jogador('MALUCO')
    ###> j
    ###> ['JOGADOR', 'MALUCO', 'PONTOS=', 0, 'VALIDAS=', [], 'INVALIDAS=', []]
    ###> jogador_nome(j)
    ###> 'MALUCO'
    #############################
    '''

    return jogador[1]

def jogador_pontuacao(jogador):

    '''
    ####### Seletor ##############
    A funcao jogador_pontucao(jogador) recebe como argumento um jogador e retorna a sua pontuacao.
    ###> j = cria_jogador('MALUCO')
    ###> j
    ###> ['JOGADOR', 'MALUCO', 'PONTOS=', 0, 'VALIDAS=', [], 'INVALIDAS=', []]
    ###> jogador_pontuacao(j)
    ###> 0
    #############################
    '''
    return jogador[3]

def jogador_palavras_validas(jogador):

    '''
    ####### Seletor ##############
    A funcao jogador_palavras_validas(jogador) recebe como argumento um jogador e retorna o seu conjunto de palavras validas.
    ###> j = cria_jogador('MALUCO')
    ###> j
    ###> ['JOGADOR', 'MALUCO', 'PONTOS=', 4, 'VALIDAS=', ['ELA', 'ALE'], 'INVALIDAS=', ['AL']]
    ###> jogador_palavras_validas(j)
    ###> ['ELA', 'ALE']
    #############################
    '''
    return jogador[5]

def jogador_palavras_invalidas(jogador):
    '''
    ####### Seletor ##############
    A funcao jogador_palavras_validas(jogador) recebe como argumento um jogador e retorna o seu conjunto de palavras invalidas.
    ###> j = cria_jogador('MALUCO')
    ###> j
    ###> ['JOGADOR', 'MALUCO', 'PONTOS=', 4, 'VALIDAS=', ['ELA', 'ALE'], 'INVALIDAS=', ['AL']]
    ###> jogador_palavras_invalidas(j)
    ###> ['AL']
    #############################
    '''
    return jogador[7]

def adiciona_palavra_valida(jogador,palavra_potencial):

    '''
    ####### Transformador ##############
    A funcao adicionar_palavra_valida(jogador,palavra_potencial) recebe como argumento um jogador e uma palavra_potencial.
    Se a palavra_potencial estiver no conjunto, nao adiciona nem pontua.
    Se a palavra_potencial nao estiver no conjunto, adiciona e pontua consoante o tamanho da palavra.
    Se introduzir algum palavra com parametros invalidos levanta erro.
    ###> j = cria_jogador('MALUCO')
    ###> j
    ###> ['JOGADOR', 'MALUCO', 'PONTOS=', 4, 'VALIDAS=', ['ELA', 'ALE'], 'INVALIDAS=', ['AL']]
    ###> adiciona_palavra_valida(j,'AEL')
    ###> ['JOGADOR', 'MALUCO', 'PONTOS=', 7, 'VALIDAS=', ['ELA', 'ALE', 'AEL'],'INVALIDAS=', ['AL']]
    #############################
    '''

    if not e_jogador(jogador) or not e_palavra_potencial(palavra_potencial):
        raise ValueError('adiciona_palavra_valida:argumentos invalidos.')


    elif palavra_potencial in jogador_palavras_validas(jogador):
        a = palavra_tamanho(palavra_potencial)

    else:
        a = palavra_tamanho(palavra_potencial)

        jogador[3] += a

        jogador[5] += [palavra_potencial]

def adiciona_palavra_invalida(jogador,palavra_potencial):
    '''
    ####### Transformador ##############
    A funcao adicionar_palavra_invalida(jogador,palavra_potencial) recebe como argumento um jogador e uma palavra_potencial.
    Se a palavra_potencial estiver no conjunto, nao adiciona nem pontua.
    Se a palavra_potencial nao estiver no conjunto, adiciona e pontua negativamente consoante o tamanho da palavra.
    Se introduzir algum palavra com parametros invalidos levanta erro.
    ###> j = cria_jogador('MALUCO')
    ###> j
    ###> ['JOGADOR', 'MALUCO', 'PONTOS=', 4, 'VALIDAS=', ['ELA', 'ALE'], 'INVALIDAS=', ['AL']]
    ###> adiciona_palavra_invalida(j,'L')
    ###> ['JOGADOR', 'MALUCO', 'PONTOS=', 6, 'VALIDAS=', ['ELA', 'ALE', 'AEL'],'INVALIDAS=', ['L','AL']]
    #############################
    '''
    if not e_jogador(jogador) or not e_palavra_potencial(palavra_potencial):
        raise ValueError('adiciona_palavra_invalida:argumentos invalidos.')

    elif palavra_potencial in jogador_palavras_invalidas(jogador):

        a = palavra_tamanho(palavra_potencial)

    else:
        jogador[3] -= len(palavra_potencial)

        a = palavra_tamanho(palavra_potencial)

        jogador[7] += [palavra_potencial]

def e_jogador(universal):

    '''
    #####   Reconhecedor   ######
    A funcao e_jogador(universal)  recebe um argumento universal do tipo jogador e retorna um booleano.
    ###> e_jogador([])
    ###> False
    ###> j = cria_jogador('MALUCO')
    ###> j
    ###> ['JOGADOR', 'MALUCO', 'PONTOS=', 0, 'VALIDAS=', [], 'INVALIDAS=', []]
    ###> e_jogador(j)
    ###> True
    ##############################
    '''

    if isinstance(universal,list) and universal != [] and isinstance(jogador_nome(universal),str) and isinstance(jogador_pontuacao(universal),int) and (jogador_palavras_validas(universal),list) and (jogador_palavras_invalidas(universal),list) and len(universal) == 8 :
        return True

    else:
        return False

def jogador_para_cadeia(jogador):
    '''
   ####### Transformador ##############
    A funcao jogador_para_cadeia(jogador) recebe como argumento um jogador.
    Retorna o o jogador em formato string
    ###> j = ['JOGADOR', 'MALUCO', 'PONTOS=', 6 , 'VALIDAS=', ['ELA', 'ALE', 'AEL'],'INVALIDAS=', ['L','AL']]
    ###> conjunto_palavras_para_cadeia(j)
    ###> 'JOGADOR MALUCO PONTOS=6 VALIDAS=[3->[AEL, ALE, ELA]] INVALIDAS=[1->[L];2->[AL]]'
    ####################################
    '''

    return 'JOGADOR {} PONTOS={} VALIDAS={} INVALIDAS={}'.format(jogador[1],jogador[3],conjunto_palavras_para_cadeia(jogador[5]),conjunto_palavras_para_cadeia(jogador[7]))

##################################  Funcoes Adicionais ####################################

def gera_todas_palavras_validas(letras):

    '''
    ####### Funcao Adicional #######
    A funcao gera_todas_palavras_validas gera todas as palavras possiveis dado um tuplo de letras respeitando uma gramatica.
    Se possuir caracteres invalidos, levanta erro.
    ###> gera_todas_palavras_validas(('A','E','L'))
    ###> ['A', 'E', 'LA', 'LE', 'AEL', 'ALE', 'ELA', 'LAE']
    ################################
    '''


    lst = cria_conjunto_palavras()

    tam = len(letras)

    i = 1

    while i <= tam:

        lst += list(permutations(letras,i))

        i+=1

    nova = cria_conjunto_palavras()

    #Como as permutacoes sao do tipo ('A','L','E'), este ciclo vai percorrer cada elemento dos novos tuplos criados e vai juntar todas as letras do tuplo.
    # ('A','L','E') ----> ('ALE')

    for i in range(len(lst)):

        nova.append(''.join(lst[i]))

    outro = []

    #Verifica se a palavra respeita a gramatica

    #verifica se esta no conjunto de palavras para descobrir, isto porque podem existir palavras com as mesmas letras ('A','L','A'),se for dado um tuplo com letras repetidas. Em contrario adiciona ao conjunto

    for e in range(len(nova)):

        if e_palavra(nova[e]) and cria_palavra_potencial(nova[e],letras):

            if nova[e] in outro:
                continue

            else:

                outro.append(nova[e])


    return outro



def guru_mj(tuplo):

    '''
    ###### Funcao Adicional #########
    A funcao guru_mj e a funcao principal do jogo.
    Recebe um tuplo de letras e cria a interacao do jogo.
    No fim retorna o resultado do jogo (vitoria ou empate) e os jogadores
    ###> a = ('A','E','L')
    ###> guru_mj(a)
        Descubra todas as palavras geradas a partir das letras:
        ('A', 'E', 'L')
        Introduza o nome dos jogadores (-1 para terminar)...
    ###> JOGADOR 1 -> pedro
    ###> JOGADOR 2 -> ricardo
    ###> JOGADOR 3 -> -1
         -------
         JOGADA 1 - Falta descobrir 8 palavras
    ###> JOGADOR pedro -> A
         A - palavra VALIDA
         --------
         FIM DE JOGO! O jogo terminou em empate.
         JOGADOR pedro PONTOS=9 VALIDAS=[1->[A];2->[LA];3->[AEL, ALE]] INVALIDAS=[]
         JOGADOR miguel PONTOS=9 VALIDAS=[1->[E];2->[LE];3->[ELA, LAE]] INVALIDAS=[]
    #################################
    '''

    def pede_jogador():
        '''
        ###### Funcao Adiconal #########
            ##### Auxiliar #####
        A funcao pede_jogador() nao recebe nenhum argumento, eh responsavel por pedir ao utilizador os nomes dos jogadores.
        Termina quando inserir -1
        ###> pede_jogador()
        ###> JOGADOR 1 -> pedro
        ###> JOGADOR 2 -> miguel
        ###> JOGADOR 3 -> -1
        ###############################
        '''

        save_jog = cria_conjunto_palavras()

        stop = '-1'

        ciclo = 1

        controla_jog = 0

        n = 0

        while n != stop:

            #pede um novo jogador, caso seja -1 comeca o jogo

            n = str(input('JOGADOR {} -> '.format(ciclo)))

            if n != stop:

                m = cria_jogador(n)

                save_jog.append(m)

                ciclo += 1

                controla_jog += 1

        return save_jog

    def pede_palavra(conjunto_jogadores,tuplo):

        '''
        ###### Funcao Adiconal #########
            ##### Auxiliar #####
        A funcao auxiliar pede_palavra(conjunto_jogadores,tuplo) recebe um conjunto_jogadores e um tuplo de letras.
        Cria um conjunto de palavras para descobrir.
        Eh responsavel por pedir ao utilizador para propor palavras.
        ###> pede_palavra(a,('A','E','L'))
        ###> JOGADA 1 - Falta descobrir 8 palavras
        ###> JOGADOR pedro -> A
        ###> A - palavra VALIDA
        ###> ......
        ##################################
        '''
        # Controlador de palavras propostas

        controla_palavras = cria_conjunto_palavras()

        # gera todas a palavras a descobrir

        conjunto = gera_todas_palavras_validas(tuplo)

        #numero de palavras a descobrir, valor atualizado a cada palavra introduzida

        falta_descobrir = numero_palavras(conjunto)

        cont = 1

        num_jog = numero_palavras(conjunto_jogadores)-1

        i = 0

        if falta_descobrir != 0:

            while i <= num_jog:

                jogador = conjunto_jogadores[i]

                # Informa ao utilizador quantas palavras falta descobrir e o numero da jogada

                print('JOGADA', cont, '- Falta descobrir', falta_descobrir , 'palavras')

                # informa quem eh a jogar

                print('JOGADOR',jogador_nome(jogador),'-> ',end="")

                # palavra introduzida

                tenta = str(input())

                # cria a palavra potencial

                tenta_jog= cria_palavra_potencial(tenta,tuplo)

                # se a palavra for VALIDA e ja tiver sido introduzida , passa a vez, sem pontuar.

                if tenta_jog in conjunto and tenta_jog in controla_palavras and falta_descobrir != 0:

                    print(tenta_jog,'- palavra VALIDA')

                    cont += 1

                # se palavra for Valida e nao estiver no conjunto que controla as palavras inseridas.

                elif tenta_jog in conjunto and not tenta_jog in controla_palavras and falta_descobrir != 0:

                    acrescenta_palavra(controla_palavras,tenta_jog)

                    print(tenta_jog,'- palavra VALIDA')

                    adiciona_palavra_valida(jogador,tenta_jog)

                    falta_descobrir -= 1

                    cont += 1

                #INVALIDAS
                else:
                    print(tenta_jog,'- palavra INVALIDA')

                    adiciona_palavra_invalida(jogador,tenta_jog)

                    cont += 1

                i += 1

                # Passador de vez se nao faltar descobrir mais palavras.

                if i == (num_jog + 1) and falta_descobrir != 0:
                    i = 0

                # nao ha mais palavras para receber e sair do ciclo while.

                elif falta_descobrir == 0:
                    break


             # Vencedor por ser o unico jogador.

            if numero_palavras(conjunto_jogadores) == 1:

                jo = conjunto_jogadores[0]

                print('FIM DE JOGO! O jogo terminou com a vitoria do jogador',jogador_nome(jo),'com',jogador_pontuacao(jo), 'pontos.')

                print(jogador_para_cadeia(jo))

            #   Verificador de pontos para decidir o vencedor.

            elif numero_palavras(conjunto_jogadores) > 1 :


                point = -100

                vencedor = cria_conjunto_palavras()

                # a pontuacao comeca a -100 e sempre que um jogador tenha pontucao maior que a anterior  este valor eh atulizado.
                # eh adicionado ao conjunto: vencedor , o jogador com a pontuacao maior, atualiza quando a pontuacao atualiza.

                for j in range(len(conjunto_jogadores)):

                    jo = conjunto_jogadores[j]

                    ponto = jogador_pontuacao(jo)

                    if ponto > point:

                        vencedor = jogador_nome(jo)

                        point = ponto

                    elif ponto == point:

                        vencedor = []

                        point = ponto

                    else:
                        continue

                # se houver jogadores com a mesma pontuacao.

                if vencedor == []:

                    print('FIM DE JOGO! O jogo terminou em empate.')

                    for j in range(len(conjunto_jogadores)-1):

                        jo = conjunto_jogadores[j]

                        print(jogador_para_cadeia(jo))

                    return print(jogador_para_cadeia(conjunto_jogadores[-1]))

                else:

                    print('FIM DE JOGO! O jogo terminou com a vitoria do jogador', vencedor[:],'com', point ,'pontos.')

                    for j in range(len(conjunto_jogadores)-1):

                        jo = conjunto_jogadores[j]


                        print(jogador_para_cadeia(jo))

                    return print(jogador_para_cadeia(conjunto_jogadores[-1]))


        else:
            print('FIM DE JOGO! O jogo terminou em empate.')

            for j in range(len(conjunto_jogadores)-1):

                jo = conjunto_jogadores[j]

                print(jogador_para_cadeia(jo))

            return print(jogador_para_cadeia(conjunto_jogadores[-1]))

    print('Descubra todas as palavras geradas a partir das letras:')

    print(tuplo)

    print('Introduza o nome dos jogadores (-1 para terminar)...')

    a = pede_jogador()

    if a != 0:
        pede_palavra(a,tuplo)

    # se nao for adicionado nenhum jogador

    else:
        return print('FIM DE JOGO! O jogo terminou em empate.')
