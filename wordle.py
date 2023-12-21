import os

os.system('cls' if os.name=='nt' else 'clear')

print('\033[44m                                                  \033[0m')
print('\033[44m          WORDLE ITA: indovina la parola          \033[0m')
print('\033[44m              Creato da luca.songini              \033[0m')
print('\033[44m                                                  \033[0m')
print('Caricamento...')




import random
from time import sleep

# apri i file contenenti le parole
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

paroleDict = open('parole.txt', "r")
parole = paroleDict.readlines()
paroleDict.close()


# ricava il numero massimo di lettere possibili in una parola, controllando tutto l'elenco di parole
maxLen = len(max(parole, key = len)) - 1


# \033[07m sfondo invertito
# \033[42m sfondo verde
# \033[43m sfondo giallo
# \033[0m reset
# \033[A freccia su
# \033[2K cancella riga

# 30 – Black
# 31 – Red
# 32 – Green
# 33 – Yellow
# 34 – Blue
# 35 – Magenta
# 36 – Cyan
# 37 – White

class cod:
    up = '\033[A\r' # UP ARROW
    clr = '\033[2K\r' # CLEAR LINE
    upClr = '\033[A\033[2K\r' # UP ARROW AND CLEAR LINE

class col:
    res = '\033[0m' # RESET
    inv = '\033[07m' # INVERTED
    r = '\033[41m' # RED
    g = '\033[42m' # GREEN
    y = '\033[43m' # YELLOW
    b = '\033[44m' # BLUE




# MESSAGGI DI ERRORE
def errmsg(err):
    print(cod.upClr, cod.upClr, col.r, 'Attenzione', col.res, err)
    sleep(2.5)
    print(cod.upClr, end='')

# CHIEDI INPUT E VERIFICA SE INT
def askInt(msg, max):
    while True:
        res = input(msg)
        if res.isnumeric() and int(res) <= max: # controlla che l'input inserito sia un int
            return int(res)
        else:
            errmsg(f'Inserisci un numero tra 0 a {max}')



# impostazioni preliminari
print(cod.upClr, end='')
maxN = askInt('Da quante lettere vuoi la parola?\n> ', maxLen)
maxtent = askInt('In quanti tentativi la vuoi indovinare?\n> ', 100)
print(cod.upClr, cod.upClr, cod.upClr, cod.upClr, end='')




# PAROLA INDOVINATA
def successmsg(word, n):
    print(f'{cod.upClr}{cod.upClr}{col.g} Complimenti {col.res} Hai indovinato la parola {col.inv} {word} {col.res} in {col.inv} {n} tentativi {col.res} su {maxtent} disponibili')




checkIndex = 1
while True:
    wordle = random.choice(parole).rstrip('\n').upper() # seleziona una parola a caso
    if len(wordle) == maxN: # controlla che la parola sia della lunghezza richiesta
        print(f'Parola scelta dopo {col.inv} {checkIndex} {col.res} randomizzazioni')
        break
    checkIndex += 1
    print(checkIndex, wordle, ' '*10,end='\r')



seq = list(wordle) # converte la parola scelta in una lista di lettere


# inizia il gioco
ntent = 1
while ntent <= maxtent:
    strtent = input(f'Tentativo {ntent} su {maxtent}:\n> ').lower() # chiede all'utente un input per il nuovo tentativo
    tent = list(strtent.upper()) # converte il tentativo in MAIUSCOLO e crea una lista delle lettere
    if len(tent) == maxN: # controlla che la parola sia della lunghezza richiesta
        if any(f'{strtent}\n' in x for x in parole): # controlla se la parola inserita dall'utente è presente nell'elenco
            if tent == seq:
                successmsg(wordle, ntent)
                exit()
            else:
                provtent = f'{ntent}. ' # inserisce il numero del tentativo
                for i in range(maxN):
                    if tent[i] in seq: # controlla se la lettera della parola inserita è presente nella parola casuale
                        if tent[i] == seq[i]: # controlla se la lettera della parola inserita è nella posizione corretta
                            provtent += f'{col.g}{tent[i]}{col.res}' # colora di VERDE la lettera e la inserisce nel tentativo
                        else:
                            provtent += f'{col.y}{tent[i]}{col.res}' # colora di GIALLO la lettera e la inserisce nel tentativo
                    else:
                        provtent += tent[i] # inserisce la lettera nel tentativo senza cambiarne il colore
                print(f'{cod.upClr}{cod.upClr} {provtent}')
                ntent += 1
        else:
            errmsg('La parola che hai inserito non è presente nel vocabolario utilizzato')
    else:
        errmsg(f'Hai inserito {len(tent)} lettere quando ne servono {maxN}')

print(f'Hai perso! La parola era {col.inv} {wordle} {col.res}')
exit()