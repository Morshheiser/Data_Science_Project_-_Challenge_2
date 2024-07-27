from pathlib import Path
from ship_logistics.service.execute_query import execute_query

# Lista ordenada de arquivos SQL
BASE_PATH = Path(__file__).parent.parent / "data" / "sql"
sql_files = [
    BASE_PATH / "drop_tables.sql",
    BASE_PATH / "create_measurement_values.sql",
    BASE_PATH / "create_type_load.sql",
    BASE_PATH / "create_type_ship.sql",
    BASE_PATH / "create_ship.sql",
    BASE_PATH / "create_charge_discharge.sql",
    BASE_PATH / "create_port.sql",
    BASE_PATH / "create_port_costs.sql",
    BASE_PATH / "create_routes.sql",
    BASE_PATH / "create_type_cost.sql",
    BASE_PATH / "create_costs.sql",
    BASE_PATH / "create_ship_log.sql",
    BASE_PATH / "insert_into_SHIP.SQL",
    BASE_PATH / "insert_into_TYPE_COST.SQL",
    BASE_PATH / "insert_into_TYPE_LOAD_NAME.SQL",
    BASE_PATH / "insert_into_type_load.sql",
    BASE_PATH / "insert_into_type_MEASUREMENT_VALUES.SQL",
    BASE_PATH / "insert_into_type_PORT_COST.SQL",
    BASE_PATH / "insert_into_type_PORT.SQL",
    BASE_PATH / "insert_into_type_ROUTES.SQL"
]

def run_sql_scripts(sql_files=sql_files):
    """
    Lê uma lista de arquivos SQL e executa os comandos SQL no banco de dados.
    """
    for file_path in sql_files:
        if file_path.exists():
            print(f"Lendo o arquivo SQL: {file_path}")
            
            # Lê o conteúdo do arquivo SQL
            try:
                with open(file_path, 'r') as file:
                    sql_script = file.read()
                
                # Executa o script SQL
                execute_query(sql_script)
                print(f"Script SQL executado: {file_path}")
            except Exception as e:
                print(f"Erro ao ler ou executar o script {file_path}: {e}")
        else:
            print(f"Arquivo SQL não encontrado: {file_path}")

# Exemplo de chamada da função
if __name__ == "__main__":
    run_sql_scripts()
