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
        menu = ttk.Frame(root, name="menu")
        menu.grid(column=0, row=0, columnspan=3)
        ttk.Label(menu, text="Menu: ").grid(column=0,row=0)
        global tela
        tela = ttk.Frame(root, name="tela")
        tela.grid(column=0,row=1)

    #Tela de adicionar novos usuários.
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
        usuarios = VerificarUsuarios()

        if usuarios == []:
            GerenciadorDeSimulados.AdicionarUsuario()
            return
        
        GerenciadorDeSimulados.EscolherUsuario()

    def EscolherUsuario():
        for child in tela.winfo_children():
            child.destroy()
        
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
        ttk.Button(tela, text="Enter", command=lambda: GerenciadorDeSimulados.EscolherSimulado()).grid(column=0,row=2, pady=75)

        #Muda para tela de adicionar novo usuário
        ttk.Button(tela, text="Adicionar novo Usuário", command=lambda: GerenciadorDeSimulados.AdicionarUsuario()).grid(column=0,row=3)


        return
    
    def EscolherSimulado():
        for child in tela.winfo_children():
            child.destroy()
            
        return
