import pandas as pd
import os

#Lista todos os arquivos .xlsx em um diretório.
def list_xlsx_files(directory):
    return [f for f in os.listdir(directory) if f.endswith('.xlsx')]

#Processa todos os arquivos .xlsx em um diretório, converte cada planilha para CSV.
def process_all_xlsx_files(directory, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    files = list_xlsx_files(directory)
    
    for file in files:
        file_path = os.path.join(directory, file)
        df = pd.read_excel(file_path)  # Lê a primeira planilha por padrão
        output_file = os.path.join(output_directory, os.path.splitext(file)[0] + '.csv')
        df.to_csv(output_file, index=False)
        print(f'Saved {output_file}')



