import psycopg2

# Estabelece uma conexão com o banco de dados PostgreSQL
conn = psycopg2.connect(database="postgres", user="postgres", password="1234", port="5433")
print("Conexão com o banco de Dados aberta com sucesso!")

# Cria um objeto de cursor para executar comandos SQL
comando = conn.cursor()

# Executa uma operação DELETE SQL para excluir o registro com id igual a 1
comando.execute("DELETE FROM AGENDA WHERE id = 1")
conn.commit()

# Obtém o número de registros afetados pela operação DELETE
cont = comando.rowcount

# Imprime a quantidade de registros excluídos e uma mensagem de sucesso
print(cont, "-> Registro excluído com sucesso!")
print("Exclusão realizada com sucesso!!!")

# Fecha a conexão com o banco de dados
conn.close()
