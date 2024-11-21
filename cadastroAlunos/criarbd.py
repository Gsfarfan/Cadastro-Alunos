import sqlite3

try:
    con = sqlite3.connect('cadastro_alunos.db')
    print('Conexao com o banco de dados realizado com sucesso!')
except sqlite3.Error as e:
    print("Erro ao conectar com o banco de dados:", e)

#####################################################################################################################

try:
    with con:
        cur = con.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS cursos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,     
            nome TEXT,
            duracao TEXT,
            preco REAL       
            )""")
        
        print("Tabela Cursos criado com sucesso!")

        
except sqlite3.Error as e:
    print("Erro ao criar a tabela cursos:", e)

################################################################################################################

try:
    with con:
        cur = con.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS turmas(
            id INTEGER PRIMARY KEY AUTOINCREMENT,     
            nome TEXT,
            curso_nome TEXT,
            data_inicio DATE,     
            FOREIGN KEY (curso_nome) REFERENCES cursos (nome) ON UPDATE CASCADE ON DELETE CASCADE
            )""")
        
        print("Tabela turmas criado com sucesso!")

        
except sqlite3.Error as e:
    print("Erro ao criar a tabela turmas:", e)

##############################################################################################################

try:
    with con:
        cur = con.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS alunos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,     
            nome TEXT,
            email TEXT,
            telefone TEXT,  
            sexo TEXT,
            imagem TEXT,
            data_nascimento DATE,
            cpf TEXT,
            turma_nome TEXT,
            FOREIGN KEY (turma_nome) REFERENCES turmas (nome) ON DELETE CASCADE
            )""")
        
        print("Tabela Alunos criado com sucesso!")

        
except sqlite3.Error as e:
    print("Erro ao criar a tabela Alunos:", e)