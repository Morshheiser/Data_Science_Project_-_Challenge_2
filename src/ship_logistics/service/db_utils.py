import psycopg2

# Configurações do banco de dados
# Avoid hardcoded things
# Use .env (Environment variables)
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'postgres'
DB_USER = 'postgres'
DB_PASSWORD = '12345'


# Inject the connection parameters as function parameters and dont reference to global variables
def get_connection():
    """
    Estabelece e retorna uma conexão com o banco de dados PostgreSQL.
    """
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        print("Conexão ao banco de dados estabelecida com sucesso.")
        return conn
    except psycopg2.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        raise

def execute_query(query, params=None):
    """
    Executa uma consulta SQL no banco de dados.
    """
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(query, params)
            conn.commit()
            print("Consulta executada com sucesso.")
    except psycopg2.Error as e:
        print(f"Erro ao executar consulta: {e}")
        conn.rollback()
    finally:
        conn.close()

# def fetch_query(query, params=None):
#     """
#     Executa uma consulta SQL e retorna os resultados.
#     """
#     conn = get_connection()
#     try:
#         with conn.cursor() as cursor:
#             cursor.execute(query, params)
#             results = cursor.fetchall()
#             print("Consulta realizada com sucesso.")
#             return results
#     except psycopg2.Error as e:
#         print(f"Erro ao realizar consulta: {e}")
#         return None
#     finally:
#         conn.close()
