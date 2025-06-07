from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd

from PIL import ImageTk, Image

from tkcalendar import Calendar, DateEntry
from datetime import date

from main import *

co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # Branca   
co2 = "#e5e5e5"  # grey
co3 = "#00a095"  # Verde
co4 = "#403d3d"   # letra
co6 = "#003452"   # azul
co7 = "#ef5350"   # vermelha

co6 = "#146C94"   # azul
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # + verde

#criando janela principal

janela = Tk()
janela.title("Cadastro de Pessoas")
janela.geometry('850x600')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

style = Style(janela)
style.theme_use("clam")


#criando frames
frame_logo = Frame(janela, width=850, height=52, bg=co6)
frame_logo.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW, columnspan=5)


frame_botoes = Frame(janela, width=100, height=200, bg=co1, relief=RAISED)
frame_botoes.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frame_detalhes = Frame(janela, width=800, height=100, bg=co1, relief=SOLID)
frame_detalhes.grid(row=1, column=1, pady=1, padx=10, sticky=NSEW)

frame_tabela = Frame(janela, width=100, height=100, bg=co1, relief=RAISED)
frame_tabela.grid(row=3, column=0, pady=0, padx=10, sticky=NSEW, columnspan=5)

#frame logo

global imagem, imagem_string, l_imagem

app_lg = Image.open('logo.png')
app_lg = app_lg.resize((50,50))
app_lg = ImageTk.PhotoImage(app_lg)
app_logo = Label(frame_logo, image=app_lg, text="Sistema de Cadastro de Pessoas", width=850, compound=LEFT, anchor=NW, font=("Verdana 15"), bg=co6, fg=co1)
app_logo.place(x=5, y=0)

#abrindo imagem 

imagem = Image.open("pessoa.webp")
imagem = imagem.resize((132,132))
imagem = ImageTk.PhotoImage(imagem)
l_imagem = Label(frame_detalhes, image=imagem, bg=co1, fg=co4)
l_imagem.place(x=435, y=10)

#criando funções ---------------------------------------
#adicionar

def adicionar():
    global imagem, imagem_string, l_imagem

    #obtendo os valores 
    nome = e_nome.get()
    endereco = e_endereco.get()
    cpf = e_cpf.get()
    sexo = c_sexo.get()
    rg = e_rg.get()
    data = data_nasc.get()
    signo = e_signo.get()
    img = imagem_string

    lista = [nome, endereco, cpf, rg, sexo, data, signo, img]

    #verifica se a lista contem valores

    for i in lista:
        if i=="":
            messagebox.showerror("Erro", "Preencha todos os campos!")
            return
    
    #inserir valores

    sistema_de_registro.registrar_pessoa(lista)

    #limpando campos apos entrada

    e_nome.delete(0, END)
    e_endereco.delete(0, END)
    e_cpf.delete(0, END)
    c_sexo.delete(0, END)
    e_rg.delete(0, END)
    data_nasc.delete(0, END)
    e_signo.delete(0, END)

    #mostrando valores na tabela

    mostrar_pessoas()

#pesquisar pessoas

def pesquisar():
    global imagem, imagem_string, l_imagem

    #obtendo ID
    id_pessoa = int(e_pesquisar.get())

    #chamar função
    dados = sistema_de_registro.pesquisar_pessoas(id_pessoa)

    e_nome.delete(0, END)
    e_endereco.delete(0, END)
    e_cpf.delete(0, END)
    c_sexo.delete(0, END)
    e_rg.delete(0, END)
    data_nasc.delete(0, END)
    e_signo.delete(0, END)

    #inserir valores nos campos

    e_nome.insert(END, dados[1])
    e_endereco.insert(END, dados[2])
    e_cpf.insert(END, dados[3])
    c_sexo.insert(END, dados[4])
    e_rg.insert(END, dados[5])
    data_nasc.insert(END, dados[6])
    e_signo.insert(END, dados[7])

    imagem = dados[8]
    imagem_string = imagem

    imagem = Image.open(imagem)
    imagem = imagem.resize((132,132))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(frame_detalhes, image=imagem, bg=co1, fg=co4)
    l_imagem.place(x=435, y=10)


#funcao atualizar
def atualizar():
    global imagem, imagem_string, l_imagem

    id_pessoa = int(e_pesquisar.get())

    #obtendo os valores 
    nome = e_nome.get()
    endereco = e_endereco.get()
    cpf = e_cpf.get()
    sexo = c_sexo.get()
    rg = e_rg.get()
    data = data_nasc.get()
    signo = e_signo.get()
    img = imagem_string

    lista = [nome, endereco, cpf, rg, sexo, data, signo, img]

    #verifica se a lista contem valores

    for i in lista:
        if i=="":
            messagebox.showerror("Erro", "Preencha todos os campos!")
            return
    
    #inserir valores

    sistema_de_registro.atualizar_pessoa(lista)

    #limpando campos apos entrada

    e_nome.delete(0, END)
    e_endereco.delete(0, END)
    e_cpf.delete(0, END)
    c_sexo.delete(0, END)
    e_rg.delete(0, END)
    data_nasc.delete(0, END)
    e_signo.delete(0, END)

    imagem = Image.open('logo.png')
    imagem = imagem.resize((130,130))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(frame_detalhes, image=imagem, bg=co1, fg=co4)
    l_imagem.place(x=450, y=10)

    #mostrando valores na tabela

    mostrar_pessoas()

def deletar():
    global imagem, imagem_string, l_imagem

    id_pessoa = int(e_pesquisar.get())

    #deletando pessoa
    sistema_de_registro.deletar_pessoa(id_pessoa)

    #limpando campos apos entrada

    e_nome.delete(0, END)
    e_endereco.delete(0, END)
    e_cpf.delete(0, END)
    c_sexo.delete(0, END)
    e_rg.delete(0, END)
    data_nasc.delete(0, END)
    e_signo.delete(0, END)

    e_pesquisar.delete(0,END)

    imagem = Image.open('logo.png')
    imagem = imagem.resize((130,130))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(frame_detalhes, image=imagem, bg=co1, fg=co4)
    l_imagem.place(x=450, y=10)

    #mostrando valores na tabela

    mostrar_pessoas()

#criando campos de entrada

l_nome = Label(frame_detalhes, text="Nome *", anchor=NW, font="Ivy 10", bg=co1, fg=co4)
l_nome.place(x=4, y=10)
e_nome = Entry(frame_detalhes, width=25, justify='left', relief='solid')
e_nome.place(x=7, y=40)


l_endereco = Label(frame_detalhes, text="Endereço *", anchor=NW, font="Ivy 10", bg=co1, fg=co4)
l_endereco.place(x=4, y=70)
e_endereco = Entry(frame_detalhes, width=25, justify='left', relief='solid')
e_endereco.place(x=7, y=100)


l_cpf = Label(frame_detalhes, text="CPF *", anchor=NW, font="Ivy 10", bg=co1, fg=co4)
l_cpf.place(x=4, y=130)
e_cpf = Entry(frame_detalhes, width=11, justify='left', relief='solid')
e_cpf.place(x=7, y=160)

l_sexo = Label(frame_detalhes, text="Sexo *", anchor=NW, font="Ivy 10", bg=co1, fg=co4)
l_sexo.place(x=127, y=130)
c_sexo = ttk.Combobox(frame_detalhes, width=5, font=('Ivy 11'), justify="center")
c_sexo['values'] = ("M", "F")
c_sexo.place(x=130, y=160)

l_data_nasc = Label(frame_detalhes, text="Data de Nascimento *", anchor=NW, font="Ivy 10", bg=co1, fg=co4)
l_data_nasc.place(x=240, y=10)
data_nasc = DateEntry(frame_detalhes, width=10, justify='center', background='darkblue', foreground='white', borderwidth=2, year=2000)
data_nasc.place(x=240, y=40)


l_rg = Label(frame_detalhes, text="RG *", anchor=NW, font="Ivy 10", bg=co1, fg=co4)
l_rg.place(x=240, y=70)
e_rg = Entry(frame_detalhes, width=10, justify='left', relief='solid')
e_rg.place(x=240, y=100)

l_signo = Label(frame_detalhes, text="Signo *", anchor=NW, font="Ivy 10", bg=co1, fg=co4)
l_signo.place(x=240, y=130)
e_signo = Entry(frame_detalhes, width=10, justify='left', relief='solid')
e_signo.place(x=240, y=160)

#escolher imagem



def escolher_imagem():
    global imagem, imagem_string, l_imagem

    imagem = fd.askopenfilename()
    imagem_string = imagem

    imagem = Image.open(imagem)
    imagem = imagem.resize((130,130))
    imagem = ImageTk.PhotoImage(imagem)
    l_imagem = Label(frame_detalhes, image=imagem, bg=co1, fg=co4)
    l_imagem.place(x=450, y=10)

    botao_carregar['text'] = 'Trocar de Foto'

botao_carregar = Button(frame_detalhes, command=escolher_imagem, text="Carregar foto".upper(), width=20, compound=CENTER, anchor=CENTER, overrelief=RIDGE, font="Ivy 7 bold", bg=co1, fg=co0)
botao_carregar.place(x=430, y=160)

def mostrar_pessoas():

    list_header = ['id', 'nome', 'endereco', 'cpf', 'rg', 'sexo', 'Data Nasc.', 'signo']

    df_list = sistema_de_registro.listar_pessoas()

    tree_pessoa = ttk.Treeview(frame_tabela, selectmode="extended", columns=list_header, show="headings")

    vsb = ttk.Scrollbar(frame_tabela, orient="vertical", command=tree_pessoa.yview)

    hsb = ttk.Scrollbar(frame_tabela, orient="horizontal", command=tree_pessoa.xview)

    tree_pessoa.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree_pessoa.grid(column=0, row=1, sticky="nsew")
    vsb.grid(column=1, row=1, sticky="ns")
    hsb.grid(column=0, row=2, sticky="ew")
    frame_tabela.grid_rowconfigure(0, weight=12)

    hd = ["nw", "nw", "center", "center", "center", "center", "center", "nw"]
    h=[40,150,150,100,100,50,100,130]
    n=0

    for col in list_header:
        tree_pessoa.heading(col, text=col.title(), anchor=NW)
        tree_pessoa.column(col, width=h[n], anchor=hd[n])

        n+=1

    for item in df_list:
        tree_pessoa.insert('', 'end', values=item)


#pesquisar pessoa
frame_pesquisar = Frame(frame_botoes, width=40, height=50, bg=co1, relief=RAISED)
frame_pesquisar.grid(row=0, column=0, pady=10, padx=10, sticky=NSEW)

l_nome = Label(frame_pesquisar, text="Procurar pessoa [ID]", anchor=NW, font="Ivy 10", bg=co1, fg=co4)
l_nome.grid(row=0, column=0, pady=10, padx=0, sticky=NSEW)
e_pesquisar = Entry(frame_pesquisar, width=5, justify='center', relief='solid', font="Ivy 10")
e_pesquisar.grid(row=1, column=0, pady=10, padx=0, sticky=NSEW)

botao_pesquisar = Button(frame_pesquisar, command=pesquisar, text="Procurar", width=9,  anchor=CENTER, overrelief=RIDGE, font="Ivy 7 bold", bg=co1, fg=co0)
botao_pesquisar.grid(row=1, column=1, pady=10, padx=0, sticky=NSEW)

#botões -------------------------------------------------

app_img_adicionar = Image.open('add.png')
app_img_adicionar = app_img_adicionar.resize((25,25))
app_img_adicionar = ImageTk.PhotoImage(app_img_adicionar)
app_adicionar = Button(frame_botoes, command=adicionar, image=app_img_adicionar, relief=GROOVE, text="Adicionar", width=100, compound=LEFT, overrelief=RIDGE, font="Ivy 11", bg=co1, fg=co0)
app_adicionar.grid(row=1, column=0, pady=5, padx=10, sticky=NSEW)

app_img_atualizar = Image.open('update.png')
app_img_atualizar = app_img_atualizar.resize((25,25))
app_img_atualizar = ImageTk.PhotoImage(app_img_atualizar)
app_atualizar = Button(frame_botoes, command=atualizar, image=app_img_atualizar, relief=GROOVE, text="Atualizar", width=100, compound=LEFT, overrelief=RIDGE, font="Ivy 11", bg=co1, fg=co0)
app_atualizar.grid(row=2, column=0, pady=5, padx=10, sticky=NSEW)

app_img_deletar = Image.open('delete.png')
app_img_deletar = app_img_deletar.resize((25,25))
app_img_deletar = ImageTk.PhotoImage(app_img_deletar)
app_deletar = Button(frame_botoes, image=app_img_deletar, command=deletar, relief=GROOVE, text="Deletar", width=100, compound=LEFT, overrelief=RIDGE, font="Ivy 11", bg=co1, fg=co0)
app_deletar.grid(row=3, column=0, pady=5, padx=10, sticky=NSEW)

#linha sepatarória ___________________________________

l_linha = Label(frame_botoes, relief=GROOVE, width=1, height=123, anchor=NW, font="Ivy 1", bg=co1, fg=co1)
l_linha.place(x=233,y=15)

#chamar tabela
mostrar_pessoas()

janela.mainloop()

