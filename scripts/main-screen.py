from tkinter import *

class MainScreen:
    def __init__(self, master = None):
        #primeiro container
        self.moldura = Frame(master)
        self.moldura.grid(row = 0, column = 0, rowspan = 2, columnspan = 2, sticky = N)

        #elementos de título
        self.titulo = Label(self.moldura)
        self.titulo["font"] = ('MS', '40')
        self.titulo["text"] = "IMAGE PROCESSING TOOL"
        self.titulo.pack(side = TOP, fill = BOTH, expand=YES)

        #elementos de botao
        self.fonte_padrao = ('Arial', '26')

        self.botao_image_pre_proc = Button(master)
        self.botao_image_pre_proc["text"] = "Image Pre Processing"
        self.botao_image_pre_proc["font"] = self.fonte_padrao
        self.botao_image_pre_proc.grid(row = 2, column = 0)

        self.botao_plot = Button(master)
        self.botao_plot["text"] = "Plotter"
        self.botao_plot["font"] = self.fonte_padrao
        self.botao_plot.grid(row = 2, column = 1)

root = Tk()
root.title("Image Processing Tool")
root.geometry('720x480')
MainScreen(root)
root.mainloop()