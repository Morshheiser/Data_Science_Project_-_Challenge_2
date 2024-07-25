import os
import shutil

def copy_csv_files(source_directory, destination_directory):
    """
    Copia todos os arquivos CSV do diretório de origem para o diretório de destino.
    
    :param source_directory: Caminho do diretório de origem.
    :param destination_directory: Caminho do diretório de destino.
    """
    # Verifica se o diretório de destino existe, se não, cria-o
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)
    
    # Itera sobre os arquivos no diretório de origem
    for filename in os.listdir(source_directory):
        # Verifica se o arquivo é um CSV
        if filename.lower().endswith('.csv'):
            src_path = os.path.join(source_directory, filename)
            dest_path = os.path.join(destination_directory, filename)
            # Copia o arquivo para o diretório de destino
            shutil.copy(src_path, dest_path)
            print(f"Arquivo CSV copiado: {filename}")
