from tkinter.ttk import *
from tkinter import*
from tkinter import ttk
from tkinter import Tk
from tkinter import messagebox
from tkinter import filedialog as fd

from PIL import ImageTk, Image

co0 = "#2e2d2b"
co1 = "#feffff"
co2 = "#e5e5e5"
co3 = "#00a095"
co4 = "#403d3d"
co6 = "#003452"
co7 = "#ef5350"

co6 = "#038cfc" 
co8 = "#263238"
co9 = "#e9edf5"

janela = Tk()
janela.title("")
janela.geometry("850x620")
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

style = Style(janela)
style.theme_use("clam")

frame_logo = Frame(janela, width=850, height=52, bg=co6)
frame_logo.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=1, columnspan=1, ipadx=680)

frame_dados = Frame(janela, width=850, height=65, bg=co1)
frame_dados.grid(row=2, column=0, pady=0, padx=0, sticky=NSEW)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=3, columnspan=1, ipadx=680)

frame_detalhes = Frame(janela, width=850, height=200, bg=co1)
frame_detalhes.grid(row=4, column=0, pady=0, padx=10, sticky=NSEW)


frame_tabela = Frame(janela, width=850, height=200, bg=co1)
frame_detalhes.grid(row=5, column=0, pady=0, padx=10, sticky=NSEW)



app_logo = Image.open('icone estudante.png')
app_logo = app_logo.resize((50,50))
app_logo = ImageTk.PhotoImage(app_logo)
app_logos = Label(frame_logo, image=app_logo, text="cadastro de Alunos", width=850, compound=LEFT, relief=RAISED, anchor=NW, font=('Ivy 15 bold'), bg=co6, fg=co1)
app_logos.place(x=0, y=0)


#######################################################################################################

def control(i):
    pass


app_img_cadastro = Image.open('icone cadastro.png')
app_img_cadastro = app_img_cadastro.resize((18,18))
app_img_cadastro = ImageTk.PhotoImage(app_img_cadastro)
app_cadastro = Button(frame_dados, image=app_img_cadastro, text="Cadastro", width=100, compound=LEFT, overrelief="ridge", font=('Ivy 11'), bg=co1, fg=co0)
app_cadastro.place(x=10, y=30)




janela.mainloop()