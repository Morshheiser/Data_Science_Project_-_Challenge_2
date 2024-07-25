from pathlib import Path
from src.ship_logistics.service.db_utils import execute_query

# Lista ordenada de arquivos SQL
# Avoid hardcoded things... in this case I changed the path to a module global variable with the data directory path
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
    BASE_PATH / "create_costs.sql"
]

def run_sql_scripts(sql_files=sql_files):
    """
    Lê uma lista de arquivos SQL e executa os comandos SQL no banco de dados.
    """
    for file_path in sql_files:
        print(f"Lendo o arquivo SQL: {file_path}")
        
        # Lê o conteúdo do arquivo SQL
        with open(file_path, 'r') as file:
            sql_script = file.read()
        
        # Executa o script SQL
        execute_query(sql_script)
        print(f"Script SQL executado: {file_path}")
