# Importe os módulos necessários
import psycopg2
from minha_classe import MinhaClasse
from insert_agenda_data import inserir_dados_na_agenda
from select_agenda_data import selecionar_dados_da_agenda
from update_agenda_data import atualizar_dados_na_agenda
from delete_agenda_data import excluir_dados_na_agenda

# Crie uma instância da classe MinhaClasse
minha_instancia = MinhaClasse()

# Conecte-se ao banco de dados PostgreSQL
try:
    conn = psycopg2.connect(database="postgres", user="postgres", password="1234", host="127.0.0.1", port="5432")
    print("Conexão com o Banco de Dados aberta com sucesso!")

    # Realize ações no banco de dados
    # Exemplo: inserir dados na agenda
    inserir_dados_na_agenda(conn)

    # Exemplo: selecionar dados da agenda
    selecionar_dados_da_agenda(conn)

    # Exemplo: atualizar dados na agenda
    atualizar_dados_na_agenda(conn)

    # Exemplo: excluir dados da agenda
    excluir_dados_na_agenda(conn)

except (Exception, psycopg2.Error) as error:
    print("Falha ao se conectar ao Banco de Dados", error)

# Certifique-se de fechar a conexão após as operações no banco de dados
if conn:
    conn.close()
    print("Conexão com o Banco de Dados fechada com sucesso!")
