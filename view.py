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

    if not livros:
        print("Nenhum livro encontrado na biblioteca")
        return
    
    print("Livros na biblioteca: ")
    for livro in livros:
        print(f"ID: {livro[0]}")
        print(f"Título: {livro[1]}")
        print(f"Autor: {livro[2]}")
        print(f"Editora: {livro[3]}")
        print(f"Telefone: {livro[4]}")
        print(f"ISBN: {livro[5]}")
        print("\n")

# Função para exibir os usuarios
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
    # Verifica se há livros emprestados sem data de devolução (em aberto)
    result = conn.execute("""
        SELECT livros.titulo, usuarios.nome, usuarios.sobrenome, 
               emprestimos.data_emprestimo, emprestimos.data_devolucao
        FROM livros
        INNER JOIN emprestimos ON livros.id = emprestimos.id_livro
        INNER JOIN usuarios ON usuarios.id = emprestimos.id_usuario
        WHERE emprestimos.data_devolucao IS NULL
    """).fetchall()
    conn.close()

    # Exibir os resultados
    if not result:
        print("Nenhum livro está emprestado no momento.")
    else:
        print("Livros emprestados no momento:")
        for row in result:
            print(f"Título: {row[0]}")
            print(f"Usuário: {row[1]} {row[2]}")
            print(f"Data de Empréstimo: {row[3]}")
            print(f"Data de Devolução: {row[4] if row[4] else 'Não devolvido'}")
            print("-" * 40)
    return result

#Funcao para atualizar a data de devolucao de emprestimo
def update_loan_return_date(id_emprestimo, data_devolucao):
    conn = connect()
    conn.execute("UPDATE emprestimos SET data_devolucao = ? WHERE id = ?",(data_devolucao. id_emprestimo))
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

# Exemplo de uso da função de exclusão
# Deletar o livro com ID 1 (se estiver emprestado)
#delete_book_on_loan()

#insert_loan(2, 2, "13-10-2020", None)
# Exemplo de uso das funções
#insert_book("Boku no hero", "J.K. Rowling", "Editora 1", 2000, "123456")
#insert_user("Marco Antonio", "Maldonado", "Rua dos Bobos", "mamaldonado241@Gmail.com", "679981453026")
#insert_loan(1, 1, "13-10-2024", None)
#update_loan_return_date(1, "23-03-2000")
print (get_books_on_loan())
#exibir_livros()
#exibir_usuarios()

