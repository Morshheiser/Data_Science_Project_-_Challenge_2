# execute_query.py

import psycopg2
from ship_logistics.get_connection_db import get_connection


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

if __name__ == "__main__":
    # Exemplo de uso da função execute_query
    test_query = "SELECT version();"
    execute_query(test_query)
