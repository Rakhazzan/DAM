import os
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.backends import default_backend
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Ruta base per desar tots els fitxers
ruta_base = "C:/Users/Mohamed/Documents/DAM/M09/Tasca 6. Encriptació asimètrica"

# Funció per crear un conjunt de claus RSA (pública i privada)
def creaConjuntClaus():
    clau_privada = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    clau_publica = clau_privada.public_key()
    return clau_privada, clau_publica

# Funció per desar una clau (pública o privada) en un fitxer
def saveClau(clau, nom_fitxer, is_private=False):
    ruta_completa = os.path.join(ruta_base, nom_fitxer)
    if is_private:
        clau_bytes = clau.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        )
    else:
        clau_bytes = clau.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
    with open(ruta_completa, 'wb') as arxiu:
        arxiu.write(clau_bytes)

# Funció per carregar una clau (pública o privada) des d'un fitxer
def loadClau(nom_fitxer, is_private=False):
    ruta_completa = os.path.join(ruta_base, nom_fitxer)
    with open(ruta_completa, 'rb') as arxiu:
        clau_bytes = arxiu.read()
        if is_private:
            clau = serialization.load_pem_private_key(
                clau_bytes,
                password=None,
                backend=default_backend()
            )
        else:
            clau = serialization.load_pem_public_key(
                clau_bytes,
                backend=default_backend()
            )
    return clau

# Funció per xifrar un text amb una clau pública
def xifra(clauPublica, text_a_xifrar):
    text_bytes = text_a_xifrar.encode('utf-8')
    xifrat = clauPublica.encrypt(
        text_bytes,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return xifrat

# Funció per desxifrar un text amb una clau privada
def desXifra(clauPrivada, text_xifrat):
    desxifrat = clauPrivada.decrypt(
        text_xifrat,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return desxifrat.decode('utf-8')

# Funció per generar un PDF amb les claus
def generaPDFClaus(nom_pdf, clau_privada_path, clau_publica_path):
    ruta_pdf = os.path.join(ruta_base, nom_pdf)
    clau_privada_ruta_completa = os.path.join(ruta_base, clau_privada_path)
    clau_publica_ruta_completa = os.path.join(ruta_base, clau_publica_path)
    
    # Llegim les claus dels fitxers
    with open(clau_privada_ruta_completa, 'rb') as f:
        clau_privada = f.read().decode('utf-8')
    with open(clau_publica_ruta_completa, 'rb') as f:
        clau_publica = f.read().decode('utf-8')
    
    # Creem el document PDF
    c = canvas.Canvas(ruta_pdf, pagesize=letter)
    c.drawString(100, 750, "Conjunt de Claus RSA")
    
    # Escriu la clau pública al PDF
    c.drawString(100, 730, "Clau Pública:")
    y_pos = 710
    for line in clau_publica.splitlines():
        c.drawString(100, y_pos, line)
        y_pos -= 15
    
    # Escriu la clau privada al PDF
    c.drawString(100, y_pos - 20, "Clau Privada:")
    y_pos -= 40
    for line in clau_privada.splitlines():
        c.drawString(100, y_pos, line)
        y_pos -= 15
    
    # Guarda el PDF
    c.save()
    print(f"PDF generat amb les claus: {ruta_pdf}")

# Exemple de funcionament
def exemple():
    # Crear un conjunt de claus (pública i privada)
    clau_privada, clau_publica = creaConjuntClaus()

    # Desar les claus en fitxers
    saveClau(clau_privada, 'clau_privada.pem', is_private=True)
    saveClau(clau_publica, 'clau_publica.pem', is_private=False)

    # Carregar les claus des dels fitxers
    clau_privada_carregada = loadClau('clau_privada.pem', is_private=True)
    clau_publica_carregada = loadClau('clau_publica.pem', is_private=False)

    # Text a xifrar
    missatge = "Aquest és un missatge secret."

    # Xifrar el missatge amb la clau pública
    text_xifrat = xifra(clau_publica_carregada, missatge)
    print("Text xifrat:", text_xifrat)

    # Desxifrar el missatge amb la clau privada
    text_desxifrat = desXifra(clau_privada_carregada, text_xifrat)
    print("Text desxifrat:", text_desxifrat)

    # Generar el PDF amb les claus
    generaPDFClaus('claus_RSA.pdf', 'clau_privada.pem', 'clau_publica.pem')

# Executa l'exemple per mostrar el funcionament de les funcions
exemple()
