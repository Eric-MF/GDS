import sqlite3

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

def VerificarSimulados(NomeUsuario):
    Iniciar()
    #Cria table de Simulados
    cur.execute("CREATE TABLE IF NOT EXISTS Simulados (nome TEXT, simulado TEXT)")
    cur.execute("SELECT oid, * FROM Simulados")
    Simulados = cur.fetchall()
    #print(Simulados)
    Fechar()
    return Simulados
def CriarSimulado(Banca: "str",Orgao: "str",Cargo: "str", NumQuestoes: "str"):
    print(Banca)
    print(Orgao)
    print(Cargo)
    print(NumQuestoes)
    return