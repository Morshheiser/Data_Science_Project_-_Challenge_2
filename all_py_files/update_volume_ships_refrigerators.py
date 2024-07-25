import pandas as pd
import re
import os

def update_volume_column(directory, file_name):
    # Defina o caminho completo do arquivo
    file_path = os.path.join(directory, file_name)

    # Carregue o arquivo CSV
    df = pd.read_csv(file_path)

    # Verifique se a coluna 'Volume (m³)' existe, se não, crie-a
    if 'Volume (m³)' not in df.columns:
        df['Volume (m³)'] = None

    # Função para extrair o volume da descrição
    def extract_volume(description):
        if pd.notna(description):
            match = re.search(r'(\d+)\s*m³', description)
            if match:
                return float(match.group(1))
        return None

    # Aplique a função para extrair e preencher os valores na coluna 'Volume (m³)'
    df['Volume (m³)'] = df.apply(lambda row: extract_volume(row['Descrição']) if pd.isna(row['Volume (m³)']) else row['Volume (m³)'], axis=1)

    # Salve o DataFrame modificado de volta para o mesmo arquivo CSV
    df.to_csv(file_path, index=False)

    print("Arquivo atualizado com sucesso!")

if __name__ == "__main__":
    # Defina o diretório e o nome do arquivo
    directory = 'C:/Users/morsh/Desktop/Casa DIgital/Data_Science_Project_-_Challenge_2/ship_project/input_csv'
    file_name = 'navio_frigorifico.csv'
    
    # Chame a função para atualizar a coluna de volume
    update_volume_column(directory, file_name)
