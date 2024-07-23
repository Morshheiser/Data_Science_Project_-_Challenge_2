import os
import shutil

# Define o mapeamento de tradução dos nomes dos arquivos
file_translation_map = {
    'dados_navios.csv': 'ship_data.csv',
    'multas_portuarias_atualizado.csv': 'port_fines_updated.csv',
    'portos.csv': 'ports.csv',
    'rotas.csv': 'routes.csv',
    'taxas_portuarias.csv': 'port_fees.csv',
    # Adicione mais traduções conforme necessário
}

def translate_csv_name(input_directory, output_directory):
    try:
        # Verifica se o diretório de saída existe, se não, cria-o
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        # Lista todos os arquivos CSV no diretório de entrada
        csv_files = [file for file in os.listdir(input_directory) if file.endswith('.csv')]

        for csv_file in csv_files:
            # Verifica se o nome do arquivo está no mapeamento de tradução
            if csv_file in file_translation_map:
                try:
                    # Define o caminho completo para o arquivo CSV
                    file_path = os.path.join(input_directory, csv_file)
                    
                    # Define o nome traduzido do arquivo
                    translated_file_name = file_translation_map[csv_file]
                    
                    # Define o caminho completo para o arquivo de saída com o nome traduzido
                    output_file = os.path.join(output_directory, translated_file_name)

                    # Copia o arquivo para o novo diretório com o nome traduzido
                    shutil.copy(file_path, output_file)
                    print(f'Arquivo {csv_file} copiado e salvo como {translated_file_name} em {output_directory}')
                
                except Exception as e:
                    print(f'Ocorreu um erro ao processar o arquivo {csv_file}: {str(e)}')
            else:
                print(f'Arquivo {csv_file} não está no mapeamento de tradução e foi ignorado.')

    except Exception as e:
        print(f'Ocorreu um erro ao listar arquivos no diretório {input_directory}: {str(e)}')


