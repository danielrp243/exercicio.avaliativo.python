# Importando a biblioteca psycopg2
import psycopg2

# Estabelecendo uma conexão com o banco de dados PostgreSQL
conn = psycopg2.connect(database="postgres", user="postgres", password="1234", port="5433")

# Imprimindo uma mensagem de confirmação de conexão
print("Conexão com o Banco de Dados aberta com sucesso!")

# Criando um objeto cursor para executar comandos SQL
comando = conn.cursor()

# Executando um comando SQL para criar a tabela "Agenda"
comando.execute("""
    CREATE TABLE Agenda
    (id INT PRIMARY KEY NOT NULL,
    Nome TEXT NOT NULL,
    Telefone CHAR(12));
""")

# Confirmando as alterações no banco de dados
conn.commit()

# Imprimindo uma mensagem de confirmação da criação da tabela
print("Tabela criada com sucesso no BD!!!")

# Fechando a conexão com o banco de dados
conn.close()
