user_input = input("Opcions\n 1.- Xifrar \n 2.- Desxifrar\n")
option = int(user_input)

def xifrar(x):
    letras = []
    xifrar_letras = []
    for letra in x:
        if ord(letra)==122 :
             letras.append(ord(letra)-25)
             xifrar_letras.append(chr(ord(letra)-25))
        else:
            letras.append(ord(letra)+1)
            xifrar_letras.append(chr(ord(letra)+1))
    
    print("Numeros ASCII:", letras)
    print("Paraula encriptada:", ''.join(xifrar_letras))


def desxifrar(x):
    letras = []
    desxifrar_letras = []
    for letra in x:
         if ord(letra)==97 :
             letras.append(ord(letra)+25)
             desxifrar_letras.append(chr(ord(letra)+25))
         else:
            letras.append(ord(letra)-1)
            desxifrar_letras.append(chr(ord(letra)-1))
    
    print("Numeros ASCII:", letras)
    print("Paraula desencriptada:", ''.join(desxifrar_letras))

user_input = input("Escriu una paraula\n")
word = str(user_input)
if option==1 :
    xifrar(word)
if option==2 :
    desxifrar(word)