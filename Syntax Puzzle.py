#Pedro Cabral, ist190767

artigo_def = ("A","O")
vogal_palavra = artigo_def + ("E",)
vogal  = vogal_palavra + ("I","U")
ditongo_palavra = ("AI","AO","EU","OU")
ditongo = ditongo_palavra + ("AE","AU","EI","OE","OI","IU")
par_vogais = ditongo + ("IA","IO")
consoante_freq = ("D","L","M","N","P","R","S","T","V")
consoante_terminal = ("L","M","R","S","X","Z")
consoante_final = ("N","P") + consoante_terminal
consoante = ("B","C","D","F","G","H","J","L","M","N","P","Q","R","S","T","V","X","Z")
par_consoantes = ("BR","CR","FR","GR","PR","TR","VR","BL","CL","FL","GL","PL")

def monossilabo_2(word):
    '''
    Esta funcao verifica toda a palavra que contem duas silabas.
    '''
    if word[0] in vogal_palavra and word[1] == "S": # vogal palavra + "S" --> AS
        return True
    elif word in ("AR","IR","EM","UM"):
        return True
    elif word in ditongo_palavra:
        return True
    elif word[0] in consoante_freq and word[1] in vogal:# consoante frequente + vogal ----> LA or LI
        return True
    else:
        return False # as or Ar

def monossilabo_3(word):
    '''
    Esta funcao verifica todas as palavras de 3 silabas.
    '''
    if word[0] in consoante and word[1:] in ditongo: #consoante + ditongo ---> SAO or POE
        return True
    elif word[0] in consoante and word[1] in vogal and word[2] in consoante_terminal: # consoante + vogal + consoante terminal ---> LOL or PIZ
        return True
    elif word[:2] in par_vogais and word[2] in consoante_terminal: # par de vogais + consoante terminal ---> AER
        return True
    else:
        return False # PIB or NIB

def e_monossilabo(word):
    '''
    Esta funcao verifica todas as palavras com 1 , 2 e 3 silabas.
    '''
    if  (not isinstance(word,str)):
        raise ValueError("e_monossilabo:argumento invalido")  #
    elif len(word) == 0:
            raise ValueError("e_monossilabo:argumento invalido")
    elif len(word) == 1 and word in vogal_palavra:
        return True
    elif len(word) == 2 and monossilabo_2(word):
        return True
    elif len(word) == 3 and monossilabo_3(word):
        return True
    else:
        return False
def silaba_2(word):
    '''
    Esta funcao verifica todas as palavras de 2 silabas.
    '''
    if word in par_vogais :
        return True
    elif word[0] in consoante and word[1] in vogal:
        return True
    elif word[0] in vogal and word[1] in consoante_final:
        return True
    else:
        return False
def silaba_3(word):
    '''
    Esta funcao verifica todas as palavras de 3 silabas.
    '''
    if word in ("QUA","QUE","QUI","GUE","GUI","ANS","ENS","INS","ONS","UNS"): #verifica se word esta no tupulo
        return True
    elif word[0] in consoante and word[1:] in par_vogais:# consoante + par_vogais ---> CIO
        return True
    elif word[0] in consoante and word[1] in vogal and word[2] in consoante_final: #consoante + vogal + consoante_final --> COFR
        return True
    elif word[:2] in par_vogais and word[2] in consoante_final: # par_vogais + consoante_final ---> AIBR
        return True
    elif word[:2] in par_consoantes and word[2] in vogal: # par_consoantes + vogal ---> CRU
        return True
    else:
        return False #retorna qq palavra fora da gramatica ---> PAO
def silaba_4(word):
    '''
    Esta funcao verifica todas as palavras de 4 silabas.
    '''
    if word[:2] in par_vogais and word[2:] == "NS": #duas vogais + "NS" ---> AENS
        return True
    elif word[0] in consoante and word[1] in vogal and word[2:] == "NS": # consoante + vogal + "NS" --> PANS
        return True
    elif word[0] in consoante and word[1] in vogal and word[2:] == "IS": # consoante + vogal + "IS" ---> PAIS or TEIS
        return True
    elif word[:2] in par_vogais and word[2:] in par_consoantes:# par de vogais + par de consoantes --> AEBR or IUPL
        return True
    elif word[0] in consoante and word[1:3] in par_vogais and word[3] in consoante_final:# consoante + par de vogais + consoante final ---> CAIR or LIUM
        return True
    else:
        return False # todos os casos que nao respeitam a gramatica, alguns ---> LUAM or CUAM

def silaba_5(word):
    '''
    Esta funcao verifica todas as palavras de 5 silabas.
    '''
    if word[:2] in par_consoantes and word [2] in vogal and word[3:] == "NS": # par de consoantes + vogal + "NS" ----> PRONS or VRINS
        return True
    else:
        return False # todos os casos que nao respeitam a gramatica, alguns --->  GMOMO or TROLL or CTINS

def silaba_final(word):
    '''
    Esta funcao verifica todas as palavras de que reunam condicoes,
    para serem consideradas silabas-finais de acordo com  a gramatica.
    '''
    if len(word) == 2 and monossilabo_2(word): # verifica se o tamanho da palavra e 2 e verifica se e monossilabo_2
        return True
    elif len(word) == 3 and monossilabo_3(word):# verifica se o tamanho da palavra e 3 e verifica se e monossilabo_3
        return True
    elif len(word) == 4 and silaba_4(word):# verifica se o tamanho da palavra e 4  e verifica se e silaba_4
        return True
    elif len(word) == 5 and silaba_5(word): #  verifica se o tamanho da palavra e 5  e verifica se e silaba_5
        return True
    else:
        return False # retorna qualquer palavra que nao respeite as condicoes acima referidas --> A or I

def e_silaba(word):

    '''
    Esta funcao verifica se a word e silaba

    '''
    if  (not isinstance(word,str)):
        raise ValueError("e_silaba:argumento invalido") # se introduzir int, tuple or list ----> error
    elif len(word) == 0:
            raise ValueError("e_silaba:argumento invalido") # corresponde ao vazio ---> ()  --->>> error
    elif len(word) == 1 and word in vogal: # se o tamanho da word for igual a 1 , verifica a condicao
        return True
    elif len(word) == 2 and silaba_2(word):# se o tamanho da word for igual a 2 , verifica a condicao
        return True
    elif len(word) == 3 and silaba_3(word):# se o tamanho da word for igual a 3 , verifica a condicao
        return True
    elif len(word) == 4 and silaba_4(word):# se o tamanho da word for igual a 4 , verifica a condicao
        return True
    elif len(word) == 5 and silaba_5(word):# se o tamanho da word for igual a 5 , verifica a condicao
        return True
    else:
        return False #se o tamanho da word for superior > a 5 retorna falso



def e_palavra(word):
    '''
    A funcao e_palvra(word) verifica se a word inserida esta na gramatica.
    '''
    if not(isinstance(word,str)):
        raise ValueError("e_palavra:argumento invalido")# se introduzir int, tuple or list ----> error
    elif len(word) == 0:
        raise ValueError("e_palavra:argumento invalido")# corresponde ao vazio ---> ()  --->>> error
    elif e_monossilabo(word):
        return True
    elif silaba_final(word):
        return True
    elif not e_monossilabo(word):

        maior_SF = ""
        for i in range(len(word)-1,-1,-1):
            fim_palavra = word[i:]

            # verifica se e silaba final. Escolhe a maior silaba final.
            if silaba_final(fim_palavra) or (maior_SF != "" and len(fim_palavra)> 5) or (maior_SF != "" and len(fim_palavra) == len(word)):
                if (len(word)-1 - i) <= 5 and len(fim_palavra) <=5 and silaba_final(fim_palavra):
                    maior_SF = fim_palavra
                    if len(word) >6:
                        continue
                    elif len(fim_palavra) < len(word):
                        continue

                palavra_sem_fim = word[:-len(maior_SF)]


                while len(palavra_sem_fim) !=0: # Forma iterativa
                    existe_silaba = False

                    # Vai criar o pedaco para analisar se e silaba

                    if len(palavra_sem_fim) > 5:
                        p_dividida  = palavra_sem_fim[-5:]
                    else:
                        p_dividida = palavra_sem_fim

                    # Vai verificar se o pedaco e silaba

                    for i in range(len(p_dividida)):
                        if e_silaba(p_dividida[i:]):
                            existe_silaba = True

                            # Actualiza a variavel que e a condicao de paragem
                            # removendo do fim da palavra a silaba.
                            palavra_sem_fim = palavra_sem_fim[:len(palavra_sem_fim)- len(p_dividida[i:])]
                            break
                        else:
                            existe_silaba = False
                    if not(existe_silaba):
                        return False
                return True
        return False
    
