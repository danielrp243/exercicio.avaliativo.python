import psycopg2

# Estabelece uma conexão com o banco de dados PostgreSQL
conn = psycopg2.connect(database="postgres", user="postgres", password="1234", port="5433")
print("Conexão com o banco de Dados aberta com sucesso!")

# Cria um objeto de cursor para executar comandos SQL
comando = conn.cursor()

# Executa uma consulta SQL para selecionar um registro com id igual a 1
comando.execute("SELECT * FROM AGENDA WHERE id = 1")
registro = comando.fetchone()
print("Dados encontrados ->", registro)

# Executa uma atualização para alterar o telefone do registro com id igual a 1
comando.execute("UPDATE AGENDA SET telefone = 96385471 WHERE id = 1")
conn.commit()
print("Registro atualizado com sucesso!!!")

# Cria um novo objeto de cursor para uma nova consulta
comando = conn.cursor()
print("--- Consulta após a atualização ---")

# Executa uma nova consulta SQL para selecionar o registro atualizado
comando.execute("SELECT * FROM AGENDA WHERE id = 1")
registro = comando.fetchone()
print("Dados atualizados ->", registro)

# Não é necessário chamar conn.commit() após a segunda consulta SELECT.
# Você pode remover essa linha.

# Fecha a conexão com o banco de dados
conn.close()
