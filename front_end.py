# -*- coding: utf-8 -*-

# Adicionando as Bibliotecas
from back_end import *
from PyInstaller import *
try:
    import Tkinter as tk
except:
    import tkinter as tk

# Inicia o Back End
Degrees()
Power()

# Conversão de RGB
def _from_rgb(rgb):
    return "#%02x%02x%02x" % rgb  

class Fullscreen:
    def __init__(self):
        # Configurações da Janela
        self.window = tk.Tk()
        self.window.geometry('1920x1080+10+10')
        self.window.configure(bg=_from_rgb((0, 170, 237)))
        self.window.attributes('-fullscreen', True)  
        self.fullScreenState = False

        # Teclas de Atalho
        self.window.bind("<F11>", self.toggleFullScreen)
        self.window.bind("<Escape>", self.quitFullScreen)

        # Body
        barra = tk.Frame(height = 50, width = 1330, bg = _from_rgb((48, 48, 48)))
        barra.place(x=18, y=5)

        body = tk.Frame(height = 690, width = 1330, bg = _from_rgb((50, 121, 168)))
        body.place(x=18, y=60)

        self.window.mainloop()

    def toggleFullScreen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.window.attributes("-fullscreen", self.fullScreenState)

    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.window.attributes("-fullscreen", self.fullScreenState)

Fullscreen()