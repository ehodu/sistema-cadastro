import sqlite3
from tkinter import messagebox

class Registro:
    def __init__(self):
        self.conn = sqlite3.connect('pessoas.db')
        self.c = self.conn.cursor()
        self.create_table()
    
    def create_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS listaPessoas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    endereco TEXT NOT NULL,
                    cpf INTEGER NOT NULL,
                    rg VARCHAR(18) NOT NULL,
                    sexo CHAR,
                    data_nasc TEXT,
                    signo TEXT NOT NULL,
                    foto TEXT
                    )
                       ''')
    
    def registrar_pessoa(self, listaPessoas):
        self.c.execute("INSERT INTO listaPessoas(nome, endereco, cpf, rg, sexo, data_nasc, signo, foto) VALUES (?,?,?,?,?,?,?,?)", (listaPessoas))
        self.conn.commit()
        
        #Mostrando mensagem de sucesso
        messagebox.showinfo("Cadastro", "Cadastro realizado com sucesso!")

    def listar_pessoas(self):
        self.c.execute("SELECT * FROM listaPessoas")
        dados = self.c.fetchall()
        
        return dados
        
    def pesquisar_pessoas(self, id):
        self.c.execute("SELECT * FROM listaPessoas WHERE id=?", (id,))
        dados = self.c.fetchone()
        return dados

    def atualizar_pessoa(self, novoValores):
        query = "UPDATE listaPessoas SET nome=?, endereco=?, cpf=?, rg=?, sexo=?, data_nasc=?, signo=?, foto=? WHERE id=?"
        self.c.execute(query, novoValores)
        self.conn.commit()
        
        messagebox.showinfo("Sucesso", f"Cadastro atualizado com sucesso para a pessoa com o ID: {novoValores[9]}!")

    def deletar_pessoa(self, id):
        self.c.execute("DELETE FROM listaPessoas WHERE id=?", (id,))
        self.conn.commit()

        messagebox.showinfo("Sucesso", f"Pessoa com o ID: {id} foi deletada com sucesso!")


sistema_de_registro = Registro()

