from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import *
from tkinter import *
from PIL import Image, ImageTk

#importando as funcao da view
from view import *

#tkcalendario
from datetime import date

from datetime import datetime

hoje = datetime.today()

# Definindo cores
co1 = "#f0f0f0"  # Cor de fundo claro
co2 = "#333333"  # Cor de texto escuro
co3 = "#81C784"  # Cor para hover (verde mais claro)
co4 = "#5CAF50"  # Cor verde mais intenso
co5 = "#388E3C"  # Cor de fundo de botão (verde escuro)
co6 = "#4CAF50"  # Cor verde para cabeçalhos e botões principais
co7 = "#FFFFFF"  # Cor de fundo de texto (branco)
co8 = "#B0B0B0"  # Cor de texto secundário ou bordas suaves

# Criando a janela
janela = Tk()
janela.title("Exemplo de Janela Tkinter")
janela.geometry('770x330')
janela.configure(background=co1)  # Usando a variável co1 para definir a cor de fundo
janela.resizable(width=False, height=False)  # Corrigido de FALSE para False

# Estilo da janela
style = Style(janela)
style.theme_use("clam")  # Definindo o tema da janela

# Divisão das janelas
frameCima = Frame(janela, width=770, height=50, bg=co6, relief="flat")
frameCima.grid(row=0, column=0, columnspan=2, sticky=NSEW)

frameEsquerdo = Frame(janela, width=150, height=265, bg=co4, relief="solid")
frameEsquerdo.grid(row=1, column=0, sticky=NSEW)

frameDireito = Frame(janela, width=600, height=265, bg=co1, relief="raised")
frameDireito.grid(row=1, column=1, sticky=NSEW)

# Logo
app_img = Image.open('logo.png')
app_img = app_img.resize((45, 40))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, width=1000, compound=LEFT, padx=5, anchor=NW, bg=co6, fg=co1)
app_logo.place(x=5, y=0)

app_ = Label(frameCima, text="Livros em Ordem", compound=LEFT, padx=5, anchor=NW, font=('Verdana', 15, 'bold'), fg=co3)  # Corrigido para ('Verdana', 15, 'bold')
app_.place(x=50, y=7)

app_linha = Label(frameCima, width=770, height=1, padx=5, anchor=NW, font=('Verdana', 1), bg=co5, fg=co5)  # Corrigido para ('Verdana', 1)
app_linha.place(x=0, y=47)

# Função para novo usuário     
def novo_usuario():

    global img_salvar 

    def add():
        first_name = e_p_nome.get()
        last_name = e_p_sobrenome.get()
        adress = e_p_endereco.get()
        email = e_p_email.get()
        phone = e_p_numero.get()

        lista = [first_name, last_name, adress, email, phone]

        messagebox.showinfo('Cadastro Realizado Com Sucesso')

        #verificando caso algum campo esteja vazio
        for i in lista:
            if i=='':
                messagebox.showerror('Erro', 'Preencha os Campos')
                return
            
        #inserindo no banco de dados
        insert_user(first_name, last_name, adress, email, phone)
        #Limpando os campos de entrada
        e_p_nome.delete(0, END)
        e_p_sobrenome.delete(0, END)
        e_p_endereco.delete(0, END)
        e_p_email.delete(0, END)
        e_p_numero.delete(0, END)

            
    app_ = Label(frameDireito, text="Inserir um novo usuario", width=50, compound=LEFT, padx=5, font=('Verdana', 12))  # Corrigido para 'Verdana', 12
    app_.grid(row=0, column=0, columnspan=4, sticky=NSEW)
    app_linha = Label(frameDireito, width=400, height=1, anchor=NW, font=('Verdana', 1), bg=co4, fg=co4)
    app_linha.grid(row=1, column=0, columnspan=4, sticky=NSEW)  # Alterado para grid

    l_p_nome = Label(frameDireito, text="Primeiro Nome",anchor=NW, font=('Verdana', 12) )   # Corrigido para 'Verdana', 12
    l_p_nome.grid(row=2, column=0, padx=5, pady=5, sticky=NSEW)
    e_p_nome = Entry(frameDireito, width=25, justify='left', relief='solid')
    e_p_nome.grid(row=2, column=1, padx=5, pady=5, sticky=NSEW)


    l_p_sobrenome = Label(frameDireito, text="Sobrenome",anchor=NW, font=('Verdana', 12) )   # Corrigido para 'Verdana', 12
    l_p_sobrenome.grid(row=3, column=0, padx=5, pady=5, sticky=NSEW)
    e_p_sobrenome = Entry(frameDireito, width=25, justify='left', relief='solid')
    e_p_sobrenome.grid(row=3, column=1, padx=5, pady=5, sticky=NSEW)

    l_p_endereco= Label(frameDireito, text="Endereço do Usuario",anchor=NW, font=('Verdana', 12) )   # Corrigido para 'Verdana', 12
    l_p_endereco.grid(row=4, column=0, padx=5, pady=5, sticky=NSEW)
    e_p_endereco = Entry(frameDireito, width=25, justify='left', relief='solid')
    e_p_endereco.grid(row=4, column=1, padx=5, pady=5, sticky=NSEW)

    l_p_email = Label(frameDireito, text="E-Mail",anchor=NW, font=('Verdana', 12) )   # Corrigido para 'Verdana', 12
    l_p_email.grid(row=5, column=0, padx=5, pady=5, sticky=NSEW)
    e_p_email= Entry(frameDireito, width=25, justify='left', relief='solid')
    e_p_email.grid(row=5, column=1, padx=5, pady=5, sticky=NSEW)

    l_p_numero = Label(frameDireito, text="Numero de Telefone",anchor=NW, font=('Verdana', 12) )   # Corrigido para 'Verdana', 12
    l_p_numero.grid(row=6, column=0, padx=5, pady=5, sticky=NSEW)
    e_p_numero = Entry(frameDireito, width=25, justify='left', relief='solid')
    e_p_numero.grid(row=6, column=1, padx=5, pady=5, sticky=NSEW)


    # BOTAO SALVAR
    img_salvar = Image.open('save.png')
    img_salvar= img_salvar.resize((18, 18))
    img_salvar = ImageTk.PhotoImage(img_salvar)
    b_salvar = Button(frameDireito,command=add, image=img_salvar, compound=LEFT, width=100,  anchor=NW, text=" Salvar", bg=co1, fg=co4, font=('Ivy', 11), overrelief=RIDGE, relief=GROOVE)
    b_salvar.grid(row=7, column=1, pady=5,  sticky=NSEW)

    #funcao ver usuarios
def ver_usuarios():

    app_ = Label(frameDireito,text="Todos os usuários do banco de dados",width=50,compound=LEFT, padx=5,pady=10, relief=FLAT, anchor=NW, font=('Verdana 12'),bg=co1, fg=co4)
    app_.grid(row=0, column=0, columnspan=4, sticky=NSEW)
    l_linha = Label(frameDireito, width=400, height=1,anchor=NW, font=('Verdana 1 '), bg=co3, fg=co1)
    l_linha.grid(row=1, column=0, columnspan=4, sticky=NSEW)

    dados = get_users()

    #creating a treeview with dual scrollbars
    list_header = ['ID','Nome','Sobrenome','Endereço','Email','Telefone']
    
    global tree

    tree = ttk.Treeview(frameDireito, selectmode="extended",
                        columns=list_header, show="headings")
    
    vsb = ttk.Scrollbar(frameDireito, orient="vertical", command=tree.yview)
    hsb = ttk.Scrollbar(frameDireito, orient="horizontal", command=tree.xview)
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=2, sticky='nsew')
    vsb.grid(column=1, row=2, sticky='ns')
    hsb.grid(column=0, row=3, sticky='ew')
    frameDireito.grid_rowconfigure(0, weight=12)
    
    hd=["nw","nw","nw","nw","nw","nw"]
    h=[20,80,80,120,120,76,100]
    n=0

    for col in list_header:
        tree.heading(col, text=col, anchor='nw')
        #adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])
        
        n+=1

    for item in dados:
        tree.insert('', 'end', values=item)

#Novo Livro

def novo_livro():
    
    global img_salvar

    def add():

        title = e_titulo.get()
        author  = e_autor.get()
        publisher = e_editora.get()
        year = e_ano.get()
        isbn = e_isbn.get()

        lista = [title, author, publisher, year, isbn]

        #verificando caso algum campo esteja vazio
        for i in lista:
            if i=='':
                messagebox.showerror('Erro', 'Preencha os Campos')
                return
                
            #inserindo no banco de dados
        insert_book(title, author, publisher, year, isbn)

        messagebox.showinfo('Sucesso', 'Livro Inserido no banco de dados')

        #Limpando os campos de entrada
        e_titulo.delete(0, END)
        e_autor.delete(0, END)
        e_editora.delete(0, END)
        e_ano.delete(0, END)
        e_isbn.delete(0, END)

    app_ = Label(frameDireito, text="Inserir novo livro", width=50, compound=LEFT, padx=5, font=('Verdana', 12))  # Corrigido para 'Verdana', 12
    app_.grid(row=0, column=0, columnspan=4, sticky=NSEW)
    app_linha = Label(frameDireito, width=400, height=1, anchor=NW, font=('Verdana', 1), bg=co4, fg=co4)
    app_linha.grid(row=1, column=0, columnspan=4, sticky=NSEW)  # Alterado para grid

    l_titulo = Label(frameDireito, text="Titulo do livro",anchor=NW, font=('Verdana', 12) )   # Corrigido para 'Verdana', 12
    l_titulo.grid(row=2, column=0, padx=5, pady=5, sticky=NSEW)
    e_titulo = Entry(frameDireito, width=25, justify='left', relief='solid')
    e_titulo.grid(row=2, column=1, padx=5, pady=5, sticky=NSEW)


    l_autor = Label(frameDireito, text="Autor do livro",anchor=NW, font=('Verdana', 12) )   # Corrigido para 'Verdana', 12
    l_autor.grid(row=3, column=0, padx=5, pady=5, sticky=NSEW)
    e_autor = Entry(frameDireito, width=25, justify='left', relief='solid')
    e_autor.grid(row=3, column=1, padx=5, pady=5, sticky=NSEW)

    l_editora= Label(frameDireito, text="Editora",anchor=NW, font=('Verdana', 12) )   # Corrigido para 'Verdana', 12
    l_editora.grid(row=4, column=0, padx=5, pady=5, sticky=NSEW)
    e_editora = Entry(frameDireito, width=25, justify='left', relief='solid')
    e_editora.grid(row=4, column=1, padx=5, pady=5, sticky=NSEW)

    l_ano = Label(frameDireito, text="Ano de publicação",anchor=NW, font=('Verdana', 12) )   # Corrigido para 'Verdana', 12
    l_ano.grid(row=5, column=0, padx=5, pady=5, sticky=NSEW)
    e_ano= Entry(frameDireito, width=25, justify='left', relief='solid')
    e_ano.grid(row=5, column=1, padx=5, pady=5, sticky=NSEW)

    l_isbn= Label(frameDireito, text="ISBN do livro",anchor=NW, font=('Verdana', 12) )   # Corrigido para 'Verdana', 12
    l_isbn.grid(row=6, column=0, padx=5, pady=5, sticky=NSEW)
    e_isbn = Entry(frameDireito, width=25, justify='left', relief='solid')
    e_isbn.grid(row=6, column=1, padx=5, pady=5, sticky=NSEW)


    # BOTAO SALVAR
    img_salvar = Image.open('save.png')
    img_salvar= img_salvar.resize((18, 18))
    img_salvar = ImageTk.PhotoImage(img_salvar)
    b_salvar = Button(frameDireito,command=add, image=img_salvar, compound=LEFT, width=100,  anchor=NW, text=" Salvar", bg=co1, fg=co4, font=('Ivy', 11), overrelief=RIDGE, relief=GROOVE)
    b_salvar.grid(row=7, column=1, pady=5,  sticky=NSEW)



#Funcão Ver Livros
def ver_livros():
    app_ = Label(frameDireito,text="Todos os livros",width=50,compound=LEFT, padx=5,pady=10, relief=FLAT, anchor=NW, font=('Verdana 12'),bg=co1, fg=co4)
    app_.grid(row=0, column=0, columnspan=4, sticky=NSEW)
    l_linha = Label(frameDireito, width=400, height=1,anchor=NW, font=('Verdana 1 '), bg=co3, fg=co1)
    l_linha.grid(row=1, column=0, columnspan=4, sticky=NSEW)

    dados = exibir_livros()

    #creating a treeview with dual scrollbars
    list_header = ['ID','Titulo','Autor','Editora','Ano','ISBN']
    
    global tree

    tree = ttk.Treeview(frameDireito, selectmode="extended", columns=list_header, show="headings")
    vsb = ttk.Scrollbar(frameDireito, orient="vertical", command=tree.yview)
    hsb = ttk.Scrollbar(frameDireito, orient="horizontal", command=tree.xview)
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=2, sticky='nsew')
    vsb.grid(column=1, row=2, sticky='ns')
    hsb.grid(column=0, row=3, sticky='ew')
    frameDireito.grid_rowconfigure(0, weight=12)
    
    hd=["nw","nw","nw","nw","nw","nw"]
    h=[20,165,110,100,50,50,100]
    n=0

    for col in list_header:
        tree.heading(col, text=col, anchor='nw')
        #adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])
        n+=1

    for item in dados:
        tree.insert('', 'end', values=item)

#realizar um emprestimo
def realizar_emprestimo():

    global img_salvar

    def add():
        user_id = e_id_usuario.get()
        book_id = e__id_livro.get()

        # Verificando se os campos estão preenchidos
        if user_id == '' or book_id == '':
            messagebox.showerror('Erro', 'Preencha todos os campos')
            return

        try:
            # Inserindo o empréstimo no banco de dados
            insert_loan(book_id, user_id, datetime.now(), None)
            messagebox.showinfo('Sucesso', 'Empréstimo realizado com sucesso')

            # Limpando os campos de entrada
            e_id_usuario.delete(0, END)
            e__id_livro.delete(0, END)

        except Exception as e:
            messagebox.showerror('Erro', f'Erro ao realizar o empréstimo: {str(e)}')

    app_ = Label(frameDireito, text="Realizar um empréstimo", width=50, compound=LEFT, padx=5, font=('Verdana', 12))
    app_.grid(row=0, column=0, columnspan=4, sticky=NSEW)
    app_linha = Label(frameDireito, width=400, height=1, anchor=NW, font=('Verdana', 1), bg=co4, fg=co4)
    app_linha.grid(row=1, column=0, columnspan=3, sticky=NSEW)

    l_id_usuario = Label(frameDireito, text="Digite o ID do usuario", anchor=NW, font=('Verdana', 12))
    l_id_usuario.grid(row=2, column=0, padx=5, pady=5, sticky=NSEW)
    e_id_usuario = Entry(frameDireito, width=25, justify='left', relief='solid')
    e_id_usuario.grid(row=2, column=1, padx=5, pady=5, sticky=NSEW)

    l_id_livro = Label(frameDireito, text="Digite o ID do Livro", anchor=NW, font=('Verdana', 12))
    l_id_livro.grid(row=3, column=0, padx=5, pady=5, sticky=NSEW)
    e__id_livro = Entry(frameDireito, width=25, justify='left', relief='solid')
    e__id_livro.grid(row=3, column=1, padx=5, pady=5, sticky=NSEW)

    # BOTAO SALVAR
    img_salvar = Image.open('save.png')
    img_salvar = img_salvar.resize((18, 18))
    img_salvar = ImageTk.PhotoImage(img_salvar)
    b_salvar = Button(frameDireito, command=add, image=img_salvar, compound=LEFT, width=100, anchor=NW, text=" Salvar", bg=co1, fg=co4, font=('Ivy', 11), overrelief=RIDGE, relief=GROOVE)
    b_salvar.grid(row=7, column=1, pady=5, sticky=NSEW)
#ver livros empprestados
def ver_livros_emprestados():
    app_ = Label(frameDireito,text="Todos os livros emprestados",width=50,compound=LEFT, padx=5,pady=10, relief=FLAT, anchor=NW, font=('Verdana 12'),bg=co1, fg=co4)
    app_.grid(row=0, column=0, columnspan=4, sticky=NSEW)
    l_linha = Label(frameDireito, width=400, height=1,anchor=NW, font=('Verdana 1 '), bg=co3, fg=co1)
    l_linha.grid(row=1, column=0, columnspan=4, sticky=NSEW)

    dados = []

    books_on_loan = get_books_on_loan()


    for  book in books_on_loan:
         dado = [f"{book[0]}", f"{book[1]}", f"{book[2]}",f"{book[3]}",f"{book[4]}"]
    
         dados.append(dado)



    #creating a treeview with dual scrollbars
    list_header = ['Titulo','Nome do usuario','Data de emprestimo','Data de devolução']
    
    global tree

    tree = ttk.Treeview(frameDireito, selectmode="extended", columns=list_header, show="headings")
    vsb = ttk.Scrollbar(frameDireito, orient="vertical", command=tree.yview)
    hsb = ttk.Scrollbar(frameDireito, orient="horizontal", command=tree.xview)
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=2, sticky='nsew')
    vsb.grid(column=1, row=2, sticky='ns')
    hsb.grid(column=0, row=3, sticky='ew')
    frameDireito.grid_rowconfigure(0, weight=12)
    
    hd=["nw","nw","ne","ne","ne","ne"]
    h=[20,175,120,90,90,100,100]
    n=0

    for col in list_header:
        tree.heading(col, text=col, anchor='nw')
        #adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])
        n+=1

    for item in dados:
        tree.insert('', 'end', values=item)

# Função para controlar o menu
def control(i):
    #novo usuario
    if i == 'novo_usuario':
        for widget in frameDireito.winfo_children():
            widget.destroy()
            #chamando a nova funcao 
        novo_usuario()

#Ver usuarios
    if i == 'ver_usuarios':
        for widget in frameDireito.winfo_children():
            widget.destroy()
            #chamando a nova funcao 
        ver_usuarios()       

#novo livro
    if i == 'novo_livro':
        for widget in frameDireito.winfo_children():
            widget.destroy()
            #chamando a nova funcao 
        novo_livro()

#Ver livros
    if i == 'ver_livro':
        for widget in frameDireito.winfo_children():
            widget.destroy()
            #chamando a funcao ver livro
        ver_livros()  

# realizare mprestimo

    if i == 'emprestimo':
        for widget in frameDireito.winfo_children():
            widget.destroy()
            #chamando a funcao ver livro
        realizar_emprestimo()  



#ver livro emprestados

    if i == 'ver_livros_emprestados':
            for widget in frameDireito.winfo_children():
                widget.destroy()

            #chamando a funcao ver livro emprestado
            ver_livros_emprestados()



# Menu de navegação
# NOVO USUARIO
img_usuario = Image.open('add.png')
img_usuario = img_usuario.resize((18, 18))
img_usuario = ImageTk.PhotoImage(img_usuario)
b_usuario = Button(frameEsquerdo, command=lambda: control('novo_usuario'), image=img_usuario, compound=LEFT, anchor=NW, text="Novo Usuario", bg=co4, fg=co1, font=('Ivy', 11), overrelief=RIDGE, relief=GROOVE)
b_usuario.grid(row=0, column=0, sticky=NSEW, padx=5, pady=6)

# NOVO LIVRO
img_novo_livro = Image.open('add.png')
img_novo_livro = img_novo_livro.resize((18, 18))
img_novo_livro = ImageTk.PhotoImage(img_novo_livro)
b_novo_livro = Button(frameEsquerdo, command=lambda: control('novo_livro'), image=img_novo_livro, compound=LEFT, anchor=NW, text="Adicionar Livro", bg=co4, fg=co1, font=('Ivy', 11), overrelief=RIDGE, relief=GROOVE)
b_novo_livro.grid(row=1, column=0, sticky=NSEW, padx=5, pady=6)

# VER LIVROS
img_ver_livro = Image.open('add.png')
img_ver_livro = img_ver_livro.resize((18, 18))
img_ver_livro = ImageTk.PhotoImage(img_ver_livro)
b_ver_livro = Button(frameEsquerdo,command=lambda:control('ver_livro'),image=img_ver_livro, compound=LEFT, anchor=NW, text="Exibir Todos Os Livros", bg=co4, fg=co1, font=('Ivy', 11), overrelief=RIDGE, relief=GROOVE)
b_ver_livro.grid(row=2, column=0, sticky=NSEW, padx=5, pady=6)

# VER USUÁRIOS
img_ver_usuario = Image.open('add.png')
img_ver_usuario = img_ver_usuario.resize((18, 18))
img_ver_usuario = ImageTk.PhotoImage(img_ver_usuario)
b_ver_usuario = Button(frameEsquerdo,command=lambda:control('ver_usuarios'), image=img_ver_usuario, compound=LEFT, anchor=NW, text="Exibir Usuários Cadastrados", bg=co4, fg=co1, font=('Ivy', 11), overrelief=RIDGE, relief=GROOVE)
b_ver_usuario.grid(row=3, column=0, sticky=NSEW, padx=5, pady=6)


# REALIZAR UM EMPRÉSTIMO
img_realizar_emprestimo = Image.open('add.png')
img_realizar_emprestimo = img_realizar_emprestimo.resize((18, 18))
img_realizar_emprestimo = ImageTk.PhotoImage(img_realizar_emprestimo)
b_realizar_emprestimo = Button(frameEsquerdo, command=lambda:control('emprestimo'), image=img_realizar_emprestimo, compound=LEFT, anchor=NW, text="Realizar Um Novo Empréstimo", bg=co4, fg=co1, font=('Ivy', 11), overrelief=RIDGE, relief=GROOVE)
b_realizar_emprestimo.grid(row=4, column=0, sticky=NSEW, padx=5, pady=6)

# DEVOLUÇÃO DE EMPRÉSTIMO
img_devolucao_emprestimo = Image.open('add.png')
img_devolucao_emprestimo = img_devolucao_emprestimo.resize((18, 18))
img_devolucao_emprestimo = ImageTk.PhotoImage(img_devolucao_emprestimo)
b_devolucao_emprestimo = Button(frameEsquerdo, image=img_devolucao_emprestimo, compound=LEFT, anchor=NW, text="Devoluções", bg=co4, fg=co1, font=('Ivy', 11), overrelief=RIDGE, relief=GROOVE)
b_devolucao_emprestimo.grid(row=5, column=0, sticky=NSEW, padx=5, pady=6)

# LIVROS EMPRESTADOS
img_livros_emprestados = Image.open('add.png')
img_livros_emprestados = img_livros_emprestados.resize((18, 18))
img_livros_emprestados = ImageTk.PhotoImage(img_livros_emprestados)
b_livros_emprestados = Button(frameEsquerdo,command=lambda:control('ver_livros_emprestados'), image=img_livros_emprestados, compound=LEFT, anchor=NW, text="Empréstimos Em Andamento", bg=co4, fg=co1, font=('Ivy', 11), overrelief=RIDGE, relief=GROOVE)
b_livros_emprestados.grid(row=6, column=0, sticky=NSEW, padx=5, pady=6)

# Exibindo a janela
janela.mainloop()
