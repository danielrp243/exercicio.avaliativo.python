import psycopg2

class AppBD:
    def __init__(self):
        print('Método Construtor')
        self.connection = None  # Inicializa a conexão como nula

    def abrirConexao(self):
        try:
            # Tenta estabelecer a conexão com o banco de dados
            self.connection = psycopg2.connect(user="postgres", password="1234",
                                              host="127.0.0.1", port="5432",
                                              database="postgres")
            print("Conexão com o Banco de Dados aberta com sucesso!")
        except (Exception, psycopg2.Error) as error:
            if self.connection:
                print("Falha ao se conectar ao Banco de Dados", error)

    def fecharConexao(self):
        if self.connection:
            self.connection.close()
            print("Conexão com o Banco de Dados fechada com sucesso!")

# Exemplo de uso:
app = AppBD()
app.abrirConexao()
# Aqui você pode realizar operações no banco de dados
# ...
app.fecharConexao()
