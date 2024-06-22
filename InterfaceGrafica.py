from tkinter import *
import tkinter as ttk
import os
from GerenciadorDeUsuários import *
from Simulados import *

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
        for usuario in usuarios:
            nome_usuarios.append(usuario[1])
        
        #Cria menu de seleção de usuarios
        usuario_escolhido = ttk.StringVar(listadeusuarios)
        usuario_escolhido.set("Selecione o usuário")
        ttk.OptionMenu(listadeusuarios, usuario_escolhido, *nome_usuarios).grid(column=1, row=1, pady=50)



        #Adiciona botão de enter à tela
        ttk.Button(tela, text="Enter", command=lambda: GDS.EscolherSimulado(usuario_escolhido.get())).grid(column=0,row=2, pady=75)

        #Muda para tela de adicionar novo usuário
        ttk.Button(tela, text="Adicionar novo Usuário", command=lambda: GDS.AdicionarUsuario()).grid(column=0,row=3)


        return  
    def EscolherSimulado(usuario):
        GDS.LimparJanela(tela)

        GDS.Titulo(tela,usuario,0,0)
        listasimulados = VerificarSimulados(usuario)
        

        if listasimulados == []:
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
            Questões=GDS.Inserir("Equantidade", "00", n+1,1,simulados)
            GDS.Inserir("Tquantidade", "Quantidade de questões:", n+1,0,textos, "Texto")
            ttk.Button(tela, text="Enter",command=lambda: GDS.EnviarDadosSimulado(Questões,ValoresObtidos)).grid(column=0,row=3,columnspan=2)
            ttk.Button(tela, text="apagar simulado",command=lambda: GDS.LimparJanela(simulados)).grid(column=0,row=4)
        else:
            #Exibe Simulados
            GDS.Titulo(tela,"Lista de Simulados",0,0)
            simulado_escolhido = ttk.StringVar(tela)
            simulado_escolhido.set("Escolha o Simulado")
            ttk.OptionMenu(tela, simulado_escolhido, *listasimulados).grid(column=0, row=1, pady=50)
            ttk.Button(tela, text="+",command=lambda: GDS.TelaDoSimulado(usuario, True)).grid(column=1,row=1)
            ttk.Button(tela, text="Enter",command=lambda: GDS.TelaDoSimulado(usuario)).grid(column=0,row=3,columnspan=2)

        #Adiciona botões "Adicionar Simulado" e "Enter"

        
        


        return
        ######################################################## 
    def TelaDoSimulado(usuario, AdicionarSimulado = False ):
        GDS.LimparJanelaSimulado(tela)
        #Adiciona texto à tela
        GDS.Titulo(tela,"Simulado:",0,0)
        return 
    def EnviarDadosSimulado(questoes, valores):
        
        try:
            NumQuestoes = int(questoes.get())
            
        except:
            Aviso = Toplevel(root)
            Aviso.title("Aviso")
            Mensagem = Label(Aviso, text='Valor digitado:"'+questoes.get()+'".Você precisa inserir um número de questões no formato válido. "00"')
            Mensagem.grid(column=0,row=0, padx= 25, pady = 12)
            return      
        Banca= valores[0].get()
        Orgao= valores[1].get()
        Cargo= valores[2].get()
        GDS.LimparJanela(tela)
        CriarSimulado(Banca,Orgao,Cargo, NumQuestoes)

        return
    def Titulo(Janela,Texto,Coluna, Linha, EspacoColuna = 1):
        ttk.Label(Janela,name="h1", text=Texto).grid(column=Coluna, row=Linha, columnspan = EspacoColuna)
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