import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
import sqlite3


class funcs:
    def conecta_bd(self):
        self.conn = sqlite3.connect("clientes.bd")
        self.cursor = self.conn.cursor()
    def desconectar_bd(self):
        self.conn.close(); print("DESCONECTANDO DO BANCO DE DADOS!")
    def tabelas(self):
        self.conecta_bd();
        print("CONECTANDO AO BANCO DE DADOS!")


        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios(
                id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_usuario TEXT NOT NULL,
                cpf_usuario TEXT NOT NULL UNIQUE,
                email_usuario TEXT NOT NULL UNIQUE,
                telefone_usuario TEXT NOT NULL,
                data_nascimento TEXT NOT NULL,
                rua TEXT NOT NULL,
                cep TEXT NOT NULL,
                bairro TEXT NOT NULL,
                cidade TEXT NOT NULL,
                senha TEXT NOT NULL,
                tipo TEXT NOT NULL CHECK(tipo IN ('admin', 'vendedor', 'financeiro', 'estoque')),
                permissao TEXT NOT NULL DEFAULT 'padrao'
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_cliente TEXT NOT NULL,
                cpf_cliente TEXT NOT NULL UNIQUE,
                email_cliente TEXT NOT NULL UNIQUE,
                telefone_cliente TEXT NOT NULL,
                data_nascimento TEXT NOT NULL,
                rua TEXT NOT NULL,
                cep TEXT NOT NULL,
                bairro TEXT NOT NULL,
                cidade TEXT NOT NULL
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS fornecedores (
                id_fornecedor INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                cnpj TEXT NOT NULL UNIQUE,
                telefone TEXT,
                email TEXT UNIQUE,
                rua TEXT NOT NULL,
                cep TEXT NOT NULL,
                bairro TEXT NOT NULL,
                cidade TEXT NOT NULL
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS produtos (
                id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                descricao TEXT,
                preco_venda REAL NOT NULL,
                preco_compra REAL NOT NULL,
                fornecedor_id INTEGER,
                FOREIGN KEY(fornecedor_id) REFERENCES fornecedores(id)
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS estoque (
                id_estoque INTEGER PRIMARY KEY AUTOINCREMENT,
                produto_id INTEGER NOT NULL,
                quantidade INTEGER NOT NULL DEFAULT 0,
                FOREIGN KEY(produto_id) REFERENCES produtos(id)
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS vendas (
                id_vendas INTEGER PRIMARY KEY AUTOINCREMENT,
                cliente_id INTEGER NOT NULL,
                usuario_id INTEGER NOT NULL,
                data_venda TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                total REAL NOT NULL,
                FOREIGN KEY(cliente_id) REFERENCES clientes(id),
                FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS compras (
                id_compras INTEGER PRIMARY KEY AUTOINCREMENT,
                fornecedor_id INTEGER NOT NULL,
                usuario_id INTEGER NOT NULL,
                data_compra TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                total REAL NOT NULL,
                FOREIGN KEY(fornecedor_id) REFERENCES fornecedores(id),
                FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS financeiro (
                id_financeiro INTEGER PRIMARY KEY AUTOINCREMENT,
                tipo TEXT NOT NULL CHECK(tipo IN ('entrada', 'saida')),
                valor REAL NOT NULL,
                descricao TEXT,
                data TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
        """)

        self.conn.commit();print("BANCO DE DADOS CRIADO!")
        self.desconectar_bd()
    def limpar_tela(self):
        self.codigo_entry.delete(0, END)
        self.nome_entry.delete(0, END)
        self.cpf_entry.delete(0, END)
        self.email_entry.delete(0, END)
        self.telefone_entry.delete(0, END)
        self.datanascimento_entry.delete(0, END)
        self.rua_entry.delete(0, END)
        self.cep_entry.delete(0, END)
        self.bairro_entry.delete(0, END)
        self.cidade_entry.delete(0, END)
    def limpar_telacad(self):
        self.nome_entry.delete(0, END)
        self.cpf_entry.delete(0, END)
        self.email_entry.delete(0, END)
        self.telefone_entry.delete(0, END)
        self.datanascimento_entry.delete(0, END)
        self.rua_entry.delete(0, END)
        self.cep_entry.delete(0, END)
        self.bairro_entry.delete(0, END)
        self.cidade_entry.delete(0, END)
    def limpar_telacadu(self):
        self.nome_entry.delete(0, END)
        self.cpf_entry.delete(0, END)
        self.email_entry.delete(0, END)
        self.telefone_entry.delete(0, END)
        self.datanascimento_entry.delete(0, END)
        self.rua_entry.delete(0, END)
        self.cep_entry.delete(0, END)
        self.bairro_entry.delete(0, END)
        self.cidade_entry.delete(0, END)
        self.senha_entry.delete(0, END)
        self.tipo_combo.delete(0,END)
    def limpar_telacon_u(self):
        self.codigo_entry.delete(0, END)
        self.nome_entry.delete(0, END)
        self.cpf_entry.delete(0, END)
        self.email_entry.delete(0, END)
        self.telefone_entry.delete(0, END)
        self.datanascimento_entry.delete(0, END)
        self.rua_entry.delete(0, END)
        self.cep_entry.delete(0, END)
        self.bairro_entry.delete(0, END)
        self.cidade_entry.delete(0, END)
        self.senha_entry.delete(0, END)
        self.tipo_combo.delete(0,END)
        self.permissao_combo.delete(0,END)
    def limpar_telaconforne(self):
        self.codigo_entry.delete(0, END)
        self.nome_entry.delete(0, END)
        self.cnpj_entry.delete(0, END)
        self.email_entry.delete(0, END)
        self.telefone_entry.delete(0, END)
        self.rua_entry.delete(0, END)
        self.cep_entry.delete(0, END)
        self.bairro_entry.delete(0, END)
        self.cidade_entry.delete(0, END)
    def limpar_telacadfor(self):
        self.nome_entry.delete(0, END)
        self.cnpj_entry.delete(0, END)
        self.email_entry.delete(0, END)
        self.telefone_entry.delete(0, END)
        self.rua_entry.delete(0, END)
        self.cep_entry.delete(0, END)
        self.bairro_entry.delete(0, END)
        self.cidade_entry.delete(0, END)
    def limpar_telacadpro(self):
        self.codigo_entry.delete(0, END)
        self.nome_entry.delete(0, END)
        self.v_venda_entry.delete(0, END)
        self.v_compra_entry.delete(0, END)
        self.fornecedor_combo.delete(0, END)
        self.descrição_entry.delete(0, END)
    def limpar_telacadprod(self):
        self.nome_entry.delete(0, END)
        self.v_venda_entry.delete(0, END)
        self.v_compra_entry.delete(0, END)
        self.fornecedor_combo.delete(0, END)
        self.descrição_entry.delete(0, END)
    def add_cliente(self):
        self.conecta_bd()


        self.nome = self.nome_entry.get()
        self.nascimento = self.datanascimento_entry.get()
        self.cpf = self.cpf_entry.get()
        self.telefone = self.telefone_entry.get()
        self.email = self.email_entry.get()
        self.rua = self.rua_entry.get()
        self.cep = self.cep_entry.get()
        self.bairro = self.bairro_entry.get()
        self.cidade = self.cidade_entry.get()

        self.cursor = self.conn.cursor()



        self.cursor.execute(""" INSERT INTO clientes (nome_cliente,cpf_cliente,email_cliente,telefone_cliente,
                                                       data_nascimento,rua,cep,bairro,cidade) 
                                                       VALUES (?,?,?,?,?,?,?,?,?) """,
                            (self.nome, self.nascimento, self.cpf, self.telefone,self.email, self.rua,self.cep,
                             self.bairro,self.cidade))
        self.conn.commit()

        self.desconectar_bd()
        self.limpar_telacad()
        messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
    def select_lista(self):
        self.listacli.delete(*self.listacli.get_children())
        self.conecta_bd()
        lista = self.cursor.execute(""" SELECT * FROM clientes ORDER BY nome_cliente ASC; """)
        for i in lista:
            self.listacli.insert("",END, values=i)
        self.desconectar_bd()
    def deleta_cliente(self):

        self.codigo = self.codigo_entry.get()
        self.nome = self.nome_entry.get()
        self.nascimento = self.datanascimento_entry.get()
        self.cpf = self.cpf_entry.get()
        self.telefone = self.telefone_entry.get()
        self.email = self.email_entry.get()
        self.rua = self.rua_entry.get()
        self.cep = self.cep_entry.get()
        self.bairro = self.bairro_entry.get()
        self.cidade = self.cidade_entry.get()

        self.conecta_bd()
        self.cursor.execute("""DELETE FROM clientes WHERE id_cliente = ?""", (int(self.codigo),))
        self.conn.commit()

        self.desconectar_bd()
        self.limpar_tela()
        self.select_lista()
    def onDoubleClick(self, event):
        self.limpar_tela()
        self.listacli.selection()

        for n in self.listacli.selection():
            col1, col2,col3,col4,col5,col6,col7,col8,col9,col10 = self.listacli.item(n, 'values')
            self.codigo_entry.insert(END, col1)
            self.nome_entry.insert(END, col2)
            self.datanascimento_entry.insert(END,col3)
            self.cpf_entry.insert(END,col4)
            self.telefone_entry.insert(END, col5)
            self.email_entry.insert(END, col6)
            self.rua_entry.insert(END,col7)
            self.cep_entry.insert(END,col8)
            self.bairro_entry.insert(END,col9)
            self.cidade_entry.insert(END,col10)
    def alterar_cliente(self):
        self.codigo = self.codigo_entry.get()
        self.nome = self.nome_entry.get()
        self.nascimento = self.datanascimento_entry.get()
        self.cpf = self.cpf_entry.get()
        self.telefone = self.telefone_entry.get()
        self.email = self.email_entry.get()
        self.rua = self.rua_entry.get()
        self.cep = self.cep_entry.get()
        self.bairro = self.bairro_entry.get()
        self.cidade = self.cidade_entry.get()
        self.conecta_bd()
        self.conn.execute(""" 
        UPDATE clientes
        SET nome_cliente = ?, cpf_cliente = ?, email_cliente = ?, telefone_cliente = ?, data_nascimento = ?,
         rua = ?, cep = ?, bairro = ?, cidade = ? WHERE id_cliente = ?""",
                          (self.nome, self.nascimento, self.cpf, self.telefone,self.email,self.rua,self.cep,
                           self.bairro,self.cidade,self.codigo))
        self.conn.commit()
        self.desconectar_bd()
        self.select_lista()
        self.limpar_tela()
    def buscar_cliente(self):
        self.conecta_bd()
        self.listacli.delete(*self.listacli.get_children())

        self.nome_entry.insert(END,"%")
        nome = self.nome_entry.get()

        self.cursor.execute("SELECT * FROM clientes "
                            "WHERE nome_cliente LIKE '%s' ORDER BY nome_cliente ASC" % nome)

        buscandonomecli = self.cursor.fetchall()
        for i in buscandonomecli:
            self.listacli.insert("", END, values=i)
        self.limpar_tela()
        self.desconectar_bd()
    def add_usuario(self):
        self.conecta_bd()

        self.nome = self.nome_entry.get()
        self.nascimento = self.datanascimento_entry.get()
        self.cpf = self.cpf_entry.get()
        self.telefone = self.telefone_entry.get()
        self.email = self.email_entry.get()
        self.rua = self.rua_entry.get()
        self.cep = self.cep_entry.get()
        self.bairro = self.bairro_entry.get()
        self.cidade = self.cidade_entry.get()
        self.senha = self.senha_entry.get()
        self.tipo = self.tipo_combo.get()

        self.cursor = self.conn.cursor()

        self.cursor.execute(""" INSERT INTO usuarios (nome_usuario,cpf_usuario,email_usuario,telefone_usuario,
                                                        data_nascimento,rua,cep,bairro,cidade,senha,tipo) 
                                                        VALUES (?,?,?,?,?,?,?,?,?,?,?) """,
                            (self.nome, self.nascimento, self.cpf, self.telefone, self.email, self.rua, self.cep,
                             self.bairro, self.cidade, self.senha,self.tipo))
        self.conn.commit()

        self.desconectar_bd()
        self.limpar_telacadu()
        messagebox.showinfo("Sucesso", "Usuario cadastrado com sucesso!")
    def select_listausu(self):
        self.listausu.delete(*self.listausu.get_children())
        self.conecta_bd()
        lista = self.cursor.execute(""" SELECT * FROM usuarios ORDER BY nome_usuario ASC; """)
        for i in lista:
            self.listausu.insert("",END, values=i)
        self.desconectar_bd()
    def onDoubleClickUsu(self, event):
        self.limpar_tela()
        self.listausu.selection()

        for n in self.listausu.selection():
            col1, col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,col12,col13 = self.listausu.item(n, 'values')
            self.codigo_entry.insert(END, col1)
            self.nome_entry.insert(END, col2)
            self.datanascimento_entry.insert(END,col3)
            self.cpf_entry.insert(END,col4)
            self.telefone_entry.insert(END, col5)
            self.email_entry.insert(END, col6)
            self.rua_entry.insert(END,col7)
            self.cep_entry.insert(END,col8)
            self.bairro_entry.insert(END,col9)
            self.cidade_entry.insert(END,col10)
            self.senha_entry.insert(END, col11)
            self.tipo_combo.insert(END, col12)
            self.permissao_combo.insert(END, col13)
    def onDoubleClickforne(self, event):
        self.limpar_telaconforne()
        self.listaforne.selection()

        for n in self.listaforne.selection():
            col1, col2, col3, col4, col5, col6, col7, col8, col9 = self.listaforne.item(n, 'values')
            self.codigo_entry.insert(END, col1)
            self.nome_entry.insert(END, col2)
            self.cnpj_entry.insert(END, col3)
            self.email_entry.insert(END, col4)
            self.telefone_entry.insert(END, col5)
            self.rua_entry.insert(END, col6)
            self.cep_entry.insert(END, col7)
            self.bairro_entry.insert(END, col8)
            self.cidade_entry.insert(END, col9)
    def deleta_usuario(self):
        self.codigo = self.codigo_entry.get()
        self.nome = self.nome_entry.get()
        self.nascimento = self.datanascimento_entry.get()
        self.cpf = self.cpf_entry.get()
        self.telefone = self.telefone_entry.get()
        self.email = self.email_entry.get()
        self.rua = self.rua_entry.get()
        self.cep = self.cep_entry.get()
        self.bairro = self.bairro_entry.get()
        self.cidade = self.cidade_entry.get()
        self.senha = self.senha_entry.get()
        self.tipo = self.tipo_combo.get()
        self.permissao = self.permissao_combo.get()

        self.conecta_bd()
        self.cursor.execute("""DELETE FROM usuarios WHERE id_usuario = ?""", (int(self.codigo),))
        self.conn.commit()

        self.desconectar_bd()
        self.limpar_telacon_u()
        self.select_listausu()
    def deleta_fornecedor(self):
        self.codigo = self.codigo_entry.get()
        self.nome = self.nome_entry.get()
        self.cnpj = self.cnpj_entry.get()
        self.telefone = self.telefone_entry.get()
        self.email = self.email_entry.get()
        self.rua = self.rua_entry.get()
        self.cep = self.cep_entry.get()
        self.bairro = self.bairro_entry.get()
        self.cidade = self.cidade_entry.get()

        self.conecta_bd()
        self.cursor.execute("""DELETE FROM fornecedores WHERE id_fornecedor = ?""", (int(self.codigo),))
        self.conn.commit()

        self.desconectar_bd()
        self.limpar_telaconforne()
        self.select_listaforne()
    def deleta_produto(self):
        self.codigo = self.codigo_entry.get()
        self.nome = self.nome_entry.get()
        self.v_venda = self.v_venda_entry.get()
        self.v_compra = self.v_compra_entry.get()
        self.fornecedor = self.fornecedor_combo.get()
        self.descrição = self.descrição_entry.get()

        self.conecta_bd()
        self.cursor.execute("""DELETE FROM produtos WHERE id_produto = ?""", (int(self.codigo),))
        self.conn.commit()

        self.desconectar_bd()
        self.limpar_telacadpro()
        self.select_listaprod()
    def alterar_usuario(self):
            self.codigo = self.codigo_entry.get()
            self.nome = self.nome_entry.get()
            self.nascimento = self.datanascimento_entry.get()
            self.cpf = self.cpf_entry.get()
            self.telefone = self.telefone_entry.get()
            self.email = self.email_entry.get()
            self.rua = self.rua_entry.get()
            self.cep = self.cep_entry.get()
            self.bairro = self.bairro_entry.get()
            self.cidade = self.cidade_entry.get()
            self.senha = self.senha_entry.get()
            self.tipo = self.tipo_combo.get()
            self.permissao = self.permissao_combo.get()
            self.conecta_bd()
            self.conn.execute(""" 
            UPDATE usuarios
            SET nome_usuario = ?, cpf_usuario = ?, email_usuario = ?, telefone_usuario = ?, data_nascimento = ?,
             rua = ?, cep = ?, bairro = ?, cidade = ?,senha = ?, tipo = ?, permissao = ? WHERE id_usuario = ?""",
                              (self.nome, self.nascimento, self.cpf, self.telefone, self.email, self.rua, self.cep,
                               self.bairro, self.cidade, self.senha, self.tipo, self.permissao, self.codigo))
            self.conn.commit()
            self.desconectar_bd()
            self.select_listausu()
            self.limpar_telacon_u()
    def alterar_fornecedor(self):
            self.codigo = self.codigo_entry.get()
            self.nome = self.nome_entry.get()
            self.cnpj = self.cnpj_entry.get()
            self.telefone = self.telefone_entry.get()
            self.email = self.email_entry.get()
            self.rua = self.rua_entry.get()
            self.cep = self.cep_entry.get()
            self.bairro = self.bairro_entry.get()
            self.cidade = self.cidade_entry.get()
            self.conecta_bd()
            self.conn.execute(""" 
            UPDATE fornecedores
            SET nome = ?, cnpj = ?, email = ?, telefone = ?,
             rua = ?, cep = ?, bairro = ?, cidade = ? 
             WHERE id_fornecedor = ?""",
                              (self.nome, self.cnpj, self.telefone, self.email, self.rua, self.cep,
                               self.bairro, self.cidade, self.codigo))
            self.conn.commit()
            self.desconectar_bd()
            self.select_listaforne()
            self.limpar_telaconforne()
    def alterar_produto(self):
            self.codigo = self.codigo_entry.get()
            self.nome = self.nome_entry.get()
            self.v_venda = self.v_venda_entry.get()
            self.v_compra = self.v_compra_entry.get()
            self.fornecedor = self.fornecedor_combo.get()
            self.descrição = self.descrição_entry.get()

            self.conecta_bd()
            self.conn.execute(""" 
            UPDATE produtos
            SET nome = ?, descricao = ?, preco_venda = ?, preco_compra = ?, fornecedor_id = ? 
            WHERE id_produto = ?""",
                              (self.nome, self.v_venda, self.v_compra,
                               self.fornecedor, self.descrição, self.codigo))
            self.conn.commit()
            self.desconectar_bd()
            self.select_listaprod()
            self.limpar_telacadpro()
    def buscar_usuario(self):
        self.conecta_bd()
        self.listausu.delete(*self.listausu.get_children())

        self.nome_entry.insert(END,"%")
        nome = self.nome_entry.get()

        self.cursor.execute("SELECT * FROM usuarios "
                            "WHERE nome_usuario LIKE '%s' ORDER BY nome_usuario ASC" % nome)

        buscandonomeusu = self.cursor.fetchall()
        for i in buscandonomeusu:
            self.listausu.insert("", END, values=i)
        self.limpar_telacon_u()
        self.desconectar_bd()
    def buscar_fornecedor(self):
        self.conecta_bd()
        self.listaforne.delete(*self.listaforne.get_children())

        self.nome_entry.insert(END,"%")
        nome = self.nome_entry.get()

        self.cursor.execute("SELECT * FROM fornecedores "
                            "WHERE nome LIKE '%s' ORDER BY nome ASC" % nome)

        buscandonomefor = self.cursor.fetchall()
        for i in buscandonomefor:
            self.listaforne.insert("", END, values=i)
        self.limpar_telaconforne()
        self.desconectar_bd()
    def buscar_produto(self):
        self.conecta_bd()
        self.listaprod.delete(*self.listaprod.get_children())

        self.nome_entry.insert(END, "%")
        nome = self.nome_entry.get()

        self.cursor.execute("SELECT * FROM produtos "
                            "WHERE nome LIKE '%s' ORDER BY nome ASC" % nome)

        buscandonomeprod = self.cursor.fetchall()
        for i in buscandonomeprod:
            self.listaprod.insert("", END, values=i)
        self.limpar_telacadpro()
        self.desconectar_bd()
    def add_fornecedor(self):
        self.conecta_bd()

        self.nome = self.nome_entry.get()
        self.cnpj = self.cnpj_entry.get()
        self.telefone = self.telefone_entry.get()
        self.email = self.email_entry.get()
        self.rua = self.rua_entry.get()
        self.cep = self.cep_entry.get()
        self.bairro = self.bairro_entry.get()
        self.cidade = self.cidade_entry.get()

        self.cursor = self.conn.cursor()

        self.cursor.execute(""" INSERT INTO fornecedores (nome,cnpj,email,telefone,
                                                        rua,cep,bairro,cidade) 
                                                        VALUES (?,?,?,?,?,?,?,?) """,
                            (self.nome, self.cnpj, self.telefone, self.email, self.rua, self.cep,
                             self.bairro, self.cidade))
        self.conn.commit()

        self.desconectar_bd()
        self.limpar_telacadfor()
        messagebox.showinfo("Sucesso", "Fornecedor cadastrado com sucesso!")
    def select_listaforne(self):
        self.listaforne.delete(*self.listaforne.get_children())
        self.conecta_bd()
        lista = self.cursor.execute(""" SELECT * FROM fornecedores ORDER BY nome ASC; """)
        for i in lista:
            self.listaforne.insert("", END, values=i)
        self.desconectar_bd()
    def comboforne(self):
        self.conecta_bd()

        self.cursor.execute("SELECT id_fornecedor, nome FROM fornecedores")
        self.fornecedores = self.cursor.fetchall()

        # Verifica se encontrou fornecedores antes de atualizar a Combobox
        if self.fornecedores:
            self.fornecedor_combo['values'] = [f"{id_fornecedor} - {nome}" for id_fornecedor, nome in self.fornecedores]

        self.desconectar_bd()
    def add_produto(self):
        self.conecta_bd()

        self.nome = self.nome_entry.get()
        self.venda = self.v_venda_entry.get()
        self.compra = self.v_compra_entry.get()
        self.fornecedor =  self.fornecedor_combo.get()
        self.descricao = self.descrição_entry.get()

        self.cursor = self.conn.cursor()

        self.cursor.execute(""" INSERT INTO produtos (nome,descricao,preco_venda,preco_compra,
                                                        fornecedor_id) 
                                                        VALUES (?,?,?,?,?) """,
                            (self.nome, self.venda,self.compra,self.fornecedor,self.descricao))
        self.conn.commit()

        self.desconectar_bd()
        self.limpar_telacadprod()
        messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso!")
    def select_listaprod(self):
        self.listaprod.delete(*self.listaprod.get_children())
        self.conecta_bd()
        lista = self.cursor.execute(""" SELECT * FROM produtos ORDER BY nome ASC; """)
        for i in lista:
            self.listaprod.insert("", END, values=i)
        self.desconectar_bd()
    def onDoubleClickprod(self, event):
        self.limpar_telacadpro()
        self.listaprod.selection()

        for n in self.listaprod.selection():
            col1, col2,col3,col4,col5,col6 = self.listaprod.item(n, 'values')
            self.codigo_entry.insert(END, col1)
            self.nome_entry.insert(END, col2)
            self.v_venda_entry.insert(END, col3)
            self.v_compra_entry.insert(END,col4)
            self.fornecedor_combo.insert(END,col5)
            self.descrição_entry.insert(END, col6)
    def combo_produto(self):
        self.conecta_bd()

        # Consulta no banco de dados para obter produtos
        self.cursor.execute("SELECT id_produto, nome, preco_venda FROM produtos")
        self.produtos = self.cursor.fetchall()

        # Verifica se encontrou produtos antes de atualizar a Combobox
        if self.produtos:
            self.produto_combo['values'] = [f"{id_produto} - {nome} - {preco_venda}" for id_produto, nome, preco_venda in self.produtos]

        self.desconectar_bd()
    def atualizar_entry_produto(self, event):
        # Pega o valor selecionado no ComboBox
        produto_selecionado = self.produto_var.get()

        # Extraímos o id e o nome do produto
        codigo_produto = produto_selecionado.split(" - ")[0]
        nome_produto = produto_selecionado.split(" - ")[1] if " - " in produto_selecionado else produto_selecionado

        # Conecta ao banco para pegar o valor do produto (preco_venda)
        self.conecta_bd()

        # Busca o preço de venda (preco_venda) para o produto selecionado
        self.cursor.execute("SELECT preco_venda FROM produtos WHERE id_produto = ?", (codigo_produto,))
        preco_venda = self.cursor.fetchone()

        if preco_venda:
            preco_venda = preco_venda[0]  # Pega o valor do preço de venda
        else:
            preco_venda = "Não encontrado"

        # Desconecta do banco de dados
        self.desconectar_bd()

        # Atualiza os campos Entry com os dados
        self.produto_entry.delete(0, tkinter.END)  # Limpa o campo Entry do nome do produto
        self.produto_entry.insert(0, nome_produto)  # Insere o nome do produto no campo Entry

        # Atualiza o campo Entry do valor unitário (preco_venda)
        self.V_U_entry.delete(0, tkinter.END)  # Limpa o campo Entry do valor unitário
        self.V_U_entry.insert(0, preco_venda)  # Insere o valor unitário no campo Entry
    def combo_vendedor(self):
        self.conecta_bd()

        # Consulta no banco de dados para obter vendedores
        self.cursor.execute("SELECT id_usuario, nome_usuario FROM usuarios WHERE TIPO = 'vendedor'")
        self.vendedor = self.cursor.fetchall()

        # Verifica se encontrou vendedores antes de atualizar a Combobox
        if self.vendedor:
            # Preenche a Combobox com o id e nome do vendedor
            self.vendedor_combo['values'] = [f"{id_usuario} - {nome_usuario}" for id_usuario, nome_usuario in
                                            self.vendedor]

        self.desconectar_bd()
    def atualizar_entry_vendedor(self, event):
        # Pega o valor selecionado no ComboBox
        vendedor_selecionado = self.vendedor_var.get()

        # Extraímos o nome do vendedor (sem o id)
        nome_vendedor = vendedor_selecionado.split(" - ")[1] if " - " in vendedor_selecionado else vendedor_selecionado

        # Atualiza o campo Entry com o nome do vendedor
        self.nome_v_entry.delete(0, tkinter.END)  # Limpa o campo Entry
        self.nome_v_entry.insert(0, nome_vendedor)  # Insere o nome do vendedor selecionado
    def calcular_valor_total(self, event):
        try:
            # Pega os valores dos campos de entrada
            qtde = self.qtde_entry.get()  # Quantidade
            V_U = self.V_U_entry.get()  # Valor Unitário (agora com o nome V_U)

            # Depuração: Verificar se os valores estão sendo capturados corretamente
            print(f"Quantidade: '{qtde}', Valor Unitário: '{V_U}'")

            # Verificar se os valores não estão vazios e fazer a conversão
            if not qtde or not V_U:
                print("Erro: Qtde ou Valor Unitário está vazio!")
                qtde = 0
                V_U = 0
            else:
                # Remove o "R$", ponto (separador de milhar) e outros caracteres não numéricos antes da conversão
                V_U = V_U.replace("R$", "").replace(".", "").replace(",", ".")

                # Converte as entradas para float, tratando possíveis erros
                qtde = float(qtde.replace(",", "."))  # Garantir que vírgula seja tratada como ponto
                V_U = float(V_U)  # Agora V_U está limpo de "R$" e milhar

            # Depuração: Verificar se a conversão foi bem-sucedida
            print(f"Quantidade (convertida): {qtde}, Valor Unitário (convertido): {V_U}")

            # Calcula o valor total
            v_total = qtde * V_U  # O valor total agora é armazenado em v_total

            # Exibe o valor total no campo de entrada
            self.v_total_entry.delete(0, tkinter.END)
            self.v_total_entry.insert(0, f"{v_total:.2f}")  # Mostra com 2 casas decimais

            print(f"Valor Total: {v_total}")

        except ValueError as e:
            # Caso haja erro de conversão (ex: texto não numérico)
            print(f"Erro na conversão: {e}")
            self.v_total_entry.delete(0, tkinter.END)
            self.v_total_entry.insert(0, "0.00")
    def adicionar_produto(self):
        # Pegando os dados dos campos
        codigo_produto = self.produto_var.get()
        nome_produto = self.produto_entry.get()
        quantidade = self.qtde_entry.get()
        valor_unitario = self.V_U_entry.get()

        # Validação dos campos
        if not codigo_produto or not nome_produto or not quantidade or not valor_unitario:
            messagebox.showwarning("Campos inválidos", "Todos os campos devem ser preenchidos!")
            return

        # Verificando se a quantidade é um número inteiro válido
        try:
            quantidade = int(quantidade)
            if quantidade <= 0:
                raise ValueError("Quantidade não pode ser menor ou igual a zero.")
        except ValueError:
            messagebox.showerror("Erro", "A quantidade deve ser um número inteiro positivo.")
            return

        # Verificando se o valor unitário é um número válido
        try:
            valor_unitario = valor_unitario.replace("R$", "").replace(",", ".")  # Tratando o R$ e vírgula
            valor_unitario = float(valor_unitario)
            if valor_unitario <= 0:
                raise ValueError("Valor unitário não pode ser menor ou igual a zero.")
        except ValueError:
            messagebox.showerror("Erro", "O valor unitário deve ser um número válido.")
            return

        # Calculando o valor total
        valor_total = valor_unitario * quantidade

        # Adicionando o produto na tabela
        self.tabela_produtos.insert("", "end", values=(codigo_produto, nome_produto, quantidade, f"R$ {valor_unitario:.2f}", f"R$ {valor_total:.2f}"))

        self.atualizar_total_bruto()
        self.calcular_desconto()
        # Limpa os campos de entrada
        self.produto_entry.delete(0, tkinter.END)
        self.qtde_entry.delete(0, tkinter.END)
        self.V_U_entry.delete(0, tkinter.END)
    def combo_cliente(self):
        self.conecta_bd()

        # Consulta no banco de dados para obter os clientes
        self.cursor.execute("SELECT id_cliente, nome_cliente, telefone_cliente, rua, bairro, cidade FROM clientes")
        self.clienteadd = self.cursor.fetchall()

        # Verifica se encontrou clientes antes de atualizar a ComboBox
        if self.clienteadd:
            self.cliente_combo['values'] = [
                f"{id_cliente} - {nome_cliente} - {telefone_cliente} - {rua} - {bairro} - {cidade}"
                for id_cliente, nome_cliente, telefone_cliente, rua, bairro, cidade
                in self.clienteadd]
        else:
            print("Nenhum cliente encontrado no banco de dados.")  # Para depuração

        self.desconectar_bd()
    def atualizar_entry_cliente(self, event=None):
        # Obtém o valor selecionado na ComboBox
        cliente_selecionado = self.cliente_var.get()

        print(f"Cliente selecionado: {cliente_selecionado}")  # Adicionando para depuração

        if not cliente_selecionado:
            print("Nenhum cliente selecionado.")
            return

        # Extraímos o id_cliente da string
        try:
            codigo_cliente = cliente_selecionado.split(" - ")[0]  # Obtém o id_cliente
        except IndexError:
            print("Erro ao dividir a string do cliente.")
            return

        # Conecta ao banco para pegar os dados do cliente
        self.conecta_bd()

        # Busca os dados do cliente no banco de dados
        self.cursor.execute(
            "SELECT nome_cliente, telefone_cliente, rua, bairro, cidade FROM clientes WHERE id_cliente = ?",
            (codigo_cliente,))
        cliente = self.cursor.fetchone()

        if cliente:
            # Se o cliente for encontrado, atualiza os campos de entrada
            nome_cliente, telefone_cliente, rua, bairro, cidade = cliente

            # Atualiza os campos Entry com os dados do cliente
            self.nome_entry.delete(0, tkinter.END)
            self.nome_entry.insert(0, nome_cliente)

            self.telefone_entry.delete(0, tkinter.END)
            self.telefone_entry.insert(0, telefone_cliente)

            self.rua_entry.delete(0, tkinter.END)
            self.rua_entry.insert(0, rua)


            self.bairro_entry.delete(0, tkinter.END)
            self.bairro_entry.insert(0, bairro)

            self.cidade_entry.delete(0, tkinter.END)
            self.cidade_entry.insert(0, cidade)
        else:
            # Caso não encontre o cliente, exibe mensagem de erro
            print("Cliente não encontrado no banco de dados.")

        # Desconecta do banco de dados
        self.desconectar_bd()
    def calcular_total_liquido(self, total_bruto):
        try:
            desconto = float(self.desconto_entry.get())  # Lê o desconto inserido pelo usuário
        except ValueError:
            desconto = 0  # Caso o desconto não seja um número válido, assume 0

        # Calcula o total líquido com base no total bruto e no desconto
        total_liquido = total_bruto - (total_bruto * (desconto / 100))

        # Atualiza o campo de "Total Liquido"
        self.totalliquido_entry.delete(0, 'end')
        self.totalliquido_entry.insert(0, f"{total_liquido:.2f}")
    def atualizar_total_bruto(self):
        total_bruto = 0
        for item in self.tabela_produtos.get_children():
            # Corrigido para remover "R$" e vírgulas antes de converter para float
            valor_total_item = self.tabela_produtos.item(item, 'values')[4]

            # Remove o símbolo "R$" e vírgulas
            valor_total_item = valor_total_item.replace('R$', '').replace(' ', '')

            # Substitui a vírgula por ponto para utilizar como separador decimal
            valor_total_item = valor_total_item.replace(',', '.')

            # Agora, tenta converter o valor para float
            try:
                total_bruto += float(valor_total_item)  # Converte para float
            except ValueError:
                pass
                # Atualiza o campo de "Total Bruto"
        self.totalbruto_entry.delete(0, 'end')
        self.totalbruto_entry.insert(0, f"{total_bruto:.2f}")

        # Chama a função para calcular o total líquido
        self.calcular_total_liquido(total_bruto)
    def calcular_desconto(self):
        total_bruto = self.obter_total_bruto()  # Agora chamando a função corretamente
        try:
            desconto_percentual = float(self.desconto_entry.get().replace('R$', '').replace(' ', '').replace(',', '.'))
        except ValueError:
            desconto_percentual = 0  # Caso o desconto não seja válido, assume 0%

        desconto = (desconto_percentual / 100) * total_bruto
        total_liquido = total_bruto - desconto

        # Atualiza o campo Total Liquido
        self.totalliquido_entry.delete(0, 'end')  # Limpa o campo
        self.totalliquido_entry.insert(0, f'R$ {total_liquido:.2f}')  #
    def calcular_troco(self, event=None):
        # Aqui você pode pegar o valor total pago e subtrair o total líquido
        try:
            total_pago = float(self.totalpago_entry.get().replace('R$', '').replace(' ', '').replace(',', '.'))
        except ValueError:
            total_pago = 0

        try:
            total_liquido = float(self.totalliquido_entry.get().replace('R$', '').replace(' ', '').replace(',', '.'))
        except ValueError:
            total_liquido = 0

        if total_pago >= total_liquido:
            troco = total_pago - total_liquido
        else:
            troco = 0

        # Atualiza o campo de troco
        self.troco_entry.delete(0, 'end')  # Limpa o campo
        self.troco_entry.insert(0, f'R$ {troco:.2f}')  # Coloca o valor do troco no formato desejado
    def obter_total_bruto(self):
        total_bruto = 0
        # Itera sobre os itens na tabela e soma o valor total de cada item
        for item in self.tabela_produtos.get_children():
            valor_total = self.tabela_produtos.item(item, 'values')[4]  # O valor total está na quinta coluna
            try:
                total_bruto += float(valor_total.replace('R$', '').replace(' ', '').replace(',', '.'))
            except ValueError:
                pass  # Caso algum valor não seja válido, ignora
        return total_bruto

    def limpar_venda(self):
        # Limpar os campos de entrada
        self.nome_v_entry.delete(0, 'end')
        self.vendedor_combo.set('')
        self.produto_combo.set('')
        self.produto_entry.delete(0, 'end')
        self.qtde_entry.delete(0, 'end')
        self.V_U_entry.delete(0, 'end')
        self.v_total_entry.delete(0, 'end')

        self.cliente_combo.set('')
        self.nome_entry.delete(0, 'end')
        self.telefone_entry.delete(0, 'end')
        self.rua_entry.delete(0, 'end')
        self.bairro_entry.delete(0, 'end')
        self.cidade_entry.delete(0, 'end')

        self.totalbruto_entry.delete(0, 'end')
        self.desconto_entry.delete(0, 'end')
        self.totalliquido_entry.delete(0, 'end')
        self.totalpago_entry.delete(0, 'end')
        self.troco_entry.delete(0, 'end')

        # Limpar a tabela de produtos
        for item in self.tabela_produtos.get_children():
            self.tabela_produtos.delete(item)
    def exibir_pop_up_venda(self, cliente_id, cliente_nome, telefone, rua, bairro, cidade, total_bruto, total_liquido,
                            troco):
        # Formata a mensagem com as informações da venda
        mensagem = (f"Venda salva com sucesso!\n"
                    f"Cliente: {cliente_id} - {cliente_nome} - {telefone} - {rua} - {bairro} - {cidade}\n"
                    f"Total Bruto: R$ {total_bruto:.2f}\n"
                    f"Total Líquido: R$ {total_liquido:.2f}\n"
                    f"Troco: R$ {troco:.2f}")

        # Exibe o pop-up
        messagebox.showinfo("Venda Concluída", mensagem)

        self.limpar_venda()
    def salvar_venda(self):
        # Obter os dados necessários (exemplo)
        cliente_id = self.cliente_combo.get()  # ID do cliente
        cliente_nome = self.nome_entry.get()  # Nome do cliente
        telefone = self.telefone_entry.get()  # Telefone
        rua = self.rua_entry.get()  # Rua
        bairro = self.bairro_entry.get()  # Bairro
        cidade = self.cidade_entry.get()  # Cidade

        total_bruto = self.obter_total_bruto()  # Chama a função para obter o total bruto
        total_liquido = float(
            self.totalliquido_entry.get().replace('R$', '').replace(' ', '').replace(',', '.'))  # Obtém o total líquido
        troco = float(self.troco_entry.get().replace('R$', '').replace(' ', '').replace(',', '.'))  # Obtém o troco

        # Aqui você salva a venda no banco de dados ou onde precisar

        # Exibe o pop-up com os dados da venda
        self.exibir_pop_up_venda(cliente_id, cliente_nome, telefone, rua, bairro, cidade, total_bruto, total_liquido,
                                 troco)


class Application(funcs):
    def __init__(self):
        self.root = Tk()
        self.style = ttk.Style()
        self.style.theme_use('classic')
        self.root.title("SoftX")
        self.root.configure(background='#1e3743')
        self.root.geometry('788x588')
        self.root.resizable(True, True)
        self.root.minsize(width=500, height=400)
        self.tabelas()
        self.fornecedor_var = tkinter.StringVar()
        self.produto_var = tkinter.StringVar()
        self.vendedor_var = tkinter.StringVar()
        self.cliente_var = tkinter.StringVar()


        self.tela_login()
        self.root.mainloop()
    def tela_login(self):
        """Cria a tela de login."""
        # Remove todos os widgets da janela
        for widget in self.root.winfo_children():
            widget.destroy()
            self.style = ttk.Style()
            self.style.theme_use('classic')

        frame = Frame(self.root, bg="#dfe3ee")
        frame.place(relx=0.12, rely=0.13, relwidth=0.76, relheight=0.70)

        titulo = Label(self.root, text="Entre com Login", bg='#e6e6e6', fg='black', font=('verdana', 20, 'bold'))
        titulo.place(relx=0.5, rely=0.2, anchor="center")

        Label(frame, text='Usuário:', bg='#c0c0c0', fg='black', font=('verdana', 8, 'bold')).place(relx=0.15, rely=0.3)
        self.usuario_entry = Entry(frame)
        self.usuario_entry.place(relx=0.30, rely=0.3, relwidth=0.55)

        Label(frame, text='Senha:', bg='#c0c0c0', fg='black', font=('verdana', 8, 'bold')).place(relx=0.15, rely=0.4)
        self.senha_entry = Entry(frame, show='*')
        self.senha_entry.place(relx=0.30, rely=0.4, relwidth=0.55)

        self.erro_label = Label(frame, text="", bg="#c0c0c0", fg="red", font=('verdana', 10))
        self.erro_label.place(relx=0.25, rely=0.58)

        # Botão de login
        Button(frame, text="Login", bd=3, bg='#3e3eff', fg='white',
               font=('verdana', 10, 'bold'), cursor="hand2", command=self.validar_login2).place(relx=0.25, rely=0.65, relwidth=0.3, relheight=0.12)

        # Botão de sair
        Button(frame, text="Sair", bd=3, bg='#ff3e3e', fg='white',
               font=('verdana', 10, 'bold'), cursor="hand2", command=self.root.quit).place(relx=0.55, rely=0.65, relwidth=0.3, relheight=0.12)
    def validar_login1(self):
        self.conecta_bd()

        self.nome = self.usuario_entry.get().strip()  # Captura o nome digitado
        self.senha_digitada = self.senha_entry.get().strip()  # Captura a senha digitada

        # Verifica se os campos foram preenchidos
        if not self.nome or not self.senha_digitada:
            self.erro_label.config(text="Preencha todos os campos!")
            return

        # Faz a consulta no banco
        self.cursor.execute("SELECT senha FROM usuarios WHERE nome_usuario LIKE ?", (f"%{self.nome}%",))
        resultado = self.cursor.fetchone()  # Captura o resultado

        # Verifica se encontrou um usuário
        if resultado:
            senha_cadastrada = resultado[0]
            if self.senha_digitada == senha_cadastrada:
                messagebox.showinfo("Login", "Login realizado com sucesso!")
                self.tela_inicial()
            else:
                self.erro_label.config(text="Senha incorreta!")
        else:
            self.erro_label.config(text="Usuário não encontrado!")

        self.desconectar_bd()
    def validar_login2(self):
        """Valida o login e abre a tela inicial se correto."""
        usuario_digitado = self.usuario_entry.get()
        senha_digitada = self.senha_entry.get()

        usuario_correto = ""
        senha_correta = ""

        if usuario_digitado == usuario_correto and senha_digitada == senha_correta:
            self.tela_inicial()
        else:
            self.erro_label.config(text="Usuário ou senha incorretos!", fg="red")
    def tela_inicial(self):
        """Cria a tela inicial após o login correto."""
        for widget in self.root.winfo_children():
            widget.destroy()


        self.menus()

        Label(self.root, text="Bem-vindo ao SoftX!", bg='#1e3743', fg='white',
              font=('verdana', 20, 'bold')).pack(pady=20)
    def menus(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)

        cadastro = Menu(menubar)
        movimentacao = Menu(menubar)
        relatorio = Menu(menubar)
        configuracao = Menu(menubar)
        ajuda = Menu(menubar)

        menubar.add_cascade(label="Cadastro", menu=cadastro)
        menubar.add_cascade(label="Movimentação", menu=movimentacao)
        menubar.add_cascade(label="Relatorios", menu=relatorio)
        menubar.add_cascade(label="Configuração", menu=configuracao)
        menubar.add_cascade(label="Ajuda", menu=ajuda)
        menubar.add_command(label="Sair", command=self.tela_login)

        cadastro.add_command(label="Clientes",command=self.cadastroCli)
        cadastro.add_command(label="Fornecedores", command=self.cadastroforne)
        cadastro.add_command(label="Produtos", command=self.cadastroProdu)
        cadastro.add_command(label="Usuários", command=self.cadastroUsu)

        movimentacao.add_command(label="Vendas", command=self.tela_vendas)
        movimentacao.add_command(label="Compras")
        movimentacao.add_command(label="Estoques")
        movimentacao.add_command(label="Financeiro")

        relatorio.add_command(label="Clientes", command=self.consultaCli)
        relatorio.add_command(label="Vendas")
        relatorio.add_command(label="Produtos", command=self.consultaprodu)
        relatorio.add_command(label="Financeiro")
        relatorio.add_command(label="Fornecedor", command=self.consultaforne)

        configuracao.add_command(label="Usuários", command=self.consultaUsu)
        configuracao.add_command(label="Permissões")
        configuracao.add_command(label="Banco de Dados")

        # Ajuda (Sobre, Suporte, Atualizações)
        ajuda.add_command(label="Sobre")
        ajuda.add_command(label="Suporte")
        ajuda.add_command(label="Atualizações")
    def consultaCli(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.menus()
        """Cria a interface da consulta de clientes."""
        self.frame_1 = Frame(self.root, bd=4, bg='#dfe3ee',
                        highlightbackground='#759fe6', highlightthickness=3)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)

        self.frame_2 = Frame(self.root, bd=4, bg='#dfe3ee',
                        highlightbackground='#759fe6', highlightthickness=3)
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

        # Botão de limpar
        bt_limpar = Button(self.frame_1, text="Limpar", bd=3, bg='#107db2', fg='white',
                           font=('verdana', 8, 'bold'), command=self.limpar_tela)
        bt_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)

        # Botão de buscar
        bt_buscar = Button(self.frame_1, text="Buscar", bd=3, bg='#107db2', fg='white',
                           font=('verdana', 8, 'bold'), command=self.buscar_cliente)
        bt_buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)

        # Botão de alterar
        bt_alterar = Button(self.frame_1, text="Alterar", bd=3, bg='#107db2', fg='white',
                            font=('verdana', 8, 'bold'), command=self.alterar_cliente)
        bt_alterar.place(relx=0.4, rely=0.1, relwidth=0.1, relheight=0.15)

        # Botão de apagar
        bt_apagar = Button(self.frame_1, text="Apagar", bd=3, bg='#107db2', fg='white',
                           font=('verdana', 8, 'bold'), command=self.deleta_cliente)
        bt_apagar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)

        voltar_button = Button(self.frame_1, text="Voltar", bg="#f44336", fg="white", font=('verdana', 10),
                               command=self.tela_inicial)
        voltar_button.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)

        # Criando campos de entrada
        Label(self.frame_1, text='Código', bg='#dfe3ee', fg='#107db2', font=('verdana', 8, 'bold')).place(relx=0.05,
                                                                                                          rely=0.05)
        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx=0.05, rely=0.15, relwidth=0.07)

        Label(self.root, text='Nome:', bg='#e6e6e6', fg='black', font=('verdana', 8, 'bold')).place(relx=0.1, rely=0.2)
        self.nome_entry = Entry(self.root)
        self.nome_entry.place(relx=0.23, rely=0.2, relwidth=0.32)

        Label(self.root, text='Data de Nascimento:', bg='#e6e6e6', fg='black', font=('verdana', 8, 'bold')).place(
            relx=0.55, rely=0.2)
        self.datanascimento_entry = Entry(self.root)
        self.datanascimento_entry.place(relx=0.73, rely=0.2, relwidth=0.10)

        Label(self.root, text='CPF:', bg='#e6e6e6', fg='black', font=('verdana', 8, 'bold')).place(relx=0.1, rely=0.26)
        self.cpf_entry = Entry(self.root)
        self.cpf_entry.place(relx=0.23, rely=0.26, relwidth=0.2)

        Label(self.root, text='Telefone:', bg='#e6e6e6', fg='black', font=('verdana', 8, 'bold')).place(relx=0.45,
                                                                                                        rely=0.26)
        self.telefone_entry = Entry(self.root)
        self.telefone_entry.place(relx=0.60, rely=0.26, relwidth=0.23)

        Label(self.root, text='E-mail:', bg='#e6e6e6', fg='black', font=('verdana', 8, 'bold')).place(relx=0.1,
                                                                                                      rely=0.31)
        self.email_entry = Entry(self.root)
        self.email_entry.place(relx=0.23, rely=0.31, relwidth=0.60)

        # Criando os novos campos: Rua, CEP, Bairro, Cidade
        Label(self.root, text='Rua:', bg='#e6e6e6', fg='black', font=('verdana', 8, 'bold')).place(relx=0.1, rely=0.35)
        self.rua_entry = Entry(self.root)
        self.rua_entry.place(relx=0.23, rely=0.35, relwidth=0.60)

        Label(self.root, text='CEP:', bg='#e6e6e6', fg='black', font=('verdana', 8, 'bold')).place(relx=0.1, rely=0.39)
        self.cep_entry = Entry(self.root)
        self.cep_entry.place(relx=0.23, rely=0.39, relwidth=0.2)

        Label(self.root, text='Bairro:', bg='#e6e6e6', fg='black', font=('verdana', 8, 'bold')).place(relx=0.45,
                                                                                                      rely=0.39)
        self.bairro_entry = Entry(self.root)
        self.bairro_entry.place(relx=0.6, rely=0.39, relwidth=0.23)

        Label(self.root, text='Cidade:', bg='#e6e6e6', fg='black', font=('verdana', 8, 'bold')).place(relx=0.1,
                                                                                                      rely=0.44)
        self.cidade_entry = Entry(self.root)
        self.cidade_entry.place(relx=0.23, rely=0.44, relwidth=0.60)

        # Criando tabela
        self.listacli = ttk.Treeview(self.frame_2, height=3,
                                     columns=('col1', 'col2', 'col3', 'col4', 'col5', 'col6', 'col7', 'col8', 'col9','col10'))
        self.listacli.heading('#1', text="Cód")
        self.listacli.heading('#2', text="Nome")
        self.listacli.heading('#3', text="Nascimento")
        self.listacli.heading('#4', text="CPF")
        self.listacli.heading('#5', text="Telefone")
        self.listacli.heading('#6', text="Email")
        self.listacli.heading('#7', text="Rua")
        self.listacli.heading('#8', text="CEP")
        self.listacli.heading('#9', text="Bairro")
        self.listacli.heading('#10', text="Cidade")

        self.listacli.column('#0', width=3)
        self.listacli.column('#1', width=30)
        self.listacli.column('#2', width=110)
        self.listacli.column('#3', width=40)
        self.listacli.column('#4', width=40)
        self.listacli.column('#5', width=80)
        self.listacli.column('#6', width=80)
        self.listacli.column('#7', width=80)
        self.listacli.column('#8', width=40)
        self.listacli.column('#9', width=70)
        self.listacli.column('#10', width=70)
        self.listacli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        self.select_lista()

        # Scrollbar
        scroll = Scrollbar(self.frame_2, orient='vertical', command=self.listacli.yview)
        self.listacli.configure(yscrollcommand=scroll.set)
        scroll.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)
        self.listacli.bind("<Double-1>", self.onDoubleClick)
    def cadastroCli(self):

        for widget in self.root.winfo_children():
            widget.destroy()

        self.menus()

        frame = Frame(self.root, bg="#dfe3ee")
        frame.place(relx=0.06, rely=0.06, relwidth=0.90, relheight=0.90)

        # Título centralizado
        Label(frame, text="Cadastro de Clientes!", bg='#1e3743', fg='white',
              font=('verdana', 20, 'bold')).pack(pady=20)

        # Nome
        Label(frame, text='Nome:', bg='#e6e6e6', fg='black', font=('verdana', 8, 'bold')).place(relx=0.1, rely=0.2)
        self.nome_entry = Entry(frame)
        self.nome_entry.place(relx=0.18, rely=0.2, relwidth=0.4, relheight=0.05)

        # Data de Nascimento
        Label(frame, text='Nascimento:', bg='#e6e6e6', fg='black', font=('verdana', 8, 'bold')).place(relx=0.60,
                                                                                                              rely=0.2)
        self.datanascimento_entry = Entry(frame)
        self.datanascimento_entry.place(relx=0.73, rely=0.2, relwidth=0.20, relheight=0.05)

        # CPF
        Label(frame, text='CPF:', bg='#e6e6e6', fg='black', font=('verdana', 8, 'bold')).place(relx=0.1, rely=0.3)
        self.cpf_entry = Entry(frame)
        self.cpf_entry.place(relx=0.18, rely=0.3, relwidth=0.30, relheight=0.05)

        # Telefone ao lado do CPF
        Label(frame, text='Telefone:', bg='#e6e6e6', fg='black', font=('verdana', 8, 'bold')).place(relx=0.5, rely=0.3)
        self.telefone_entry = Entry(frame)
        self.telefone_entry.place(relx=0.61, rely=0.3, relwidth=0.32, relheight=0.05)

        # E-mail
        Label(frame, text='E-mail:', bg='#e6e6e6', fg='black', font=('verdana', 8, 'bold')).place(relx=0.1, rely=0.4)
        self.email_entry = Entry(frame)
        self.email_entry.place(relx=0.18, rely=0.4, relwidth=0.75, relheight=0.05)

        # Rua
        Label(frame, text='Rua:', bg='#e6e6e6', fg='black', font=('verdana', 8, 'bold')).place(relx=0.1, rely=0.5)
        self.rua_entry = Entry(frame)
        self.rua_entry.place(relx=0.18, rely=0.5, relwidth=0.75, relheight=0.05)

        # CEP
        Label(frame, text='CEP:', bg='#e6e6e6', fg='black', font=('verdana', 8, 'bold')).place(relx=0.1, rely=0.6)
        self.cep_entry = Entry(frame)
        self.cep_entry.place(relx=0.18, rely=0.6, relwidth=0.25, relheight=0.05)

        # Bairro
        Label(frame, text='Bairro:', bg='#e6e6e6', fg='black', font=('verdana', 8, 'bold')).place(relx=0.45, rely=0.6)
        self.bairro_entry = Entry(frame)
        self.bairro_entry.place(relx=0.53, rely=0.6, relwidth=0.40, relheight=0.05)

        # Cidade
        Label(frame, text='Cidade:', bg='#e6e6e6', fg='black', font=('verdana', 8, 'bold')).place(relx=0.1, rely=0.7)
        self.cidade_entry = Entry(frame)
        self.cidade_entry.place(relx=0.18, rely=0.7, relwidth=0.75, relheight=0.05)

        # Botões (sem command)
        cadastrar_button = Button(frame, text="Cadastrar", bg="#4CAF50", fg="white", font=('verdana', 10), command=self.add_cliente)
        cadastrar_button.place(relx=0.20, rely=0.8, relwidth=0.20, relheight=0.08)

        voltar_button = Button(frame, text="Voltar", bg="#f44336", fg="white", font=('verdana', 10), command=self.tela_inicial)
        voltar_button.place(relx=0.50, rely=0.8, relwidth=0.20, relheight=0.08)
    def cadastroUsu(self):

        for widget in self.root.winfo_children():
            widget.destroy()

        self.menus()


        frame = Frame(self.root, bg="#dfe3ee")
        frame.place(relx=0.06, rely=0.06, relwidth=0.90, relheight=0.90)

        # Título centralizado
        Label(frame, text="Cadastro de Usuários!", bg='#1e3743', fg='white',
              font=('verdana', 20, 'bold')).pack(pady=20)

        # Nome
        Label(frame, text='Nome:', bg='#e6e6e6', fg='black', font=('verdana', 8, 'bold')).place(relx=0.1, rely=0.2)
        self.nome_entry = Entry(frame)
        self.nome_entry.place(relx=0.18, rely=0.2, relwidth=0.4, relheight=0.05)

        # Data de Nascimento
        Label(frame, text='Nascimento:', bg='#e6e6e6', fg='black', font=('verdana', 8, 'bold')).place(relx=0.60,
                                                                                                      rely=0.2)
        self.datanascimento_entry = Entry(frame)
        self.datanascimento_entry.place(relx=0.73, rely=0.2, relwidth=0.20, relheight=0.05)

        # CPF
        Label(frame, text='CPF:', bg='#e6e6e6', fg='black', font=('verdana', 8, 'bold')).place(relx=0.1, rely=0.28)
        self.cpf_entry = Entry(frame)
        self.cpf_entry.place(relx=0.18, rely=0.28, relwidth=0.30, relheight=0.05)

        # Telefone ao lado do CPF
        Label(frame, text='Telefone:', bg='#e6e6e6', fg='black', font=('verdana', 8, 'bold')).place(relx=0.5,
                                                                                                    rely=0.28)
        self.telefone_entry = Entry(frame)
        self.telefone_entry.place(relx=0.61, rely=0.28, relwidth=0.32, relheight=0.05)

        # E-mail
        Label(frame, text='E-mail:', bg='#e6e6e6', fg='black', font=('verdana', 8, 'bold')).place(relx=0.1,
                                                                                                  rely=0.36)
        self.email_entry = Entry(frame)
        self.email_entry.place(relx=0.18, rely=0.36, relwidth=0.75, relheight=0.05)

        # Rua
        Label(frame, text='Rua:', bg='#e6e6e6', fg='black', font=('verdana', 8, 'bold')).place(relx=0.1, rely=0.44)
        self.rua_entry = Entry(frame)
        self.rua_entry.place(relx=0.18, rely=0.44, relwidth=0.75, relheight=0.05)

        # CEP
        Label(frame, text='CEP:', bg='#e6e6e6', fg='black', font=('verdana', 8, 'bold')).place(relx=0.1, rely=0.52)
        self.cep_entry = Entry(frame)
        self.cep_entry.place(relx=0.18, rely=0.52, relwidth=0.25, relheight=0.05)

        # Bairro
        Label(frame, text='Bairro:', bg='#e6e6e6', fg='black', font=('verdana', 8, 'bold')).place(relx=0.45,
                                                                                                  rely=0.52)
        self.bairro_entry = Entry(frame)
        self.bairro_entry.place(relx=0.53, rely=0.52, relwidth=0.40, relheight=0.05)

        # Cidade
        Label(frame, text='Cidade:', bg='#e6e6e6', fg='black', font=('verdana', 8, 'bold')).place(relx=0.1,
                                                                                                  rely=0.6)
        self.cidade_entry = Entry(frame)
        self.cidade_entry.place(relx=0.18, rely=0.6, relwidth=0.75, relheight=0.05)

        # senha
        Label(frame, text='Senha:', bg='#e6e6e6', fg='black', font=('verdana', 8, 'bold')).place(relx=0.1,
                                                                                                  rely=0.68)
        self.senha_entry = Entry(frame)
        self.senha_entry.place(relx=0.18, rely=0.68, relwidth=0.38, relheight=0.05)

        # tipo
        Label(frame, text='Tipo:', bg='#e6e6e6', fg='black', font=('verdana', 8, 'bold')).place(relx=0.60,
                                                                                                 rely=0.68)
        self.tipo_combo = ttk.Combobox(frame, values=["admin", "vendedor", "financeiro", "estoque"])
        self.tipo_combo.place(relx=0.66, rely=0.68, relwidth=0.27, relheight=0.05)

        # Botões (sem command)
        cadastrar_button = Button(frame, text="Cadastrar", bg="#4CAF50", fg="white", font=('verdana', 10), command=self.add_usuario)
        cadastrar_button.place(relx=0.20, rely=0.8, relwidth=0.20, relheight=0.08)

        voltar_button = Button(frame, text="Voltar", bg="#f44336", fg="white", font=('verdana', 10),
                               command=self.tela_inicial)
        voltar_button.place(relx=0.50, rely=0.8, relwidth=0.20, relheight=0.08)
    def consultaUsu(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.menus()
        """Cria a interface da consulta de clientes."""
        self.frame_1 = Frame(self.root, bd=4, bg='#dfe3ee',
                        highlightbackground='#759fe6', highlightthickness=3)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)

        self.frame_2 = Frame(self.root, bd=4, bg='#dfe3ee',
                        highlightbackground='#759fe6', highlightthickness=3)
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

        # Botão de limpar
        bt_limpar = Button(self.frame_1, text="Limpar", bd=3, bg='#107db2', fg='white',
                           font=('verdana', 8, 'bold'),command=self.limpar_telacon_u)
        bt_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)

        # Botão de buscar
        bt_buscar = Button(self.frame_1, text="Buscar", bd=3, bg='#107db2', fg='white',
                           font=('verdana', 8, 'bold'), command=self.buscar_usuario)
        bt_buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)

        # Botão de alterar
        bt_alterar = Button(self.frame_1, text="Alterar", bd=3, bg='#107db2', fg='white',
                            font=('verdana', 8, 'bold'), command=self.alterar_usuario)
        bt_alterar.place(relx=0.4, rely=0.1, relwidth=0.1, relheight=0.15)

        # Botão de apagar
        bt_apagar = Button(self.frame_1, text="Apagar", bd=3, bg='#107db2', fg='white',
                           font=('verdana', 8, 'bold'), command=self.deleta_usuario)
        bt_apagar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)

        voltar_button = Button(self.frame_1, text="Voltar", bg="#f44336", fg="white", font=('verdana', 10),
                               command=self.tela_inicial)
        voltar_button.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)

        # Criando campos de entrada
        Label(self.frame_1, text='Código', bg='#dfe3ee', fg='#107db2', font=('verdana', 8, 'bold')).place(relx=0.05,
                                                                                                          rely=0.05)
        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx=0.05, rely=0.15, relwidth=0.07)

        Label(self.root, text='Nome:', bg='#e6e6e6', fg='black', font=('verdana', 8, 'bold')).place(relx=0.1, rely=0.2)
        self.nome_entry = Entry(self.root)
        self.nome_entry.place(relx=0.165, rely=0.2, relwidth=0.42)

        Label(self.root, text='Data de Nascimento:', bg='#e6e6e6', fg='black', font=('verdana', 8, 'bold')).place(
            relx=0.57, rely=0.2)
        self.datanascimento_entry = DateEntry(self.root, width=12, background='darkblue',
                               foreground='white', borderwidth=2, date_pattern='dd/MM/yyyy')
        self.datanascimento_entry.place(relx=0.75, rely=0.2, relwidth=0.15)

        Label(self.root, text='CPF:', bg='#e6e6e6', fg='black', font=('verdana', 8, 'bold')).place(relx=0.1, rely=0.26)
        self.cpf_entry = Entry(self.root)
        self.cpf_entry.place(relx=0.165, rely=0.26, relwidth=0.2)

        Label(self.root, text='Telefone:', bg='#e6e6e6', fg='black', font=('verdana', 8, 'bold')).place(relx=0.38,
                                                                                                        rely=0.26)
        self.telefone_entry = Entry(self.root)
        self.telefone_entry.place(relx=0.475, rely=0.26, relwidth=0.23)

        Label(self.root, text='E-mail:', bg='#e6e6e6', fg='black', font=('verdana', 8, 'bold')).place(relx=0.1,
                                                                                                      rely=0.31)
        self.email_entry = Entry(self.root)
        self.email_entry.place(relx=0.165, rely=0.31, relwidth=0.60)

        # Criando os novos campos: Rua, CEP, Bairro, Cidade
        Label(self.root, text='Rua:', bg='#e6e6e6', fg='black', font=('verdana', 8, 'bold')).place(relx=0.1, rely=0.35)
        self.rua_entry = Entry(self.root)
        self.rua_entry.place(relx=0.165, rely=0.35, relwidth=0.37)

        Label(self.root, text='CEP:', bg='#e6e6e6', fg='black', font=('verdana', 8, 'bold')).place(relx=0.6, rely=0.35)
        self.cep_entry = Entry(self.root)
        self.cep_entry.place(relx=0.65, rely=0.35, relwidth=0.2)

        Label(self.root, text='Bairro:', bg='#e6e6e6', fg='black', font=('verdana', 8, 'bold')).place(relx=0.1,
                                                                                                      rely=0.39)
        self.bairro_entry = Entry(self.root)
        self.bairro_entry.place(relx=0.165, rely=0.39, relwidth=0.23)

        Label(self.root, text='Cidade:', bg='#e6e6e6', fg='black', font=('verdana', 8, 'bold')).place(relx=0.40,
                                                                                                      rely=0.39)
        self.cidade_entry = Entry(self.root)
        self.cidade_entry.place(relx=0.47, rely=0.39, relwidth=0.30)

        Label(self.root, text='Senha:', bg='#e6e6e6', fg='black', font=('verdana', 8, 'bold')).place(relx=0.1,
                                                                                                      rely=0.44)
        self.senha_entry = Entry(self.root)
        self.senha_entry.place(relx=0.165, rely=0.44, relwidth=0.23)

        Label(self.root, text='Tipo:', bg='#e6e6e6', fg='black', font=('verdana', 8, 'bold')).place(relx=0.4,
                                                                                                rely=0.44)
        self.tipo_combo = ttk.Combobox(self.root, values=["admin", "vendedor", "financeiro", "estoque"])
        self.tipo_combo.place(relx=0.47, rely=0.44, relwidth=0.10)

        Label(self.root, text='permissao:', bg='#e6e6e6', fg='black', font=('verdana', 8, 'bold')).place(relx=0.585,
                                                                                                rely=0.44)
        self.permissao_combo = ttk.Combobox(self.root, values=[""])
        self.permissao_combo.place(relx=0.7, rely=0.44, relwidth=0.10)

        # Criando tabela
        self.listausu = ttk.Treeview(self.frame_2, height=3,
                                     columns=('col1', 'col2', 'col3', 'col4', 'col5', 'col6', 'col7', 'col8', 'col9','col10','col11','col12'))
        self.listausu.heading('#1', text="Cód")
        self.listausu.heading('#2', text="Nome")
        self.listausu.heading('#3', text="Nascimento")
        self.listausu.heading('#4', text="CPF")
        self.listausu.heading('#5', text="Telefone")
        self.listausu.heading('#6', text="Email")
        self.listausu.heading('#7', text="Rua")
        self.listausu.heading('#8', text="CEP")
        self.listausu.heading('#9', text="Bairro")
        self.listausu.heading('#10', text="Cidade")
        self.listausu.heading('#11', text="Senha")
        self.listausu.heading('#12', text="Tipo")

        self.listausu.column('#0', width=3)
        self.listausu.column('#1', width=30)
        self.listausu.column('#2', width=110)
        self.listausu.column('#3', width=40)
        self.listausu.column('#4', width=40)
        self.listausu.column('#5', width=80)
        self.listausu.column('#6', width=80)
        self.listausu.column('#7', width=80)
        self.listausu.column('#8', width=40)
        self.listausu.column('#9', width=70)
        self.listausu.column('#10', width=70)
        self.listausu.column('#11', width=40)
        self.listausu.column('#12', width=40)
        self.listausu.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        self.select_listausu()

        # Scrollbar
        scroll = Scrollbar(self.frame_2, orient='vertical', command=self.listausu.yview)
        self.listausu.configure(yscrollcommand=scroll.set)
        scroll.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)
        self.listausu.bind("<Double-1>", self.onDoubleClickUsu)
    def cadastroforne(self):

        for widget in self.root.winfo_children():
            widget.destroy()

        self.menus()

        frame = Frame(self.root, bg="#dfe3ee")
        frame.place(relx=0.06, rely=0.06, relwidth=0.90, relheight=0.90)

        # Título centralizado
        Label(frame, text="Cadastro de Fornecedores!!", bg='#1e3743', fg='white',
              font=('verdana', 20, 'bold')).pack(pady=20)

        # Nome
        Label(frame, text='Nome:', bg='#e6e6e6', fg='black', font=('verdana', 8, 'bold')).place(relx=0.1, rely=0.2)
        self.nome_entry = Entry(frame)
        self.nome_entry.place(relx=0.18, rely=0.2, relwidth=0.75, relheight=0.05)

        # CNPJ
        Label(frame, text='CNPJ:', bg='#e6e6e6', fg='black', font=('verdana', 8, 'bold')).place(relx=0.1, rely=0.28)
        self.cnpj_entry = Entry(frame)
        self.cnpj_entry.place(relx=0.18, rely=0.28, relwidth=0.30, relheight=0.05)

        # Telefone ao lado do CPF
        Label(frame, text='Telefone:', bg='#e6e6e6', fg='black', font=('verdana', 8, 'bold')).place(relx=0.5,
                                                                                                    rely=0.28)
        self.telefone_entry = Entry(frame)
        self.telefone_entry.place(relx=0.61, rely=0.28, relwidth=0.32, relheight=0.05)

        # E-mail
        Label(frame, text='E-mail:', bg='#e6e6e6', fg='black', font=('verdana', 8, 'bold')).place(relx=0.1,
                                                                                                  rely=0.36)
        self.email_entry = Entry(frame)
        self.email_entry.place(relx=0.18, rely=0.36, relwidth=0.75, relheight=0.05)

        # Rua
        Label(frame, text='Rua:', bg='#e6e6e6', fg='black', font=('verdana', 8, 'bold')).place(relx=0.1, rely=0.44)
        self.rua_entry = Entry(frame)
        self.rua_entry.place(relx=0.18, rely=0.44, relwidth=0.75, relheight=0.05)

        # CEP
        Label(frame, text='CEP:', bg='#e6e6e6', fg='black', font=('verdana', 8, 'bold')).place(relx=0.1, rely=0.52)
        self.cep_entry = Entry(frame)
        self.cep_entry.place(relx=0.18, rely=0.52, relwidth=0.25, relheight=0.05)

        # Bairro
        Label(frame, text='Bairro:', bg='#e6e6e6', fg='black', font=('verdana', 8, 'bold')).place(relx=0.45,
                                                                                                  rely=0.52)
        self.bairro_entry = Entry(frame)
        self.bairro_entry.place(relx=0.53, rely=0.52, relwidth=0.40, relheight=0.05)

        # Cidade
        Label(frame, text='Cidade:', bg='#e6e6e6', fg='black', font=('verdana', 8, 'bold')).place(relx=0.1,
                                                                                                  rely=0.6)
        self.cidade_entry = Entry(frame)
        self.cidade_entry.place(relx=0.18, rely=0.6, relwidth=0.75, relheight=0.05)

        # Botões (sem command)
        cadastrar_button = Button(frame, text="Cadastrar", bg="#4CAF50", fg="white", font=('verdana', 10), command=self.add_fornecedor)
        cadastrar_button.place(relx=0.20, rely=0.8, relwidth=0.20, relheight=0.08)

        voltar_button = Button(frame, text="Voltar", bg="#f44336", fg="white", font=('verdana', 10),
                               command=self.tela_inicial)
        voltar_button.place(relx=0.50, rely=0.8, relwidth=0.20, relheight=0.08)
    def consultaforne(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.menus()
        """Cria a interface da consulta de fornecedores."""
        self.frame_1 = Frame(self.root, bd=4, bg='#dfe3ee',
                             highlightbackground='#759fe6', highlightthickness=3)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)

        self.frame_2 = Frame(self.root, bd=4, bg='#dfe3ee',
                             highlightbackground='#759fe6', highlightthickness=3)
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

        # Botão de limpar
        bt_limpar = Button(self.frame_1, text="Limpar", bd=3, bg='#107db2', fg='white',
                           font=('verdana', 8, 'bold'), command=self.limpar_telaconforne)
        bt_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)

        # Botão de buscar
        bt_buscar = Button(self.frame_1, text="Buscar", bd=3, bg='#107db2', fg='white',
                           font=('verdana', 8, 'bold'), command=self.buscar_fornecedor)
        bt_buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)

        # Botão de alterar
        bt_alterar = Button(self.frame_1, text="Alterar", bd=3, bg='#107db2', fg='white',
                            font=('verdana', 8, 'bold'), command=self.alterar_fornecedor)
        bt_alterar.place(relx=0.4, rely=0.1, relwidth=0.1, relheight=0.15)

        # Botão de apagar
        bt_apagar = Button(self.frame_1, text="Apagar", bd=3, bg='#107db2', fg='white',
                           font=('verdana', 8, 'bold'), command=self.deleta_fornecedor)
        bt_apagar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)

        voltar_button = Button(self.frame_1, text="Voltar", bg="#f44336", fg="white", font=('verdana', 10),
                               command=self.tela_inicial)
        voltar_button.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)

        # Criando campos de entrada
        Label(self.frame_1, text='Código', bg='#dfe3ee', fg='#107db2', font=('verdana', 8, 'bold')).place(relx=0.05,
                                                                                                          rely=0.05)
        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx=0.05, rely=0.15, relwidth=0.07)

        Label(self.root, text='Nome:', bg='#e6e6e6', fg='black', font=('verdana', 8, 'bold')).place(relx=0.1, rely=0.2)
        self.nome_entry = Entry(self.root)
        self.nome_entry.place(relx=0.165, rely=0.2, relwidth=0.42)


        Label(self.root, text='CNPJ:', bg='#e6e6e6', fg='black', font=('verdana', 8, 'bold')).place(relx=0.1, rely=0.26)
        self.cnpj_entry = Entry(self.root)
        self.cnpj_entry.place(relx=0.165, rely=0.26, relwidth=0.2)

        Label(self.root, text='Telefone:', bg='#e6e6e6', fg='black', font=('verdana', 8, 'bold')).place(relx=0.38,
                                                                                                        rely=0.26)
        self.telefone_entry = Entry(self.root)
        self.telefone_entry.place(relx=0.475, rely=0.26, relwidth=0.23)

        Label(self.root, text='E-mail:', bg='#e6e6e6', fg='black', font=('verdana', 8, 'bold')).place(relx=0.1,
                                                                                                      rely=0.31)
        self.email_entry = Entry(self.root)
        self.email_entry.place(relx=0.165, rely=0.31, relwidth=0.60)

        # Criando os novos campos: Rua, CEP, Bairro, Cidade
        Label(self.root, text='Rua:', bg='#e6e6e6', fg='black', font=('verdana', 8, 'bold')).place(relx=0.1, rely=0.35)
        self.rua_entry = Entry(self.root)
        self.rua_entry.place(relx=0.165, rely=0.35, relwidth=0.37)

        Label(self.root, text='CEP:', bg='#e6e6e6', fg='black', font=('verdana', 8, 'bold')).place(relx=0.6, rely=0.35)
        self.cep_entry = Entry(self.root)
        self.cep_entry.place(relx=0.65, rely=0.35, relwidth=0.2)

        Label(self.root, text='Bairro:', bg='#e6e6e6', fg='black', font=('verdana', 8, 'bold')).place(relx=0.1,
                                                                                                      rely=0.39)
        self.bairro_entry = Entry(self.root)
        self.bairro_entry.place(relx=0.165, rely=0.39, relwidth=0.23)

        Label(self.root, text='Cidade:', bg='#e6e6e6', fg='black', font=('verdana', 8, 'bold')).place(relx=0.40,
                                                                                                      rely=0.39)
        self.cidade_entry = Entry(self.root)
        self.cidade_entry.place(relx=0.47, rely=0.39, relwidth=0.30)

        # Criando tabela
        self.listaforne = ttk.Treeview(self.frame_2, height=3,
                                     columns=(
                                     'col1', 'col2', 'col3', 'col4', 'col5', 'col6', 'col7', 'col8', 'col9'
                                      ))
        self.listaforne.heading('#1', text="Cód")
        self.listaforne.heading('#2', text="Nome")
        self.listaforne.heading('#3', text="CNPJ")
        self.listaforne.heading('#4', text="Email")
        self.listaforne.heading('#5', text="Telefone")
        self.listaforne.heading('#6', text="Rua")
        self.listaforne.heading('#7', text="CEP")
        self.listaforne.heading('#8', text="Bairro")
        self.listaforne.heading('#9', text="Cidade")


        self.listaforne.column('#0', width=3)
        self.listaforne.column('#1', width=30)
        self.listaforne.column('#2', width=110)
        self.listaforne.column('#3', width=40)
        self.listaforne.column('#4', width=40)
        self.listaforne.column('#5', width=80)
        self.listaforne.column('#6', width=80)
        self.listaforne.column('#7', width=80)
        self.listaforne.column('#8', width=40)
        self.listaforne.column('#9', width=70)

        self.listaforne.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        self.select_listaforne()

        # Scrollbar
        scroll = Scrollbar(self.frame_2, orient='vertical', command=self.listaforne.yview)
        self.listaforne.configure(yscrollcommand=scroll.set)
        scroll.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)
        self.listaforne.bind("<Double-1>", self.onDoubleClickforne)
    def cadastroProdu(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.menus()
        frame = Frame(self.root, bg="#dfe3ee")
        frame.place(relx=0.06, rely=0.06, relwidth=0.90, relheight=0.90)

        # Título
        Label(frame, text="Cadastro de Produtos!", bg='#1e3743', fg='white',
              font=('verdana', 20, 'bold')).pack(pady=20)

        # Nome
        Label(frame, text='Nome:', bg='#e6e6e6', fg='black', font=('verdana', 8, 'bold')).place(relx=0.1, rely=0.2)
        self.nome_entry = Entry(frame)
        self.nome_entry.place(relx=0.18, rely=0.2, relwidth=0.75, relheight=0.05)

        # Preço de Venda
        Label(frame, text='Preço de Venda:', bg='#e6e6e6', fg='black', font=('verdana', 8, 'bold')).place(relx=0.1,
                                                                                                          rely=0.3)
        self.v_venda_entry = Entry(frame)
        self.v_venda_entry.place(relx=0.265, rely=0.3, relwidth=0.20, relheight=0.05)

        # Preço de Compra
        Label(frame, text='Preço de Compra:', bg='#e6e6e6', fg='black', font=('verdana', 8, 'bold')).place(relx=0.49,
                                                                                                           rely=0.3)
        self.v_compra_entry = Entry(frame)
        self.v_compra_entry.place(relx=0.665, rely=0.3, relwidth=0.25, relheight=0.05)

        # Fornecedor (ComboBox)
        Label(frame, text='Fornecedor:', bg='#e6e6e6', fg='black', font=('verdana', 8, 'bold')).place(relx=0.1,
                                                                                                      rely=0.40)

        self.fornecedor_combo = ttk.Combobox(frame, textvariable=self.fornecedor_var)
        self.fornecedor_combo.place(relx=0.23, rely=0.40, relwidth=0.70, relheight=0.05)

        # Descrição
        Label(frame, text='Descrição:', bg='#e6e6e6', fg='black', font=('verdana', 8, 'bold')).place(relx=0.1,
                                                                                                     rely=0.58)
        self.descrição_entry = Entry(frame)
        self.descrição_entry.place(relx=0.23, rely=0.50, relwidth=0.70, relheight=0.25)

        # Botões
        cadastrar_button = Button(frame, text="Cadastrar", bg="#4CAF50", fg="white", font=('verdana', 10),
                                  command=self.add_produto)
        cadastrar_button.place(relx=0.20, rely=0.8, relwidth=0.20, relheight=0.08)

        voltar_button = Button(frame, text="Voltar", bg="#f44336", fg="white", font=('verdana', 10),
                               command=self.tela_inicial)
        voltar_button.place(relx=0.50, rely=0.8, relwidth=0.20, relheight=0.08)

        # Carregar fornecedores na combobox
        self.comboforne()
    def consultaprodu(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.menus()
        """Cria a interface da consulta de produtos."""
        self.frame_1 = Frame(self.root, bd=4, bg='#dfe3ee',
                             highlightbackground='#759fe6', highlightthickness=3)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)

        self.frame_2 = Frame(self.root, bd=4, bg='#dfe3ee',
                             highlightbackground='#759fe6', highlightthickness=3)
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

        # Botão de limpar
        bt_limpar = Button(self.frame_1, text="Limpar", bd=3, bg='#107db2', fg='white',
                           font=('verdana', 8, 'bold'), command=self.limpar_telacadpro)
        bt_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)

        # Botão de buscar
        bt_buscar = Button(self.frame_1, text="Buscar", bd=3, bg='#107db2', fg='white',
                           font=('verdana', 8, 'bold'), command=self.buscar_produto)
        bt_buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)

        # Botão de alterar
        bt_alterar = Button(self.frame_1, text="Alterar", bd=3, bg='#107db2', fg='white',
                            font=('verdana', 8, 'bold'), command=self.alterar_produto)
        bt_alterar.place(relx=0.4, rely=0.1, relwidth=0.1, relheight=0.15)

        # Botão de apagar
        bt_apagar = Button(self.frame_1, text="Apagar", bd=3, bg='#107db2', fg='white',
                           font=('verdana', 8, 'bold'), command=self.deleta_produto)
        bt_apagar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)

        voltar_button = Button(self.frame_1, text="Voltar", bg="#f44336", fg="white", font=('verdana', 10),
                               command=self.tela_inicial)
        voltar_button.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)

        # Criando campos de entrada
        Label(self.frame_1, text='Código', bg='#dfe3ee', fg='#107db2', font=('verdana', 8, 'bold')).place(relx=0.05,
                                                                                                          rely=0.05)
        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx=0.05, rely=0.15, relwidth=0.07)

        # Nome
        Label(self.frame_1, text='Nome:', bg='#e6e6e6', fg='black', font=('verdana', 8, 'bold')).place(relx=0.1, rely=0.30)
        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx=0.18, rely=0.30, relwidth=0.7,relheight=0.1)

        # Preço de Venda
        Label(self.frame_1, text='Preço de Venda:', bg='#e6e6e6', fg='black', font=('verdana', 8, 'bold')).place(relx=0.1,
                                                                                                          rely=0.43)
        self.v_venda_entry = Entry(self.frame_1)
        self.v_venda_entry.place(relx=0.265, rely=0.43, relwidth=0.20, relheight=0.1)

        # Preço de Compra
        Label(self.frame_1, text='Preço de Compra:', bg='#e6e6e6', fg='black', font=('verdana', 8, 'bold')).place(relx=0.49,
                                                                                                           rely=0.43)
        self.v_compra_entry = Entry(self.frame_1)
        self.v_compra_entry.place(relx=0.665, rely=0.43, relwidth=0.25, relheight=0.1)

        # Fornecedor (ComboBox)
        Label(self.frame_1, text='Fornecedor:', bg='#e6e6e6', fg='black', font=('verdana', 8, 'bold')).place(relx=0.1,
                                                                                                      rely=0.57)

        self.fornecedor_combo = ttk.Combobox(self.frame_1, textvariable=self.fornecedor_var)
        self.fornecedor_combo.place(relx=0.23, rely=0.57, relwidth=0.70, relheight=0.1)

        self.comboforne()

        # Descrição
        Label(self.frame_1, text='Descrição:', bg='#e6e6e6', fg='black', font=('verdana', 8, 'bold')).place(relx=0.1,
                                                                                                     rely=0.78)
        self.descrição_entry = Entry(self.frame_1)
        self.descrição_entry.place(relx=0.23, rely=0.70, relwidth=0.70, relheight=0.25)

        # Criando tabela
        self.listaprod = ttk.Treeview(self.frame_2, height=3,
                                     columns=(
                                     'col1', 'col2', 'col3', 'col4', 'col5', 'col6'
                                      ))
        self.listaprod.heading('#1', text="Cód")
        self.listaprod.heading('#2', text="Nome")
        self.listaprod.heading('#3', text="Preço_venda")
        self.listaprod.heading('#4', text="Preço_compra")
        self.listaprod.heading('#5', text="Fornecedor")
        self.listaprod.heading('#6', text="Descrição")



        self.listaprod.column('#0', width=3)
        self.listaprod.column('#1', width=30)
        self.listaprod.column('#2', width=110)
        self.listaprod.column('#3', width=40)
        self.listaprod.column('#4', width=40)
        self.listaprod.column('#5', width=80)
        self.listaprod.column('#6', width=80)


        self.listaprod.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        self.select_listaprod()

        # Scrollbar
        scroll = Scrollbar(self.frame_2, orient='vertical', command=self.listaprod.yview)
        self.listaprod.configure(yscrollcommand=scroll.set)
        scroll.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)
        self.listaprod.bind("<Double-1>", self.onDoubleClickprod)
    def tela_vendas(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.menus()


        self.frame_1 = Frame(self.root, bd=4, bg='#dfe3ee',
                        highlightbackground='#759fe6', highlightthickness=3)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.3)

        self.frame_2 = Frame(self.root, bd=4, bg='#dfe3ee',
                        highlightbackground='#759fe6', highlightthickness=3)
        self.frame_2.place(relx=0.02, rely=0.34, relwidth=0.96, relheight=0.3)


        self.frame_3 = Frame(self.root, bd=4, bg='#dfe3ee',
                             highlightbackground='#759fe6', highlightthickness=3)
        self.frame_3.place(relx=0.02, rely=0.66, relwidth=0.66, relheight=0.3)

        self.frame_4 = Frame(self.root, bd=4, bg='#dfe3ee',
                             highlightbackground='#759fe6', highlightthickness=3)
        self.frame_4.place(relx=0.688, rely=0.66, relwidth=0.29, relheight=0.3)


        Label(self.frame_1, text='Codigo Vendedor:',  bg='#dfe3ee', fg='black', font=('verdana', 8, 'bold')).place(relx=0.05,
                                                                                                      rely=0.15)
        self.vendedor_combo = ttk.Combobox(self.frame_1, textvariable=self.vendedor_var)
        self.vendedor_combo.place(relx=0.05, rely=0.29, relwidth=0.16, relheight=0.15)

        Label(self.frame_1, text='Nome:', bg='#dfe3ee', fg='black', font=('verdana', 8, 'bold')).place(relx=0.22,
                                                                                             rely=0.15)
        self.nome_v_entry = Entry(self.frame_1)
        self.nome_v_entry.place(relx=0.22, rely=0.29, relwidth=0.5, relheight=0.15)
        # Preencher o ComboBox de Produtos
        self.combo_vendedor()

        # Bind do ComboBox para atualizar o Entry quando o item for selecionado
        self.vendedor_combo.bind("<<ComboboxSelected>>", self.atualizar_entry_vendedor)
        Label(self.frame_1, text='Data:', bg='#dfe3ee', fg='black', font=('verdana', 8, 'bold')).place(relx=0.725,
                                                                                             rely=0.15)
        data_entry = DateEntry(self.frame_1, width=12, background='darkblue',
                               foreground='white', borderwidth=2, date_pattern='dd/MM/yyyy')
        data_entry.place(relx=0.725, rely=0.29, relwidth=0.16, relheight=0.15)

        tkinter.Label(self.frame_1, text='Codigo Produto:', bg='#dfe3ee', fg='black', font=('verdana', 8, 'bold')).place(
            relx=0.05, rely=0.6)
        self.produto_combo = ttk.Combobox(self.frame_1, textvariable=self.produto_var)
        self.produto_combo.place(relx=0.05, rely=0.73, relwidth=0.16, relheight=0.15)

        # Produto (Entry)
        tkinter.Label(self.frame_1, text='Produto:', bg='#dfe3ee', fg='black', font=('verdana', 8, 'bold')).place(relx=0.22,
                                                                                                             rely=0.6)
        self.produto_entry = tkinter.Entry(self.frame_1)
        self.produto_entry.place(relx=0.22, rely=0.73, relwidth=0.4, relheight=0.15)

        # Preencher o ComboBox de Produtos
        self.combo_produto()

        # Bind do ComboBox para atualizar o Entry quando o item for selecionado
        self.produto_combo.bind("<<ComboboxSelected>>", self.atualizar_entry_produto)

        Label(self.frame_1, text='Qtde:', bg='#dfe3ee', fg='black', font=('verdana', 8, 'bold')).place(relx=0.625,
                                                                                                          rely=0.6)
        self.qtde_entry = Entry(self.frame_1)
        self.qtde_entry.place(relx=0.625, rely=0.73, relwidth=0.1, relheight=0.15)
        self.qtde_entry.bind("<KeyRelease>", self.calcular_valor_total)

        Label(self.frame_1, text='Valor Unitario:', bg='#dfe3ee', fg='black', font=('verdana', 8, 'bold')).place(relx=0.73,
                                                                                                          rely=0.6)
        self.V_U_entry = Entry(self.frame_1)
        self.V_U_entry.place(relx=0.73, rely=0.73, relwidth=0.14, relheight=0.15)
        self.V_U_entry.bind("<KeyRelease>", self.calcular_valor_total)

        Label(self.frame_1, text='Valor Total:', bg='#dfe3ee', fg='black', font=('verdana', 8, 'bold')).place(relx=0.88,
                                                                                                          rely=0.6)
        self.v_total_entry = Entry(self.frame_1)
        self.v_total_entry.place(relx=0.88, rely=0.73, relwidth=0.1, relheight=0.15)

        self.btn_adicionar = Button(self.frame_1, text="Adicionar", bg="#4CAF50", fg="white",
                                    font=("verdana", 10, "bold"), command=self.adicionar_produto)
        self.btn_adicionar.place(relx=0.7, rely=0.88, relwidth=0.2, relheight=0.15)

        # Criando a Treeview dentro do frame_2
        self.tabela_produtos = ttk.Treeview(self.frame_2, columns=("#1", "#2", "#3", "#4", "#5"), show='headings')

        # Definindo os títulos das colunas
        self.tabela_produtos.heading("#1", text="Código")
        self.tabela_produtos.heading("#2", text="Produto")
        self.tabela_produtos.heading("#3", text="Quantidade")
        self.tabela_produtos.heading("#4", text="Valor Unitario")  # Valor Unitário
        self.tabela_produtos.heading("#5", text="Valor Total")  # Valor Total

        # Definindo o tamanho das colunas
        self.tabela_produtos.column("#1", width=80)
        self.tabela_produtos.column("#2", width=200)
        self.tabela_produtos.column("#3", width=100, anchor='center')
        self.tabela_produtos.column("#4", width=100, anchor='center')
        self.tabela_produtos.column("#5", width=120, anchor='center')

        # Posicionando a tabela no frame_2
        self.tabela_produtos.pack(fill='both', expand=True, padx=5, pady=5)

        # Adicionando barra de rolagem
        scroll_y = ttk.Scrollbar(self.frame_2, orient='vertical', command=self.tabela_produtos.yview)
        self.tabela_produtos.configure(yscrollcommand=scroll_y.set)
        scroll_y.pack(side='right', fill='y')

        #adicionando cliente
        Label(self.frame_3, text='Codigo Cliente:', bg='#dfe3ee', fg='black', font=('verdana', 8, 'bold')).place(
            relx=0.05,
            rely=0.15)
        self.cliente_combo = ttk.Combobox(self.frame_3, textvariable=self.cliente_var)
        self.cliente_combo.place(relx=0.05, rely=0.29, relwidth=0.19, relheight=0.15)

        self.cliente_combo.bind("<<ComboboxSelected>>", self.atualizar_entry_cliente)

        Label(self.frame_3, text='Nome:', bg='#dfe3ee', fg='black', font=('verdana', 8, 'bold')).place(relx=0.252,
                                                                                                       rely=0.15)
        self.nome_entry = Entry(self.frame_3)
        self.nome_entry.place(relx=0.252, rely=0.29, relwidth=0.4, relheight=0.15)

        Label(self.frame_3, text='Telefone:', bg='#dfe3ee', fg='black', font=('verdana', 8, 'bold')).place(relx=0.667,
                                                                                                       rely=0.15)
        self.telefone_entry = Entry(self.frame_3)
        self.telefone_entry.place(relx=0.667, rely=0.29, relwidth=0.3, relheight=0.15)

        Label(self.frame_3, text='Rua:', bg='#dfe3ee', fg='black', font=('verdana', 8, 'bold')).place(relx=0.05,
                                                                                                       rely=0.45)
        self.rua_entry = Entry(self.frame_3)
        self.rua_entry.place(relx=0.05, rely=0.59, relwidth=0.4, relheight=0.15)

        Label(self.frame_3, text='Bairro:', bg='#dfe3ee', fg='black', font=('verdana', 8, 'bold')).place(relx=0.466,
                                                                                                       rely=0.45)
        self.bairro_entry = Entry(self.frame_3)
        self.bairro_entry.place(relx=0.466, rely=0.59, relwidth=0.3, relheight=0.15)

        Label(self.frame_3, text='Cidade:', bg='#dfe3ee', fg='black', font=('verdana', 8, 'bold')).place(relx=0.05,
                                                                                                       rely=0.73)
        self.cidade_entry = Entry(self.frame_3)
        self.cidade_entry.place(relx=0.05, rely=0.85, relwidth=0.3, relheight=0.15)

        self.btn_novo = Button(self.frame_3, text="Novo cliente", bg="#4CAF50", fg="white",
                                    font=("verdana", 10, "bold"), command=self.cadastroCli)
        self.btn_novo.place(relx=0.7, rely=0.83, relwidth=0.2, relheight=0.15)

        self.combo_cliente()
        self.atualizar_entry_cliente()

        Label(self.frame_4, text='Total Bruto:', bg='#dfe3ee', fg='black', font=('verdana', 8, 'bold')).place(relx=0.02,
                                                                                                       rely=0.02)
        self.totalbruto_entry = Entry(self.frame_4)
        self.totalbruto_entry.place(relx=0.5, rely=0.02, relwidth=0.4, relheight=0.15)

        Label(self.frame_4, text='Desconto (%):', bg='#dfe3ee', fg='black', font=('verdana', 8, 'bold')).place(relx=0.02,
                                                                                                       rely=0.2)
        self.desconto_entry = Entry(self.frame_4)
        self.desconto_entry.place(relx=0.5, rely=0.195, relwidth=0.4, relheight=0.15)

        Label(self.frame_4, text='Total Liquido:', bg='#dfe3ee', fg='black', font=('verdana', 8, 'bold')).place(relx=0.02,
                                                                                                           rely=0.35)
        self.totalliquido_entry = Entry(self.frame_4)
        self.totalliquido_entry.place(relx=0.5, rely=0.365, relwidth=0.4, relheight=0.15)

        Label(self.frame_4, text='Total Pago:', bg='#dfe3ee', fg='black', font=('verdana', 8, 'bold')).place(relx=0.02,
                                                                                                      rely=0.55)
        self.totalpago_entry = Entry(self.frame_4)
        self.totalpago_entry.place(relx=0.5, rely=0.53, relwidth=0.4, relheight=0.15)

        Label(self.frame_4, text='Troco:', bg='#dfe3ee', fg='black', font=('verdana', 8, 'bold')).place(relx=0.02,
                                                                                                         rely=0.7)
        self.troco_entry = Entry(self.frame_4)
        self.troco_entry.place(relx=0.5, rely=0.7, relwidth=0.4, relheight=0.15)

        self.btn_ok = Button(self.frame_4, text="OK", bg="#4CAF50", fg="white",
                               font=("verdana", 10, "bold"),command=self.salvar_venda)
        self.btn_ok.place(relx=0.02, rely=0.85, relwidth=0.2, relheight=0.15)

        self.atualizar_total_bruto()
        self.totalpago_entry.bind("<KeyRelease>", self.calcular_troco)


    def calcular_total_liquido(self, total_bruto):
        try:
            desconto = float(self.desconto_entry.get())  # Lê o desconto inserido pelo usuário
        except ValueError:
            desconto = 0  # Caso o desconto não seja um número válido, assume 0

        # Calcula o total líquido com base no total bruto e no desconto
        total_liquido = total_bruto - (total_bruto * (desconto / 100))

        # Atualiza o campo de "Total Liquido"
        self.totalliquido_entry.delete(0, 'end')
        self.totalliquido_entry.insert(0, f"{total_liquido:.2f}")




Application()
