import os
import zipfile

def extract_zip_files(source_dir, dest_dir):
    """
    Procura arquivos ZIP em um diretório e extrai seu conteúdo para a pasta de destino.
    
    :param source_dir: Diretório onde procurar arquivos ZIP.
    :param dest_dir: Diretório onde extrair o conteúdo dos arquivos ZIP.
    """
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
        print(f"Diretório de destino criado: {dest_dir}")
    
    # Percorre todos os arquivos no diretório de origem
    for item in os.listdir(source_dir):
        # Cria o caminho completo para o item
        item_path = os.path.join(source_dir, item)
        
        # Verifica se o item é um arquivo ZIP
        if os.path.isfile(item_path) and item.lower().endswith('.zip'):
            try:
                # Extrai o arquivo ZIP
                with zipfile.ZipFile(item_path, 'r') as zip_ref:
                    zip_ref.extractall(dest_dir)
                    print(f"Arquivo ZIP extraído: {item_path}")
            except Exception as e:
                print(f"Erro ao extrair {item_path}: {e}")

# # Diretório onde procurar arquivos ZIP
# source_directory = r'C:\Users\morsh\Desktop\Casa DIgital\Data_Science_Project_-_Challenge_2\data\zip'
# # Diretório onde extrair os arquivos
# destination_directory = r'C:\Users\morsh\Desktop\Casa DIgital\Data_Science_Project_-_Challenge_2\data\all_files'

# # Executa a função de extração
# extract_zip_files(source_directory, destination_directory)
