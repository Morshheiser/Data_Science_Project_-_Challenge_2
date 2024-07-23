import os
import sys

# Adiciona o diretório 'all_py_files' ao sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), 'all_py_files'))

try:
    from copy_csv_files import copy_csv_files
    from extract_zip_files import extract_zip_files
    from extract_xml import process_all_xml_files
    from extract_xlsx import process_all_xlsx_files
    from ship_union import combine_csv_files
    from ship_id import separate_by_ship
    from translation_files import translate_csv_name 
    from csv_column_processor import process_column_in_csv
except ImportError as e:
    print(f"Erro ao importar os módulos: {e}")
    sys.exit(1)

def main():
    # Diretório onde procurar arquivos ZIP
    source_directory = r'C:\Users\morsh\Desktop\Casa DIgital\Data_Science_Project_-_Challenge_2\zip_files'
    # Diretório onde extrair os arquivos
    destination_directory = r'C:\Users\morsh\Desktop\Casa DIgital\Data_Science_Project_-_Challenge_2\all_files'

    # Executa a função de extração
    extract_zip_files(source_directory, destination_directory)

    # Diretório de entrada contendo os arquivos XML e XLSX
    input_directory = destination_directory
    # Diretório de entrada para os arquivos CSV
    input_directory_2 = r'C:\Users\morsh\Desktop\Casa DIgital\Data_Science_Project_-_Challenge_2\ship_project\input_csv'
    # Diretório de saída para os arquivos CSV
    output_directory = r'C:\Users\morsh\Desktop\Casa DIgital\Data_Science_Project_-_Challenge_2\ship_project\output_csv'

    # Verifica se os diretórios existem, caso contrário, cria-os
    if not os.path.exists(input_directory_2):
        os.makedirs(input_directory_2)
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    try:
        # Processa todos os arquivos XML e XLSX
        process_all_xml_files(input_directory, input_directory_2)
        process_all_xlsx_files(input_directory, input_directory_2)
        copy_csv_files(input_directory, input_directory_2)
        combine_csv_files(input_directory_2, output_directory)
        separate_by_ship(os.path.join(output_directory, 'ships_status_log.csv'), output_directory)
        translate_csv_name(input_directory_2, output_directory)  
        print("Processamento concluído com sucesso!")

    except Exception as e:
        print(f"Ocorreu um erro durante o processamento: {str(e)}")

if __name__ == "__main__":
    main()
