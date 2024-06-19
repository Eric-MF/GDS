import tkinter as tk
from InterfaceGrafica import *
from GerenciadorDeUsuários import *

import os
#Limpa o terminal
os.system('cls' if os.name == 'nt' else 'clear')

#Cria instância do tk e envia para interface gráfica.
root = tk.Tk()
GerenciadorDeSimulados(root)


#Define a ordem do processo principal.
def Gerenciador():

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