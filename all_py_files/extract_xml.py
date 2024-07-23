import os
import pandas as pd
import xml.etree.ElementTree as ET

def process_all_xml_files(xml_directory, csv_directory):
    # Conjunto para armazenar pontos de dados únicos
    data_set = set()

    # Função para extrair dados de um arquivo XML
    def extract_data_from_xml(xml_file):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        
        navio_id = root.get('ID')
        navio_nome = root.find('Nome').text
        
        for ponto in root.findall('.//PontoDeDados'):
            timestamp = ponto.get('Timestamp')
            latitude = ponto.find('Latitude').text
            longitude = ponto.find('Longitude').text
            velocidade = ponto.find('Velocidade').text
            direcao = ponto.find('Direcao').text
            status = ponto.find('Status').text
            
            data_key = (navio_id, timestamp, latitude, longitude)
            if data_key not in data_set:
                # Adicionar ao conjunto
                data_set.add(data_key)
                # Adicionar à lista de dados
                data.append([navio_id, navio_nome, timestamp, latitude, longitude, velocidade, direcao, status])
    
    data = []

    # Iterar pelos arquivos XML no diretório
    for filename in os.listdir(xml_directory):
        if filename.endswith('.xml'):
            xml_file = os.path.join(xml_directory, filename)
            extract_data_from_xml(xml_file)

    # Ordenar os dados pelo NavioID e Timestamp
    data.sort(key=lambda x: (int(x[0]), x[2]))

    # Converter a lista de dados para DataFrame
    df = pd.DataFrame(data, columns=['NavioID', 'Nome', 'Timestamp', 'Latitude', 'Longitude', 'Velocidade', 'Direcao', 'Status'])

    # Salvar o DataFrame como um arquivo CSV
    csv_file = os.path.join(csv_directory, 'dados_navios.csv')
    df.to_csv(csv_file, index=False)

    print(f"Dados salvos em {csv_file}")
