import os
import sys

# Adiciona o diretório 'all_py_files' ao sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), 'all_py_files'))

try:
    from update_volume_ships_refrigerators import update_volume_column
    from copy_csv_files import copy_csv_files
    from extract_zip_files import extract_zip_files
    from extract_xml import process_all_xml_files
    from extract_xlsx import process_all_xlsx_files
    from ship_union import combine_csv_files
    from ship_id import separate_by_ship
    from translation_files import translate_csv_name 
    from csv_column_processor import process_column_in_csv
    from create_tables import run_sql_scripts
    from create_tables import sql_files
except ImportError as e:
    print(f"Erro ao importar os módulos: {e}")
    sys.exit(1)

def main():
    # Diretório onde procurar arquivos ZIP
    source_directory = r'C:\Users\morsh\Desktop\Casa DIgital\Data_Science_Project_-_Challenge_2\zip_files'
    # Diretório onde extrair os arquivos
    destination_directory = r'C:\Users\morsh\Desktop\Casa DIgital\Data_Science_Project_-_Challenge_2\all_files'

    # Diretório de entrada contendo os arquivos XML e XLSX
    input_directory = destination_directory
    # Diretório de entrada para os arquivos CSV
    input_directory_2 = r'C:\Users\morsh\Desktop\Casa DIgital\Data_Science_Project_-_Challenge_2\ship_project\input_csv'
    # Diretório de saída para os arquivos CSV
    output_directory = r'C:\Users\morsh\Desktop\Casa DIgital\Data_Science_Project_-_Challenge_2\ship_project\output_csv'
    # Defina o diretório e o nome do arquivo
    file_name = 'navio_frigorifico.csv'
    # Diretório onde os scripts SQL estão armazenados
    sql_scripts_directory = r'C:\Users\morsh\Desktop\Casa DIgital\Data_Science_Project_-_Challenge_2\data\sql'

    # Verifica se os diretórios existem, caso contrário, cria-os
    if not os.path.exists(input_directory_2):
        os.makedirs(input_directory_2)
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    if not os.path.exists(sql_scripts_directory):
        os.makedirs(sql_scripts_directory)

    try:
        # Processa todos os arquivos XML e XLSX
        extract_zip_files(source_directory, destination_directory)
        process_all_xml_files(input_directory, input_directory_2)
        process_all_xlsx_files(input_directory, input_directory_2)
        copy_csv_files(input_directory, input_directory_2)
        update_volume_column(input_directory_2, file_name)

        # Executa os scripts SQL para criar as tabelas no banco de dados
        run_sql_scripts(sql_files)

        print("Processamento concluído com sucesso!")

    except Exception as e:
        print(f"Ocorreu um erro durante o processamento: {str(e)}")

if __name__ == "__main__":
    main()
