import tkinter as tk
from InterfaceGrafica import *
from GerenciadorDeUsuários import *
import customtkinter as ctk

import os
#Limpa o terminal
os.system('cls' if os.name == 'nt' else 'clear')




#Define a ordem do processo principal.
def Gerenciador():
    #Cria instância do tk e envia para interface gráfica.
    global root
    global GerenciadorDeSimulados
    root = ctk.CTk()

    GerenciadorDeSimulados(root)
    GerenciadorDeSimulados.__IniciarGerenciador__(root)
    TelaInicial()
    root.mainloop()
    return


#Define qual tela de início vai ser apresentada, caso tenha ou não usuários já cadastrados.
def TelaInicial():
    usuarios = VerificarUsuarios()

    if usuarios == []:
        GerenciadorDeSimulados.AdicionarUsuario()
    else:
        GerenciadorDeSimulados.EscolherUsuario()
        #TelaInicial()
    return

#Chama o programa
Gerenciador()
