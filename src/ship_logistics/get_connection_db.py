import psycopg2
import os

# Definindo variáveis de ambiente diretamente
os.environ['DB_NAME'] = 'postgres'
os.environ['DB_USER'] = 'postgres'
os.environ['DB_PASSWORD'] = '12345'
os.environ['DB_HOST'] = '172.29.209.240'
os.environ['DB_PORT'] = '5432'

def get_connection():
    """
    Estabelece e retorna uma conexão com o banco de dados PostgreSQL usando variáveis de ambiente.
    """
    try:
        conn = psycopg2.connect(
            dbname=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT')
        )
        print("Conexão ao banco de dados estabelecida com sucesso.")
        return conn
    except psycopg2.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        raise
