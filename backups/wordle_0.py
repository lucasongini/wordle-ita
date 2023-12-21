print('\033[44m  -----  WORDLE: indovina la parola  -----  \033[0m')

import random
from time import sleep

import os
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

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

maxN = int(input('Da quante lettere vuoi la parola? '))
maxtent = int(input('In quanti tentativi la vuoi indovinare? '))
print('\033[A\r\033[2K\033[A\r\033[2K', end='')

parole = open('parole.txt', "r").readlines()
dizionario = open('dizionario.txt', "r").readlines()

sn = 1
while True:
    # print('Eseguo...')
    wordle = random.choice(parole).rstrip('\n').upper()
    # print(wordle.upper())
    # print(wordle + '\n' in dizionario)
    if len(wordle) == maxN:
        if wordle.lower() + '\n' in dizionario:
            print(f'Parola scelta dopo \033[07m {sn} \033[0m controlli')
            break
    sn += 1

seq = list(wordle)

# MESSAGGI DI ERRORE
def errmsg(err):
    print(f'\033[A\033[2K\r{err}', end='')
    sleep(2.5)
    print('\033[2K\r', end='')


ntent = 1
while ntent <= maxtent:
    msg = f'Tentativo {ntent} su {maxtent}: '
    strtent = input(msg).lower()
    tent = list(strtent.upper())
    if len(tent) == maxN:
        if any(f'{strtent}\n' in x for x in parole):
            if tent == seq:
                print(f'\033[A\r\033[2K\033[42m Complimenti \033[0m Hai indovinato la parola \033[07m {wordle} \033[0m in \033[07m {ntent} tentativi \033[0m su {maxtent} disponibili')
                exit()
            else:
                provtent = f'{ntent}. '
                for i in range(maxN):
                    if tent[i] in seq:
                        if tent[i] == seq[i]:
                            provtent += f'\033[42m{tent[i]}\033[0m'
                        else:
                            provtent += f'\033[43m{tent[i]}\033[0m'
                    else:
                        provtent += tent[i]
                print(f'\033[A\r\033[2K {provtent}')
                ntent += 1
        else:
            errmsg('\033[41m Attenzione \033[0m La parola che hai inserito non è presente nel vocabolario utilizzato')
    else:
        errmsg(f'\033[41m Attenzione \033[0m Hai inserito {len(tent)} lettere quando ne servono {maxN}')

print(f'Hai perso! La parola era \033[07m {wordle} \033[0m')
exit()