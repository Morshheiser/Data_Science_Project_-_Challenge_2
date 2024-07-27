import pandas as pd
from pathlib import Path

# Definição dos mapeamentos
TYPE_SHIP_column_mapping = {
    'ship_type.csv': {'Type': 'TYPE_NAME'}
}

TYPE_LOAD_column_mapping = {
    'navio_ro_ro.csv': {'Tipo de Veículos': 'LOAD_NAME'},
    'navio_porta_conteiner.csv': {'Tipo de Contêineres': 'LOAD_NAME'},
    'navio_graneleiro.csv': {'Tipo de Carga': 'LOAD_NAME'},
    'navio_frigorifico.csv': {'Tipo de Carga': 'LOAD_NAME'},
    'navio_carga_geral.csv': {'Tipo de Carga': 'LOAD_NAME'}
}

MEASUREMENT_VALUES_column_mapping = {
    'navio_ro_ro.csv': {'Número de Veículos': 'NUMBER_OF_VEHICLES'},
    'navio_porta_conteiner.csv': {'Número de Contêineres': 'NUMBER_OF_CONTAINERS'},
    'navio_graneleiro.csv': {'Tonelagem': 'WEIGHT_TONNAGE'},
    'navio_frigorifico.csv': {'Temperatura': 'TEMP', 'Volume': 'VOLUME', 'Volume (m³)': 'VOLUME'},
    'navio_carga_geral.csv': {'Volume': 'VOLUME', 'Volume (m³)': 'VOLUME'}
}

SHIP_column_mapping = {
    'navio_ro_ro.csv': {'Nome do Navio': 'SHIP_NAME'},
    'navio_porta_conteiner.csv': {'Nome do Navio': 'SHIP_NAME'},
    'navio_graneleiro.csv': {'Nome do Navio': 'SHIP_NAME'},
    'navio_frigorifico.csv': {'Nome do Navio': 'SHIP_NAME'},
    'navio_carga_geral.csv': {'Nome do Navio': 'SHIP_NAME'}
}

CHARGE_DISCHARGE_column_mapping = {}  # Adicione mapeamentos se disponíveis

PORT_column_mapping = {
    'portos.csv': {'Nome_Porto': 'PORT_NAME', 'Pais': 'COUNTRY', 'Latitude': 'LATITUDE', 'Longitude': 'LONGITUDE'}
}

PORT_COSTS_column_mapping = {
    'taxas_portuarias.csv': {'Tipo_Taxa': 'RATE_TYPE', 'Valor_Por_Navio': 'VALUE_PER_SHIP', 'Valor_Por_Tonelada': 'VALUE_PER_TON'}
}

ROUTES_column_mapping = {
    'rotas.csv': {'Distancia': 'DISTANCE', 'Tempo_Medio': 'AVERAGE_TIME'}
}

TYPE_COST_column_mapping = {
    'navio_ro_ro.csv': {'Tipo de Custo': 'TYPE_COST'},
    'navio_porta_conteiner.csv': {'Tipo de Custo': 'TYPE_COST'},
    'navio_graneleiro.csv': {'Tipo de Custo': 'TYPE_COST'},
    'navio_frigorifico.csv': {'Tipo de Custo': 'TYPE_COST'},
    'navio_carga_geral.csv': {'Tipo de Custo': 'TYPE_COST'}
}

COSTS_column_mapping = {
    'navio_ro_ro.csv': {'Data': 'DATE_', 'Valor (USD)': 'VALUE'},
    'navio_porta_conteiner.csv':  {'Data': 'DATE_', 'Valor (USD)': 'VALUE'},
    'navio_graneleiro.csv': {'Data': 'DATE_', 'Valor (USD)': 'VALUE'},
    'navio_frigorifico.csv':  {'Data': 'DATE_', 'Valor (USD)': 'VALUE'},
    'navio_carga_geral.csv':  {'Data': 'DATE_', 'Valor (USD)': 'VALUE'}
}

# Mapeamento geral
mappings = {
    'TYPE_SHIP': TYPE_SHIP_column_mapping,
    'TYPE_LOAD': TYPE_LOAD_column_mapping,
    'MEASUREMENT_VALUES': MEASUREMENT_VALUES_column_mapping,
    'SHIP': SHIP_column_mapping,
    'CHARGE_DISCHARGE': CHARGE_DISCHARGE_column_mapping,
    'PORT': PORT_column_mapping,
    'PORT_COSTS': PORT_COSTS_column_mapping,
    'ROUTES': ROUTES_column_mapping,
    'TYPE_COST': TYPE_COST_column_mapping,
    'COSTS': COSTS_column_mapping
}

def load_and_process_csv(file_path, table_name):
    """
    Carrega um arquivo CSV, aplica o mapeamento e salva o DataFrame processado no mesmo arquivo CSV.
    """
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {file_path}")
        return
    except Exception as e:
        print(f"Erro ao ler o arquivo {file_path}: {e}")
        return
    
    # Verifica se o nome do arquivo tem um mapeamento
    file_name = file_path.name
    column_mapping = mappings.get(table_name, {}).get(file_name)
    
    if not column_mapping:
        print(f"No mapping found for {file_name} in table {table_name}")
        return
    
    # Renomeia as colunas com base no mapeamento
    df.rename(columns=column_mapping, inplace=True)
    
    # Salva o DataFrame processado no mesmo arquivo CSV
    try:
        df.to_csv(file_path, index=False)
        print(f"Dados processados e salvos em {file_path}")
    except Exception as e:
        print(f"Erro ao salvar o arquivo {file_path}: {e}")

def process_all_files(input_directory):
    """
    Processa todos os arquivos CSV de acordo com os mapeamentos definidos.
    """
    input_path = Path(input_directory)
    for table_name, files in mappings.items():
        for file_name in files.keys():
            file_path = input_path / file_name
            load_and_process_csv(file_path, table_name)

# Exemplo de uso
input_directory = '/home/emorshhe/Data_Science_Project_-_Challenge_2/src/ship_logistics/data/csv/input'
process_all_files(input_directory)
