import sqlite3

# Conectar ao banco de dados ou criar um novo banco de dados
con = sqlite3.connect('dados.db')

# Criando uma tabela de livros, se não existir
con.execute('''CREATE TABLE IF NOT EXISTS livros(
                id INTEGER PRIMARY KEY,
                titulo TEXT,
                autor TEXT,
                editora TEXT,
                ano_publicacao INTEGER,
                isbn TEXT)''')

# Criando uma tabela de usuários, se não existir
con.execute('''CREATE TABLE IF NOT EXISTS usuarios(
                id INTEGER PRIMARY KEY,
                nome TEXT,
                sobrenome TEXT,
                endereco TEXT,
                email TEXT,
                telefone TEXT)''')

# Criando uma tabela de empréstimos, se não existir
con.execute('''CREATE TABLE IF NOT EXISTS emprestimos(
                id INTEGER PRIMARY KEY,
                id_livro INTEGER,
                id_usuario INTEGER,
                data_emprestimo TEXT,
                data_devolucao TEXT,
                FOREIGN KEY(id_livro) REFERENCES livros(id),
                FOREIGN KEY(id_usuario) REFERENCES usuarios(id))''')

# Salvar as mudanças e fechar a conexão
con.commit()
con.close()
