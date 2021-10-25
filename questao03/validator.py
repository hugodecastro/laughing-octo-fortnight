#! /usr/bin/env python

def verifica_pares(cdvpy):
    digitos = []
    while cdvpy > 0:
        digitos.append(cdvpy % 10)
        cdvpy = int(cdvpy/10)
    digitos = digitos[::-1]
    if ((digitos[0] == digitos[2] and digitos[1] == digitos[3]) or
       (digitos[1] == digitos[3] and digitos[2] == digitos[4]) or
       (digitos[2] == digitos[4] and digitos[3] == digitos[5])):
       return False
    else:
        return True

def valida_cdvpy(cdvpy):
    if str(cdvpy).isnumeric():
        codigo = int(cdvpy)
        if len(str(cdvpy)) > 6:
            return False
        return verifica_pares(codigo)
    else:
        return False

if __name__ == '__main__':
    cdvpy = input('Digite um CDvPy:')
    print(valida_cdvpy(cdvpy))