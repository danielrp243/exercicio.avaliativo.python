import psycopg2

# Estabelece uma conexão com o banco de dados PostgreSQL
conn = psycopg2.connect(database="postgres", user="postgres", password="1234", port="5433")
print("Conexão com o banco de Dados aberta com sucesso!")

# Cria um objeto de cursor para executar comandos SQL
comando = conn.cursor()

# Executa uma consulta SQL para selecionar um registro com id igual a 2
comando.execute("SELECT * FROM AGENDA WHERE id = 2")
registro = comando.fetchone()

# Imprime o registro encontrado
print("Dados encontrados ->", registro)

# Não é necessário chamar conn.commit() para consultas de leitura (SELECT).
# Você pode remover essa linha.

# Fecha a conexão com o banco de dados
conn.close()
