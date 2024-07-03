import pandas as pd
import os

def create_ship_id_mapping(df):
    # Ordena o DataFrame pelo Nome do Navio em ordem alfabética
    df_sorted = df.sort_values(by='Nome do Navio')
    
    # Cria o mapeamento de IDs de navios baseado no DataFrame ordenado
    ship_id_map = {nome_navio: idx + 1 for idx, nome_navio in enumerate(df_sorted['Nome do Navio'].unique())}
    return ship_id_map

def save_ship_id_mapping(ship_id_map, output_directory):
    ship_id_df = pd.DataFrame(list(ship_id_map.items()), columns=['Nome do Navio', 'ID do Navio'])
    output_file = os.path.join(output_directory, 'ship_id_mapping.csv')
    ship_id_df.to_csv(output_file, index=False)
    print(f'Tabela de mapeamento de IDs de navios foi salva em {output_file}')

def separate_by_ship(file_path, output_directory):
    try:
        # Carrega o arquivo CSV geral
        df_general = pd.read_csv(file_path)

        # Cria o mapeamento de IDs de navios ordenando primeiro pelo Nome do Navio
        ship_id_map = create_ship_id_mapping(df_general)

        # Salva a tabela de mapeamento de IDs de navios
        save_ship_id_mapping(ship_id_map, output_directory)

        # Substitui o nome do navio pelo ID único no DataFrame geral
        df_general['ID do Navio'] = df_general['Nome do Navio'].map(ship_id_map)

        # Ordena o DataFrame primeiro pelo ID do navio e depois pela data
        df_general.sort_values(by=['ID do Navio', 'Data'], inplace=True)

        # Define o caminho completo para o arquivo de saída
        output_file = os.path.join(output_directory, 'ships_id.csv')

        # Salva o resultado em um novo arquivo CSV
        df_general.to_csv(output_file, index=False)
        
        print(f'Dados separados por navio foram salvos em {output_file}')
    
    except Exception as e:
        print(f'Ocorreu um erro durante o processamento: {str(e)}')
