import os
from db_utils import execute_query

# Lista ordenada de arquivos SQL
sql_files = [
    "C:\\Users\\morsh\\Desktop\\Casa DIgital\\Data_Science_Project_-_Challenge_2\\data\\sql\\drop_tables.sql",
    "C:\\Users\\morsh\\Desktop\\Casa DIgital\\Data_Science_Project_-_Challenge_2\\data\\sql\\create_measurement_values.sql",
    "C:\\Users\\morsh\\Desktop\\Casa DIgital\\Data_Science_Project_-_Challenge_2\\data\\sql\\create_type_load.sql",
    "C:\\Users\\morsh\\Desktop\\Casa DIgital\\Data_Science_Project_-_Challenge_2\\data\\sql\\create_type_ship.sql",
    "C:\\Users\\morsh\\Desktop\\Casa DIgital\\Data_Science_Project_-_Challenge_2\\data\\sql\\create_ship.sql",
    "C:\\Users\\morsh\\Desktop\\Casa DIgital\\Data_Science_Project_-_Challenge_2\\data\\sql\\create_charge_discharge.sql",
    "C:\\Users\\morsh\\Desktop\\Casa DIgital\\Data_Science_Project_-_Challenge_2\\data\\sql\\create_port.sql",
    "C:\\Users\\morsh\\Desktop\\Casa DIgital\\Data_Science_Project_-_Challenge_2\\data\\sql\\create_port_costs.sql",
    "C:\\Users\\morsh\\Desktop\\Casa DIgital\\Data_Science_Project_-_Challenge_2\\data\\sql\\create_routes.sql",
    "C:\\Users\\morsh\\Desktop\\Casa DIgital\\Data_Science_Project_-_Challenge_2\\data\\sql\\create_type_cost.sql",
    "C:\\Users\\morsh\\Desktop\\Casa DIgital\\Data_Science_Project_-_Challenge_2\\data\\sql\\create_costs.sql"
]

def run_sql_scripts(sql_files):
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
