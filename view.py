import sqlite3

# Conectar ao banco de dados
def connect():
    conn = sqlite3.connect('dados.db')
    return conn

# Função para inserir um novo livro
def insert_book(titulo, autor, editora, ano_publicacao, isbn):
    conn = connect()
    conn.execute("INSERT INTO livros(titulo, autor, editora, ano_publicacao, isbn)\
                 VALUES (?, ?, ?, ?, ?)", (titulo, autor, editora, ano_publicacao, isbn))
    conn.commit()
    conn.close()

#Funcao para exibir usuarios
def get_users():
    conn = connect()
    c = conn.cursor()
    c.execute('SELECT * FROM usuarios')
    users = c.fetchall()
    conn.close()
    return users

# Função para inserir um novo usuário
def insert_user(nome, sobrenome, endereco, email, telefone):
    conn = connect()
    conn.execute("INSERT INTO usuarios(nome, sobrenome, endereco, email, telefone)\
                 VALUES(?,?,?,?,?)", (nome, sobrenome, endereco, email, telefone))
    conn.commit()
    conn.close()

# Função para exibir os livros
def exibir_livros():
    conn = connect()
    livros = conn.execute("SELECT * FROM livros").fetchall()
    conn.close()

    return livros




# Função para exibir os usuários
def exibir_usuarios():
    conn = connect()
    usuarios = conn.execute("SELECT * FROM usuarios").fetchall()
    conn.close()

    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return
    
    print("Usuários Cadastrados: ")
    for usuario in usuarios:
        print(f"Nome: {usuario[0]}")
        print(f"Sobrenome: {usuario[1]}")
        print(f"Endereço: {usuario[2]}")
        print(f"Email: {usuario[3]}")
        print(f"Telefone: {usuario[4]}")
        print("\n")

# Função para realizar empréstimos
def insert_loan(id_livro, id_usuario, data_emprestimo, data_devolucao):
    conn = connect()
    conn.execute("INSERT INTO emprestimos(id_livro, id_usuario, data_emprestimo, data_devolucao)\
                VALUES(?,?,?,?)",(id_livro, id_usuario, data_emprestimo, data_devolucao))
    conn.commit()
    conn.close()


# Função para exibir todos os livros emprestados no momento
def get_books_on_loan():
    conn = connect()
    result = conn.execute("SELECT emprestimos.id, livros.titulo, usuarios.nome, usuarios.sobrenome, emprestimos.data_emprestimo, emprestimos.data_devolucao \
                           FROM livros \
                           INNER JOIN emprestimos ON livros.id = emprestimos.id_livro \
                           INNER JOIN usuarios ON usuarios.id = emprestimos.id_usuario \
                           WHERE emprestimos.data_devolucao IS NULL").fetchall()
    conn.close()
    return result

# Função para atualizar a data de devolução de empréstimo
def update_loan_return_date(id_emprestimo, data_devolucao):
    conn = connect()
    conn.execute("UPDATE emprestimos SET data_devolucao = ? WHERE id = ?", (data_devolucao, id_emprestimo))
    conn.commit()
    conn.close()


# Função para excluir um empréstimo e o livro associado
def delete_book_on_loan(id_livro):
    conn = connect()

    # Verificar se o livro está emprestado (se a data de devolução é NULL)
    emprestimos = conn.execute("SELECT id FROM emprestimos WHERE id_livro = ? AND data_devolucao IS NULL", (id_livro,)).fetchall()
    
    if not emprestimos:
        print(f"O livro com ID {id_livro} não está emprestado ou não existe.")
        conn.close()
        return
   

    # Excluir o empréstimo associado ao livro
    conn.execute("DELETE FROM emprestimos WHERE id_livro = ? AND data_devolucao IS NULL", (id_livro,))
    
    # Agora excluir o livro da tabela 'livros'
    conn.execute("DELETE FROM livros WHERE id = ?", (id_livro,))
    
    conn.commit()
    conn.close()
    
    print(f"O livro com ID {id_livro} foi excluído, junto com o empréstimo associado.")

#Exlcluir usuarios cadastrados
def delete_user_on_loan(user_id):
    conn = sqlite3.connect('dados.db')  # Conectar ao banco de dados
    try:
        # Verificar se o usuário está emprestado
        exibir_usuarios = conn.execute("SELECT id FROM usuarios WHERE id = ?", (user_id,)).fetchall()
        
        if not exibir_usuarios:
            print(f"O usuário com ID {user_id} não existe.")
            return
        
        # Excluir o empréstimo associado ao usuário
        conn.execute("DELETE FROM emprestimos WHERE id_usuario = ?", (user_id,))
        
        # Agora excluir o usuário da tabela 'usuarios'
        conn.execute("DELETE FROM usuarios WHERE id = ?", (user_id,))
        
        conn.commit()
        print(f"O usuário com ID {user_id} foi excluído, junto com o empréstimo associado.")
    
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    
    finally:
        conn.close()


