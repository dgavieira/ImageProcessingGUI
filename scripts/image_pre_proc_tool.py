from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageTk
from matplotlib import image
from matplotlib import pyplot

class ImagePreProcessingTool:
    def __init__(self, master = None):
        self.container = Frame(master)
        self.container.pack()

        self.botao_browse = Button(master)
        self.botao_browse['text'] = "Browse Image"
        self.botao_browse["command"] = self.fileDialog
        self.botao_browse.pack()

    #open operational system explorer and returns file path
    def fileDialog(self):
        self.filename = filedialog.askopenfilename(initialdir="/", title="Select A File", filetype=
        (("jpeg files", "*.jpg"), ("all files", "*.*")))
        self.label = ttk.Label(self.container, text="")
        self.label.grid(column=1, row=2)
        self.label.configure(text=self.filename)


        img = Image.open(self.filename)
        photo = ImageTk.PhotoImage(image = img)

        self.label2 = Label(image=photo)
        self.label2.image = photo
        self.label2.pack()

    #erases image from canvas
    def blankimage(self):
        img = T

root = Tk()
root.title("Image Processing Tool")
root.geometry('720x480')
ImagePreProcessingTool(root)
root.mainloop()