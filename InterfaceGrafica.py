from tkinter import *
import tkinter as ttk
from GerenciadorDeUsuários import *
from Simulados import *
import math

#Classe gerenciadora de interface.


class GerenciadorDeSimulados:
    #Define método de inicialização
    def __init__(self, master):
        self.master = master
        #self.GUI_list = []
        return
        ######################################################## 
    #Inicia o gerenciador.
    def __IniciarGerenciador__(r):

        #Dados da interface
        CaminhoDoIcone = r"Aprendizado\Gerenciador de Simulados\Ícones\Gerenciador de Simulados - Ícone.ico"
        NomeDoPrograma  = "Gerenciador de Simulados"
        global root
        root = r
        #Cria a tela dentro da tela do programa
        root.title(NomeDoPrograma)  
        root.iconbitmap(CaminhoDoIcone)
        root.state('zoomed')
        root.columnconfigure(0, weight=1)
        root.rowconfigure(1, weight=1)

        #Cria os frames do programa
        global menu
        menu = ttk.Frame(root, name="menu")
        menu.grid(column=0, row=0, columnspan=3)
        ttk.Label(menu, text="Menu: ").grid(column=0,row=0)
        global tela
        tela = ttk.Frame(root, name="tela")
        tela.grid(column=0,row=1)
        return
        ######################################################## 
    #Tela de adicionar novos usuários.
    def AdicionarUsuario():
        GDS.LimparJanela(tela)
        #Adiciona texto à tela
        GDS.Titulo(tela,"Nome:",0,0)
        global usuario
        usuario = "Nome Usuário"
        #Adiciona campo para inserir texto à tela
        e = Entry(tela)
        e.grid(column=0,row=1)
        e.insert(0, "Nome Usuário")

        #Adiciona botão à tela
        ttk.Button(tela, text="Enter", command=lambda: GDS.Voltar(e.get())).grid(column=0,row=2)
        return
        ########################################################     
    def Voltar(Nome):
        AdicionarNome(Nome)
        usuarios = VerificarUsuarios()

        if usuarios == []:
            GDS.AdicionarUsuario()
            return
        
        GerenciadorDeSimulados.EscolherUsuario()
        return
        ########################################################       
    def EscolherUsuario():
        GDS.LimparJanela(tela)
        
        #Adiciona texto à tela
        usuarios = VerificarUsuarios()

        listadeusuarios = ttk.Frame(tela, name="listadeusuarios")
        listadeusuarios.grid(column=0, row=1)

        #Cria lista com apenas nomes de usuários
        nome_usuarios = []
        for user in usuarios:
            nome_usuarios.append(user[1])
        
        #Cria menu de seleção de usuarios
        usuario_escolhido = ttk.StringVar(listadeusuarios)
        usuario_escolhido.set("Selecione o usuário")
        

        ttk.OptionMenu(listadeusuarios, usuario_escolhido, *nome_usuarios).grid(column=1, row=1, pady=50)



        #Adiciona botão de enter à tela
        ttk.Button(tela, text="Enter", command=lambda: GDS.EscolherSimulado(usuario_escolhido)).grid(column=0,row=2, pady=75)

        #Muda para tela de adicionar novo usuário
        ttk.Button(tela, text="Adicionar novo Usuário", command=lambda: GDS.AdicionarUsuario()).grid(column=0,row=3)


        return  
    def EscolherSimulado(usuario_escolhido):
        GDS.LimparJanela(tela)
        global usuario
        usuario = usuario_escolhido.get()
        GDS.Titulo(tela,usuario,0,0)
        listasimulados = VerificarSimulados(usuario)
        

        if listasimulados == []:
            GDS.TelaAdicionarSimulado()
        else:
            #Exibe Simulados
            GDS.Titulo(tela,"Lista de Simulados",0,0)
            simulado_escolhido = ttk.StringVar(tela)
            simulado_escolhido.set("Escolha o Simulado")
            ttk.OptionMenu(tela, simulado_escolhido, *listasimulados).grid(column=0, row=1, pady=50)
            ttk.Button(tela, text="+",command=lambda: GDS.TelaAdicionarSimulado()).grid(column=1,row=1)
            ttk.Button(tela, text="Enter",command=lambda: GDS.TelaDoSimulado()).grid(column=0,row=3,columnspan=2)

        #Adiciona botões "Adicionar Simulado" e "Enter"

        
        


        return
        ######################################################## 
    def TelaAdicionarSimulado():
        GDS.LimparJanela(tela)
        GDS.Titulo(tela,"Adicionar Simulado",0,0,2)
        InfoSimulado=["Banca", "Orgão", "Cargo"]
        simulados = ttk.Frame(tela, name="simulados")
        simulados.grid(column=1,row=1)
        textos = ttk.Frame(tela, name="textos")
        textos.grid(column=0,row=1)
        n = 1
        ValoresObtidos = []
        for Info in InfoSimulado:
            n = n + 1
            ValoresObtidos.append(GDS.Inserir(Info,"Nome do(a) "+Info,n,1,simulados))
            GDS.Inserir(Info,Info+":",n, 0, textos, "Texto")
        Questões=GDS.Inserir("Equantidade", "70", n+1,1,simulados)
        GDS.Inserir("Tquantidade", "Quantidade de questões:", n+1,0,textos, "Texto")
        ttk.Button(tela, text="Enter",command=lambda: GDS.TelaDeRespostas(Questões,ValoresObtidos)).grid(column=0,row=3,columnspan=2)
        return
        ######################################################## 
    def TelaDoSimulado(usuario):
        GDS.LimparJanelaSimulado(tela)
        #Adiciona texto à tela
        GDS.Titulo(tela,"Simulado:",0,0)
        return 
    def TelaDeRespostas(questoes, valores):
        
        try:
            NumQuestoes = int(questoes.get())
            1/NumQuestoes 
            
        except:
            Aviso = Toplevel(root)
            Aviso.title("Aviso")
            Mensagem = Label(Aviso, text='Valor digitado:"'+questoes.get()+'".Você precisa inserir um número de questões no formato válido e maior que 0. "01..."')
            Mensagem.grid(column=0,row=0, padx= 25, pady = 12)
            return      
        Banca= valores[0].get()
        Orgao= valores[1].get()
        Cargo= valores[2].get()
        GDS.LimparJanela(tela)
        QMarcadas = []
        Titulo = GDS.Titulo(tela,"Insira suas RESPOSTAS:",1,0,int(NumQuestoes/10)*2)
        for n in range(1,NumQuestoes+1):
            QMarcadas.append(GDS.Inserir(Nome = "Numeros"+str(n),Texto= "A",Linha = math.ceil((n-0.1)%10),Coluna=math.ceil(n/10)*2))
            GDS.Inserir("Questão"+str(n),n,math.ceil((n-0.1)%10),(math.ceil(n/10)*2)-1,Tipo="Label")
        Botao = ttk.Button(tela, text="Enter")
        Botao.grid(column=1,row=11,columnspan=int(NumQuestoes/10)*2)
        Botao.configure(command=lambda: GDS.TelaDeGabarito(Banca,Orgao,Cargo, NumQuestoes,QMarcadas,Titulo, Botao))
        return
    
    def TelaDeGabarito(Banca,Orgao,Cargo,NumQuestoes,QMarcadas,Titulo, Botao):
        Titulo.configure(text="Insira o GABARITO")
        LetrasMarcadas = []
        for questao in QMarcadas:
            LetrasMarcadas.append(questao.get())
        for questao in QMarcadas:
            questao.delete(0,END)
            questao.insert(0,"B")
        Botao.configure(text="Enter",command=lambda: GDS.SalvarSimulado(Banca,Orgao,Cargo, NumQuestoes,LetrasMarcadas,QMarcadas))
        return
        
    
    def SalvarSimulado(Banca,Orgao,Cargo, NumQuestoes,LetrasMarcadas,QMarcadas):
        QGabarito = []
        for questao in QMarcadas:
            QGabarito.append(questao.get())

        CriarSimulado(usuario, Banca,Orgao,Cargo, NumQuestoes,LetrasMarcadas,QGabarito)
        GDS.EscolherUsuario()
        return
    def Titulo(Janela,Texto,Coluna, Linha, EspacoColuna = 1):
        Titulo = ttk.Label(Janela,name="h1", text=Texto)
        Titulo.grid(column=Coluna, row=Linha, columnspan = EspacoColuna)
        return Titulo
    def LimparJanela(Tela):
        for child in Tela.winfo_children():
         child.destroy()
    def Inserir(Nome: "str", Texto: "str" = "Insira seu texto aqui", Linha: "int" = 1, Coluna: "int" = 0, Janela: "Frame" = "tela", Tipo: "str" = "Entry") -> "Entry":
        if Janela == "tela": Janela = tela
        Nome = Nome.lower()
        match Tipo:
            case "Entry" | "Entrada":
                e = Entry(Janela, name= Nome)
                e.insert(0, Texto)
                e.grid(column= Coluna,row= Linha)
                return e
            case "Label" | "Texto":
                l = Label(Janela, name= Nome, text=Texto)
                l.grid(column= Coluna,row= Linha)
                return l
                
        
        
        
        ################################################################

    #_______________________________________________________________
GDS = GerenciadorDeSimulados