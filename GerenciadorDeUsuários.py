
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
    cur.execute("CREATE TABLE IF NOT EXISTS Usuarios (nome TEXT, simulados TEXT)")
    cur.execute("SELECT oid, * FROM Usuarios")
    Nomes = cur.fetchall()

    return Nomes

def AdicionarNome(Nome):
    Iniciar()
    
    #Cria tabela
    cur.execute("CREATE TABLE IF NOT EXISTS Usuarios (nome TEXT, simulados TEXT)")
    cur.execute("SELECT oid, * FROM Usuarios")

    Nomes = cur.fetchall()

    Inserir = "INSERT INTO Usuarios VALUES ('" + Nome + "','Simulados')"
    cur.execute(Inserir)
    Fechar()
    return




