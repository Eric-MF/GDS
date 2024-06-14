from tkinter import *
import tkinter as ttk
from GerenciadorDeUsuários import *

class GerenciadorDeSimulados:
    def __init__(self, master):
        self.master = master
        #self.GUI_list = []

    
    def __IniciarGerenciador__(r):

        #Dados da interface
        CaminhoDoIcone = r"C:\Users\ericm\Documents\Justice\Legis Ler\Programas\Aprendizado\Gerenciador de Simulados\Ícones\Gerenciador de Simulados - Ícone.ico"
        NomeDoPrograma  = "Gerenciador de Simulados"
        global root
        root = r
        #Cria a tela dentro da tela do programa
        root.title(NomeDoPrograma)  
        root.iconbitmap(CaminhoDoIcone)
        root.state('zoomed')

        #Cria os frames do programa
        menu = ttk.Frame(root, name="menu")
        menu.grid(column=0, row=0, columnspan=3)
        ttk.Label(menu, text="Menu: ").grid(column=0,row=0)
        global tela
        tela = ttk.Frame(root, name="tela")
        tela.grid(column=1,row=1)

    def AdicionarUsuario():
        for child in tela.winfo_children():
            child.destroy()
        #Adiciona texto à tela
        ttk.Label(tela, text="Nome:").grid(column=0,row=0)

        #Adiciona campo para inserir texto à tela
        e = Entry(tela)
        e.grid(column=0,row=1)
        e.insert(0, "Nome Usuário")

        #Adiciona botão à tela
        ttk.Button(tela, text="Enter", command=lambda: GerenciadorDeSimulados.Voltar(e.get())).grid(column=0,row=2)
        return    
    def Voltar(Nome):
        AdicionarNome(Nome)
        GerenciadorDeSimulados.EscolherUsuario()

    def EscolherUsuario():
        for child in tela.winfo_children():
            child.destroy()
        
        #Adiciona texto à tela
        usuarios = VerificarUsuarios()
        ttk.Label(tela, text=usuarios).grid(column=0,row=0)

        #Muda para tela de adicionar novo usuário
        ttk.Button(tela, text="Adicionar novo Usuário", command=lambda: GerenciadorDeSimulados.AdicionarUsuario()).grid(column=0,row=2)

        #Adiciona botão à tela3)
        ttk.Button(tela, text="Enter").grid(column=0,row=3)
        return
    

