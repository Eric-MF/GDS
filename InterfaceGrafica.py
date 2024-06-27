from tkinter import *
import tkinter as ttk
from GerenciadorDeUsuários import *
from Simulados import *
import math
from customtkinter import *

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
        root.columnconfigure(0, weight=1)
        root.rowconfigure(1, weight=1)
        root.after(0, lambda: root.wm_state('zoomed'))
        #global app
        #app = CTk()

        #Cria os frames do programa
        global menu
        menu = CTkFrame(root)
        menu.grid(column=0, row=0, columnspan=3)
        CTkLabel(menu, text="Menu: ").grid(column=0,row=0)
        global tela
        tela = CTkFrame(root)
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
        e = CTkEntry(tela)
        e.grid(column=0,row=1)
        e.insert(0, "Nome Usuário")

        #Adiciona botão à tela
        CTkButton(tela, text="Enter", command=lambda: GDS.Voltar(e.get())).grid(column=0,row=2)
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

        listadeusuarios = CTkFrame(tela)
        listadeusuarios.grid(column=0, row=1)

        #Cria lista com apenas nomes de usuários
        nome_usuarios = []
        for user in usuarios:
            nome_usuarios.append(user[1])
        
        #Cria menu de seleção de usuarios
        usuario_escolhido = ttk.StringVar(listadeusuarios)
        usuario_escolhido.set("Selecione o usuário")
        

        CTkOptionMenu(master=listadeusuarios, variable=usuario_escolhido, values=nome_usuarios).grid(column=1, row=1,padx=100, pady=50)



        #Adiciona botão de enter à tela
        CTkButton(tela, text="Enter", command=lambda: GDS.EscolherSimulado(usuario_escolhido)).grid(column=0,row=2, pady=25)

        #Muda para tela de adicionar novo usuário
        CTkButton(tela, text="Adicionar novo Usuário", command=lambda: GDS.AdicionarUsuario()).grid(column=0,row=3, pady=25)

        return  
    def EscolherSimulado(usuario_escolhido):
        GDS.LimparJanela(tela)
        global usuario
        usuario = usuario_escolhido.get()
        GDS.Titulo(tela,usuario,0,0)
        listasimulados = VerificarSimulados(usuario)
        VerificarPorcentagem(usuario,"1")

        if listasimulados == []:
            GDS.TelaAdicionarSimulado()
        else:
            #Exibe Simulados
            GDS.Titulo(tela,"Lista de Simulados",0,0)
            n = 0
            for simulado in listasimulados:
                Porcentagem = VerificarPorcentagem(usuario,simulado[0])
                Texto = "Nº: "+str(n+1)+" | Banca: " + simulado[1] + " | Orgão: "+simulado[2]+" | Cargo: "+simulado[3]+" | Acerto: " +Porcentagem
                CTkLabel(master= tela, text=Texto).grid(column=0, row=n+1)
                n += 1
                
            
            
            CTkButton(tela, text="+",command=lambda: GDS.TelaAdicionarSimulado()).grid(column=1,row=0, padx=20, pady=10)
            CTkButton(tela, text="<",command=lambda: GDS.EscolherUsuario()).grid(column=1,row=1, padx=20)


        #Adiciona botões "Adicionar Simulado" e "Enter"

        
        


        return
        ######################################################## 
    def TelaAdicionarSimulado():
        GDS.LimparJanela(tela)
        GDS.Titulo(tela,"Adicionar Simulado",0,0,2)
        InfoSimulado=["Banca", "Orgão", "Cargo"]
        simulados = CTkFrame(tela)
        simulados.grid(column=1,row=1)
        textos = CTkFrame(tela)
        textos.grid(column=0,row=1)
        n = 1
        ValoresObtidos = []
        for Info in InfoSimulado:
            n = n + 1
            ValoresObtidos.append(GDS.Inserir(Info,"Nome do(a) "+Info,n,1,simulados))
            GDS.Inserir(Info,Info+":",n, 0, textos, "Texto")
        Questões=GDS.Inserir("Equantidade", "00", n+1,1,simulados)
        GDS.Inserir("Tquantidade", "Quantidade de questões:", n+1,0,textos, "Texto")
        CTkButton(tela, text="Enter",command=lambda: GDS.TelaDeRespostas(Questões,ValoresObtidos)).grid(column=0,row=3,columnspan=2)
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
            QMarcadas.append(GDS.Inserir(Nome = "Numeros"+str(n),Texto= "",Linha = math.ceil((n-0.1)%10),Coluna=math.ceil(n/10)*2))
            GDS.Inserir("Questão"+str(n),n,math.ceil((n-0.1)%10),(math.ceil(n/10)*2)-1,Tipo="Label")
        Botao = CTkButton(tela, text="Enter")
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
            questao.insert(0,"")
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
        Titulo = CTkLabel(Janela, text=Texto)
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
                e = CTkEntry(Janela)
                e.insert(0, Texto)
                e.grid(column= Coluna,row= Linha)
                return e
            case "Label" | "Texto":
                l = CTkLabel(Janela, text=Texto)
                l.grid(column= Coluna,row= Linha)
                return l
                
        
        
        
        ################################################################

    #_______________________________________________________________
GDS = GerenciadorDeSimulados