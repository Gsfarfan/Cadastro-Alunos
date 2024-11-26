from tkinter.ttk import *
from tkinter import*
from tkinter import ttk
from tkinter import Tk
from tkinter import messagebox
from tkinter import filedialog as fd

from PIL import ImageTk, Image
from tkcalendar import Calendar, DateEntry
from datetime import date

from view import *

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
frame_tabela.grid(row=5, column=0, pady=0, padx=10, sticky=NSEW)



app_logo = Image.open('icone estudante.png')
app_logo = app_logo.resize((50,50))
app_logo = ImageTk.PhotoImage(app_logo)
app_logos = Label(frame_logo, image=app_logo, text="cadastro de Alunos", width=850, compound=LEFT, relief=RAISED, anchor=NW, font=('Ivy 15 bold'), bg=co6, fg=co1)
app_logos.place(x=0, y=0)


#######################################################################################################

def alunos():
    l_nome = Label(frame_detalhes, text="Nome *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_nome.place(x=4, y=10)
    e_nome = Entry(frame_detalhes, width=45, justify='left', relief='solid')
    e_nome.place(x=7, y=40)

    l_email = Label(frame_detalhes, text="Email *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_email.place(x=4, y=70)
    e_email = Entry(frame_detalhes, width=45, justify='left', relief='solid')
    e_email.place(x=7, y=100)

    l_tel = Label(frame_detalhes, text="Telefone *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_tel.place(x=4, y=130)
    e_tel = Entry(frame_detalhes, width=20, justify='left', relief='solid')
    e_tel.place(x=7, y=160)


    l_sexo = Label(frame_detalhes, text="Sexo *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_sexo.place(x=190, y=130)
    c_sexo = ttk.Combobox(frame_detalhes, width=12, font=('Ivy 8 bold'))
    c_sexo['values'] = ('Masculino', 'Feminino', 'Não Binario')
    c_sexo.place(x=190, y=160)

    
    l_data_nasc = Label(frame_detalhes, text="Data de Nascimento *", height=1,anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_data_nasc.place(x=446, y=10)
    data_nasc = DateEntry(frame_detalhes, width=18, background='darkblue', foregorund='white', borderwidth=2, year=2024)
    data_nasc.place(x=450, y=40)

    l_cpf = Label(frame_detalhes, text="CPF *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_cpf.place(x=446, y=70)
    e_cpf = Entry(frame_detalhes, width=20, justify='left', relief='solid')
    e_cpf.place(x=450, y=100)

    turmas = ['Turma A', 'Turma B']
    turma = []
    for i in turmas:
        turma.append(i)

    l_turma = Label(frame_detalhes, text="Turma *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_turma.place(x=446, y=130)
    c_turma = ttk.Combobox(frame_detalhes, width=20, font=('Ivy 8 bold'))
    c_turma['values'] = (turma)
    c_turma.place(x=450, y=160)

############################################################################################

    global imagem, imagem_string, l_imagem

    def escolher_imagem():
        global imagem, imagem_string, l_imagem

        imagem = fd.askopenfilename()
        imagem_string = imagem

        imagem = Image.open(imagem)
        imagem = imagem.resize((130,130))
        imagem = ImageTk.PhotoImage(imagem)
        l_imagem = Label(frame_detalhes, image=imagem, anchor=NW, bg=co1, fg=co4)
        l_imagem.place(x=300, y=10)

        botao_carregar['text'] = 'Trocar de Foto'

    botao_carregar = Button(frame_detalhes, command=escolher_imagem, text="Carregar foto".upper(), width=20, compound=CENTER, anchor=CENTER, overrelief="ridge", font=('Ivy 7'), bg=co1, fg=co0)
    botao_carregar.place(x=300, y=160)


    l_linha = Label(frame_detalhes, relief=GROOVE, text='h', width=1, height=100, anchor=NW, font=('Ivy 1'), bg=co0, fg=co0)
    l_linha.place(x=610, y=10)
    l_linha = Label(frame_detalhes, relief=GROOVE, text='h', width=1, height=100, anchor=NW, font=('Ivy 1'), bg=co1, fg=co0)
    l_linha.place(x=608, y=10)

    l_nome = Label(frame_detalhes, text="Buscar Aluno:", height=1,anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_nome.place(x=627, y=10)
    e_nome_procurar = Entry(frame_detalhes, width=17, justify='center', relief="solid", font=('Ivy 10'))
    e_nome_procurar.place(x=630, y=35)

    botao_procurar = Button(frame_detalhes, anchor=CENTER, text='Buscar', width=9, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co1, fg=co0)
    botao_procurar.place(x=757, y=35)

    ########################################################################################################################################################

    botao_salvar = Button(frame_detalhes, anchor=CENTER, text='Salvar'.upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co3, fg=co1)
    botao_salvar.place(x=627, y=110)

    botao_atualizar = Button(frame_detalhes, anchor=CENTER, text='Atualizar'.upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co6, fg=co1)
    botao_atualizar.place(x=627, y=135)


    botao_deletar = Button(frame_detalhes, anchor=CENTER, text='Deletar'.upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co7, fg=co1)
    botao_deletar.place(x=627, y=160)

    botao_ver = Button(frame_detalhes, anchor=CENTER, text='Ver'.upper(), width=9, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co1, fg=co0)
    botao_ver.place(x=727, y=160)

    def mostrar_alunos():
        app_nome = Label(frame_tabela, text="Tabela de Estudantes", height=1,pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
        app_nome.grid(row=0, column=0, padx=0, pady=10, sticky=NSEW)
        
        list_header = ['ID','Nome','email','telefone','sexo','imagem','data','CPF', 'Curso']
        df_list = []
        global tree_aluno
        tree_aluno = ttk.Treeview(frame_tabela, selectmode="extended",columns=list_header, show="headings")
        vsb = ttk.Scrollbar(frame_tabela, orient="vertical", command=tree_aluno.yview)
        hsb = ttk.Scrollbar(frame_tabela, orient="horizontal", command=tree_aluno.xview)
        tree_aluno.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        tree_aluno.grid(column=0, row=1, sticky='nsew')
        vsb.grid(column=1, row=1, sticky='ns')
        hsb.grid(column=0, row=2, sticky='ew')
        frame_tabela.grid_rowconfigure(0, weight=12)
        hd=["nw","nw","nw","center","center","center","center","center","center"]
        h=[40,150,150,70,70,70,80,80,100]
        n=0
        for col in list_header:
            tree_aluno.heading(col, text=col.title(), anchor=NW)
            tree_aluno.column(col, width=h[n],anchor=hd[n])
            n+=1
        for item in df_list:
            tree_aluno.insert('', 'end', values=item)

    mostrar_alunos()










    



######################################################################################

def adicionar():
    frame_tabela_curso = Frame(frame_tabela, width=300, height=200, bg=co1)
    frame_tabela_curso.grid(row=0, column=0, pady=0, padx=10, sticky=NSEW)

    frame_tabela_linha = Frame(frame_tabela, width=30, height=200, bg=co1)
    frame_tabela_linha.grid(row=0, column=1, pady=0, padx=10, sticky=NSEW)

    frame_tabela_turma = Frame(frame_tabela, width=300, height=200, bg=co1)
    frame_tabela_turma.grid(row=0, column=2, pady=0, padx=10, sticky=NSEW)

#########################################################################################    

    def novo_curso():
        nome = e_nome_curso.get()
        duracao = e_duracao.get()
        preco = e_preco.get()

        lista = [nome, duracao, preco]

        for i in lista:
            if i=="":
                messagebox.showerror('Erro', 'Preencha todos os campos')
                return
        
        criar_curso(lista)
        
        messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')

        e_nome_curso.delete(0,END)
        e_duracao.delete(0,END)
        e_preco.delete(0,END)

        mostrar_cursos()

####################################################################################

    def update_curso():
        try:
            tree_itens = tree_curso.focus()
            tree_dicionario = tree_curso.item(tree_itens)
            tree_lista = tree_dicionario['values']
            
            valor_id = tree_lista[0]

            e_nome_curso.insert(0, tree_lista[1])
            e_duracao.insert(0, tree_lista[2])
            e_preco.insert(0, tree_lista[3])

            def update():
                
                nome = e_nome_curso.get()
                duracao = e_duracao.get()
                preco = e_preco.get()
                lista = [nome, duracao, preco, valor_id]

                for i in lista:
                    if i=="":
                        messagebox.showerror('Erro', 'Preencha todos os campos')
                        return
                
                atualizar_curso(lista)
            
                messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')

                e_nome_curso.delete(0,END)
                e_duracao.delete(0,END)
                e_preco.delete(0,END)
                mostrar_cursos()
                botao_salvar.destroy()
    
            botao_salvar = Button(frame_detalhes, anchor=CENTER, command=update, text='Salvar atualizacao'.upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co3, fg=co1)
            botao_salvar.place(x=227, y=130)
        except IndexError:
            messagebox.showerror('Erro', 'Seleciona um dos cursos da tabela')

    def delete_curso():
        try:
            tree_itens = tree_curso.focus()
            tree_dicionario = tree_curso.item(tree_itens)
            tree_lista = tree_dicionario['values']
            
            valor_id = tree_lista[0]

            deletar_curso([valor_id])
            messagebox.showinfo('Sucesso', 'Os dados foram deletados')
            mostrar_cursos()

        except IndexError:
            messagebox.showerror('Erro', 'Seleciona um dos cursos da tabela')

        

    l_nome = Label(frame_detalhes, text="Nome do curso *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_nome.place(x=4, y=10)
    e_nome_curso = Entry(frame_detalhes, width=35, justify='left', relief='solid')
    e_nome_curso.place(x=7, y=40)

    l_duracao = Label(frame_detalhes, text="Duração *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_duracao.place(x=4, y=70)
    e_duracao = Entry(frame_detalhes, width=20, justify='left', relief='solid')
    e_duracao.place(x=7, y=100)

    l_preco = Label(frame_detalhes, text="Preço *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_preco.place(x=4, y=130)
    e_preco = Entry(frame_detalhes, width=10, justify='left', relief='solid')
    e_preco.place(x=7, y=160)

    botao_carregar = Button(frame_detalhes, anchor=CENTER, command=novo_curso, text='Novo Cursp'.upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co3, fg=co1)
    botao_carregar.place(x=107, y=160)

    botao_atualizar = Button(frame_detalhes, anchor=CENTER, command=update_curso, text='Atualizar'.upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co6, fg=co1)
    botao_atualizar.place(x=187, y=160)

    botao_deletar = Button(frame_detalhes, anchor=CENTER, command=delete_curso, text='Deletar'.upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co7, fg=co1)
    botao_deletar.place(x=267, y=160)

###################################################################################################################################################################################
    
    def mostrar_cursos():
        app_nome = Label(frame_tabela_curso, text="Tabela de Cursos", height=1,pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
        app_nome.grid(row=0, column=0, padx=0, pady=10, sticky=NSEW)
        
        list_header = ['ID','Curso','Duração','Preço']
        df_list = ver_cursos()
        global tree_curso
        tree_curso = ttk.Treeview(frame_tabela_curso, selectmode="extended",columns=list_header, show="headings")
        vsb = ttk.Scrollbar(frame_tabela_curso, orient="vertical", command=tree_curso.yview)
        hsb = ttk.Scrollbar(frame_tabela_curso, orient="horizontal", command=tree_curso.xview)
        tree_curso.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        tree_curso.grid(column=0, row=1, sticky='nsew')
        vsb.grid(column=1, row=1, sticky='ns')
        hsb.grid(column=0, row=2, sticky='ew')
        frame_tabela_curso.grid_rowconfigure(0, weight=12)
        hd=["nw","nw","e","e"]
        h=[30,150,80,60]
        n=0
        for col in list_header:
            tree_curso.heading(col, text=col.title(), anchor=NW)
            tree_curso.column(col, width=h[n],anchor=hd[n])
            n+=1
        for item in df_list:
            tree_curso.insert('', 'end', values=item)

    mostrar_cursos()

###############################################################################################################################################

    l_linha = Label(frame_detalhes, relief=GROOVE, text='h', width=1, height=100, anchor=NW, font=('Ivy 1'), bg=co0, fg=co0)
    l_linha.place(x=374, y=10)
    l_linha = Label(frame_detalhes, relief=GROOVE, text='h', width=1, height=100, anchor=NW, font=('Ivy 1'), bg=co1, fg=co0)
    l_linha.place(x=372, y=10)

    l_linha = Label(frame_tabela_linha, relief=GROOVE, text='h', width=1, height=200, anchor=NW, font=('Ivy 1'), bg=co0, fg=co0)
    l_linha.place(x=6, y=10)
    l_linha = Label(frame_tabela_linha, relief=GROOVE, text='h', width=1, height=200, anchor=NW, font=('Ivy 1'), bg=co1, fg=co0)
    l_linha.place(x=4, y=10)

####################################################################################################################

    l_nome = Label(frame_detalhes, text="Nome da Turma *", height=1,anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_nome.place(x=404, y=10)
    e_nome_turma = Entry(frame_detalhes, width=35, justify='left', relief="solid")
    e_nome_turma.place(x=407, y=40)

    l_turma = Label(frame_detalhes, text="Curso *", height=1,anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_turma.place(x=404, y=70)

    cursos = ['curso 1', 'curso 2']
    curso = []
    for i in cursos:
        curso.append(i)

    c_curso = ttk.Combobox(frame_detalhes, width=20, font=('Ivy 8 bold'))
    c_curso['values'] = (curso)
    c_curso.place(x=407, y=100)

    l_data_inicio = Label(frame_detalhes, text="Data de inicio *", height=1,anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_data_inicio.place(x=406, y=130)
    data_inicio = DateEntry(frame_detalhes, width=10, background='darkblue', foregorund='white', borderwidth=2, year=2024)
    data_inicio.place(x=407, y=160)

#################################################################################################################################################################################
    
    botao_carregar = Button(frame_detalhes, anchor=CENTER, text='Salvar'.upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co3, fg=co1)
    botao_carregar.place(x=507, y=160)

    botao_atualizar = Button(frame_detalhes, anchor=CENTER, text='Atualizar'.upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co6, fg=co1)
    botao_atualizar.place(x=587, y=160)

    botao_deletar = Button(frame_detalhes, anchor=CENTER, text='Deletar'.upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co7, fg=co1)
    botao_deletar.place(x=667, y=160)

#####################################################################################################################################################################################

    def mostrar_turmas():
        app_nome = Label(frame_tabela_turma, text="Tabela de Turmas", height=1,pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
        app_nome.grid(row=0, column=0, padx=0, pady=10, sticky=NSEW)
        
        list_header = ['ID','Nome da Turma','Curso','Inicio']
        df_list = []
        global tree_turma
        tree_turma = ttk.Treeview(frame_tabela_turma, selectmode="extended",columns=list_header, show="headings")
        vsb = ttk.Scrollbar(frame_tabela_turma, orient="vertical", command=tree_turma.yview)
        hsb = ttk.Scrollbar(frame_tabela_turma, orient="horizontal", command=tree_turma.xview)
        tree_turma.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        tree_turma.grid(column=0, row=1, sticky='nsew')
        vsb.grid(column=1, row=1, sticky='ns')
        hsb.grid(column=0, row=2, sticky='ew')
        frame_tabela_turma.grid_rowconfigure(0, weight=12)
        hd=["nw","nw","e","e"]
        h=[30,130,150,80]
        n=0
        for col in list_header:
            tree_turma.heading(col, text=col.title(), anchor=NW)
            tree_turma.column(col, width=h[n],anchor=hd[n])
            n+=1
        for item in df_list:
            tree_turma.insert('', 'end', values=item)

    mostrar_turmas()


########################################################################

def salvar():
    print('Salvar')

##################################################################################################

def control(i):
    if i == 'cadastro':
        for widget in frame_detalhes.winfo_children():
            widget.destroy()

        for widget in frame_tabela.winfo_children():
            widget.destroy()

        alunos()
        

    if i == 'adicionar':
        for widget in frame_detalhes.winfo_children():
            widget.destroy()

        for widget in frame_tabela.winfo_children():
            widget.destroy()

        adicionar()


    if i == 'salvar':
        for widget in frame_detalhes.winfo_children():
            widget.destroy()

        for widget in frame_tabela.winfo_children():
            widget.destroy()

        salvar()


#####################################################################################################


app_img_cadastro = Image.open('icone cadastro.png')
app_img_cadastro = app_img_cadastro.resize((18,18))
app_img_cadastro = ImageTk.PhotoImage(app_img_cadastro)
app_cadastro = Button(frame_dados, command=lambda:control('cadastro'), image=app_img_cadastro, text="Cadastro", width=100, compound=LEFT, overrelief="ridge", font=('Ivy 11'), bg=co1, fg=co0)
app_cadastro.place(x=10, y=30)


app_img_adicionar = Image.open('icone cadastro.png')
app_img_adicionar = app_img_adicionar.resize((18,18))
app_img_adicionar = ImageTk.PhotoImage(app_img_adicionar)
app_adicionar = Button(frame_dados, command=lambda:control('adicionar'), image=app_img_adicionar, text="Adicionar", width=100, compound=LEFT, overrelief="ridge", font=('Ivy 11'), bg=co1, fg=co0)
app_adicionar.place(x=123, y=30)


app_img_salvar = Image.open('icone salvar.png')
app_img_salvar = app_img_salvar.resize((18,18))
app_img_salvar = ImageTk.PhotoImage(app_img_salvar)
app_salvar = Button(frame_dados, command=lambda:control('salvar'), image=app_img_salvar, text="Salvar", width=100, compound=LEFT, overrelief="ridge", font=('Ivy 11'), bg=co1, fg=co0)
app_salvar.place(x=236, y=30)



alunos()
janela.mainloop()