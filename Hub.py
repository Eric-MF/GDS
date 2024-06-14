import tkinter as tk
from InterfaceGrafica import *
from GerenciadorDeUsuários import *

import os
os.system('cls' if os.name == 'nt' else 'clear')

root = tk.Tk()
GerenciadorDeSimulados(root)



def Gerenciador():

    GerenciadorDeSimulados.__IniciarGerenciador__(root)
    TelaInicial()
    root.mainloop()
    return



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