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

def VerificarSimulados(NomeUsuario: "str"):
    Iniciar()
    #Cria table de Simulados
    cur.execute("CREATE TABLE IF NOT EXISTS Simulados (usuario TEXT, numero TEXT, banca TEXT,orgao TEXT,cargo TEXT,resposta TEXT,gabarito TEXT)")
    cur.execute('SELECT numero, banca, orgao, cargo FROM Simulados WHERE usuario = "' + NomeUsuario + '" group by numero'  )
    Simulados = cur.fetchall()
    print (NomeUsuario)
    print(Simulados)
    Fechar()
    return Simulados
def CriarSimulado(usuario: "str", Banca: "str",Orgao: "str",Cargo: "str", NumQuestoes: "str",LetrasMarcadas: "list",QGabarito: "list"):
    
    Iniciar()
    #Cria table de Simulados
    cur.execute("CREATE TABLE IF NOT EXISTS Simulados (usuario TEXT, numero TEXT, banca TEXT,orgao TEXT,cargo TEXT,resposta TEXT,gabarito TEXT)")
    cur.execute("SELECT oid, * FROM Simulados")
    Simulados = cur.fetchall()
    cur.execute("SELECT numero, count(*) from Simulados group by numero;")
    SimuladosAnteriores = cur.fetchall()
    NovoSimulado = len(SimuladosAnteriores)+1
    LetrasMarcadas = list(LetrasMarcadas)
    QGabarito = list(QGabarito)
    for n in range(0,NumQuestoes):
        Inserir = "INSERT INTO Simulados VALUES ('" + usuario + "','" + str(NovoSimulado) + "','" + Banca + "','" + Orgao + "','" + Cargo + "','" + LetrasMarcadas[n] + "','" + QGabarito[n] + "')"
        cur.execute(Inserir)

    Fechar()
    return 1
def VerificarPorcentagem(Usuario: "str", Identificador: "str"):
    Iniciar()
    comando = "SELECT count(*) from Simulados WHERE numero = " + Identificador + " AND usuario = '" + Usuario+"'"
    cur.execute(comando)
    Total = cur.fetchall()
    Total = Total[0][0]
    comando = "SELECT count(*) from Simulados WHERE numero = " + Identificador + " AND usuario = '" + Usuario +"' AND resposta = gabarito"
    cur.execute(comando)
    Acertos = cur.fetchall()
    Acertos = Acertos[0][0]
    if Acertos == 0 or Total ==0:
        porcentagem = 0
    else:
        porcentagem = Acertos / Total

    Fechar()
    return  f"{porcentagem:.2%}"