#----------------------------------------------------------------
# Una finestra amb textbox, buttons i labels
#-----------------------------------------------------------------
# Previament s'ha d'instalar la llibreria tkinter, alerta les
# diferents versions.

from tkinter import *
from tkinter import messagebox

#Primer s'han de definir les funcions dels events

def identi():
    m="Hola "+t1.get("1.0","end")
    t3.delete ("1.0","end")
    t3.insert (INSERT,"Aquí mostrarà el hash guardat")
    messagebox.showinfo(message=m, title="Saludo")
    #ha de confirmar que l'usuari és com el que es guarda al file on es va crear
    #i que la contrasenya genera el mateix hash

def crea():
        m="Generant usuari "+t1.get("1.0","end")
        t3.delete ("1.0","end")
        t3.insert (INSERT,"Aquí mostrarà el hash CREAT")
        messagebox.showinfo(message=m, title="Creant usuari")
        #ha de crear l'usuari i guardar el hash a un file

def codifica():
        t6.delete ("1.0","end")
        t6.insert (INSERT,"Codificació correcta "+t4.get("1.0","end"))
        messagebox.showinfo(message="Saving file", title="CODIFICANT")
        #aqui ha de gravar el fitxer codificat

def decodifica():
        t6.delete ("1.0","end")
        t6.insert (INSERT,"Arxiu decodificat "+t4.get("1.0","end") )
        messagebox.showinfo(message="Saving file", title="DECODIFICANT")
        #aqui ha de gravar el fitxer codificat



#Crear objecte arrel, tipus tkinter
raiz=Tk()

#Defineix el comportament de la finestra
raiz.title("Python HASH")
raiz.resizable (False, False) #tamany fix

#A dins de la finestra crea un frame
miFrame=Frame(raiz, width=800, height=300)
miFrame.pack()

#A dins del frame va creant els diferents objectes

#.....................CREAR o IDENTIFICAR-SE............................
Label (miFrame, text="Usuari").place(x=10,y=50)

#usuari
t1=Text(raiz)
t1.place(x=10,y=70) 
t1.config(width=15,height=1, font=("Consolas",12))

#contrasenya
Label (miFrame, text="Password").place(x=10,y=100)
t2=Text(raiz)
t2.place(x=10,y=120)
t2.config(width=30,height=1, font=("Consolas",12))

#botó identificar-se
button1 = Button(raiz, text="Login", command=identi)
button1.place (x=160,y=70)

#botó Crear
button2 = Button(raiz, text="Crear Usuari", command=crea)
button2.place (x=210,y=70)

#finestra on es veu el hash creant
t3=Text(raiz)
t3.place(x=10,y=150)
t3.config(width=30,height=6, font=("Consolas",12))

#....................................................................


#..................CODIFICAR EL FITXER...............................
#nom del fitxer
Label (miFrame, text="Arxiu a codificar").place(x=350,y=50)
t4=Text(raiz)
t4.place(x=350,y=70)
t4.config(width=40,height=1, font=("Consolas",12))

#botó CODIFICAR
button3 = Button(raiz, text="Codificar", command=codifica)
button3.place (x=350,y=100)

#botó DECODIFICAR
button3 = Button(raiz, text="Decodificar", command=decodifica)
button3.place (x=430,y=100)

#Resultat Codificat
t6=Text(raiz)
t6.place(x=350,y=150)
t6.config(width=40,height=2, font=("Consolas",12))
#---------------------------------------------------------------------


#Aqui fa un loop fins que es tanca la finestra
raiz.mainloop()