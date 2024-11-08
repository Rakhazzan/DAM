from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.backends import default_backend

def creaConjuntClaus():
    clau_privada = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    clau_publica = clau_privada.public_key()
    return clau_privada, clau_publica

def saveClau(clau, nomArxiu, is_private=False):
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
    with open(nomArxiu, 'wb') as arxiu:
        arxiu.write(clau_bytes)

def loadClau(nomArxiu, is_private=False):
    with open(nomArxiu, 'rb') as arxiu:
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

def exemple():
    clau_privada, clau_publica = creaConjuntClaus()
    saveClau(clau_privada, 'clau_privada.pem', is_private=True)
    saveClau(clau_publica, 'clau_publica.pem', is_private=False)
    clau_privada_carregada = loadClau('clau_privada.pem', is_private=True)
    clau_publica_carregada = loadClau('clau_publica.pem', is_private=False)
    missatge = "Aquest és un missatge secret."
    text_xifrat = xifra(clau_publica_carregada, missatge)
    print("Text xifrat:", text_xifrat)
    text_desxifrat = desXifra(clau_privada_carregada, text_xifrat)
    print("Text desxifrat:", text_desxifrat)


exemple()
