user_input = input("Escriu una paraula\n")

word = str(user_input)

def xifrar(x):
    letras = []
    xifrar_letras = []
    for letra in x:
        letras.append(ord(letra) + 1)
        xifrar_letras.append(chr(ord(letra) + 1))
    
    print("Code points:", letras)
    print("Encrypted letters:", ''.join(xifrar_letras))

xifrar(word)