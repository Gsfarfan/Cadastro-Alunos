import sqlite3 as lite


try:
    con = lite.connect('cadastro_alunos.db')
    print('Conexao com o banco de dados realizado com sucesso!')
except lite.Error as e:
    print("Erro ao conectar com o banco de dados:", e)

###################################################################################################

def criar_curso(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Cursos (nome, duracao, preco) VALUES (?,?,?)"
        cur.execute(query,i)

def ver_cursos():
    lista = []
    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM Cursos')
        linha = cur.fetchall()

        for i in linha:
            lista.append(i)
        return lista
    
def atualizar_curso(i):
    with con:
        cur = con.cursor()
        query = "UPDATE Cursos SET nome=?, duracao=?, preco=? WHERE id=?"
        cur.execute(query,i)


def deletar_curso(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Cursos WHERE id=?"
        cur.execute(query,i)

########################################################################################

def criar_turma(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Turmas (nome, curso_nome, data_inicio) VALUES (?, ?, ?)"
        cur.execute(query, i)

def ver_turmas():
    lista = []
    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM Turmas')
        linha = cur.fetchall()

        for i in linha:
            lista.append(i)
    return lista

def atualizar_turma(i):
    with con:
        cur = con.cursor()
        query = "UPDATE turmas SET nome=?, curso_nome=?, data_inicio=? WHERE id=?"
        cur.execute(query,i)

def deletar_turma(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Turmas WHERE id=?"
        cur.execute(query,i)

#################################################################################################

def criar_alunos(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Alunos (nome, email, telefone, sexo, imagem, data_nascimento, cpf, turma_nome) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
        cur.execute(query, i)

def ver_alunos():
    lista = []
    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM Alunos')
        linha = cur.fetchall()

        for i in linha:
            lista.append(i)
    return lista

def atualizar_alunos(i):
    with con:
        cur = con.cursor()
        query = "UPDATE Turma SET nome=?, email=?, telefone=?, sexo=?, imagem=?, data_nascimento=?, cpf=?, turma_nome=? WHERE id=?"
        cur.execute(query,i)

def deletar_alunos(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Alunos WHERE id=?"
        cur.execute(query,i)


