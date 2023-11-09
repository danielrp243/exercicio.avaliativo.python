import psycopg2

def inserir_dados_na_agenda(conn, nome, telefone):
    comando = conn.cursor()

    # Gere um novo ID para a inserção
    comando.execute("SELECT max(id) FROM Agenda")
    ultimo_id = comando.fetchone()[0]

    if ultimo_id is not None:
        novo_id = ultimo_id + 1
    else:
        novo_id = 1

    comando.execute("""
    INSERT INTO Agenda (id, Nome, Telefone)
    VALUES (%s, %s, %s)
    """, (novo_id, nome, telefone))

    conn.commit()
    print("Inserção realizada com sucesso!!!")
    conn.close()
