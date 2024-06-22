
import sqlite3
from InterfaceGrafica import *

def Iniciar():
    #Cria banco de dados ou conecta a ele
    global conec
    conec = sqlite3.connect("Banco de Dados.db")

    #Cria cursor
    global cur
    cur = conec.cursor()

def Fechar():
    #Envia mudanças
    conec.commit()

    #Fecha conexão
    conec.close()

def VerificarUsuarios():
    
    Iniciar()
    #Cria tabela
    cur.execute("CREATE TABLE IF NOT EXISTS Usuarios (nome TEXT)")
    cur.execute("SELECT oid, * FROM Usuarios")
    Nomes = cur.fetchall()
    return Nomes

def AdicionarNome(Nome):
    if Nome == "Nome Usuário":
        return 0
    
    Iniciar()
    
    #Cria tabela
    cur.execute("CREATE TABLE IF NOT EXISTS Usuarios (nome TEXT)")
    cur.execute("SELECT oid, * FROM Usuarios")

    Nomes = cur.fetchall()
    for nome in Nomes:
        if nome[1] == Nome:
            return 1
    Inserir = "INSERT INTO Usuarios VALUES ('" + Nome + "')"
    cur.execute(Inserir)
    Fechar()
    return 1




