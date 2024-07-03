import os
from extract_xml import process_all_xml_files
from extract_xlsx import process_all_xlsx_files
from ship_union import combine_csv_files
from ship_id import separate_by_ship
from csv_column_processor import  process_column_in_csv

def main():
    # Diretório de entrada contendo os arquivos XML
    input_directory = r'C:\Users\morsh\Desktop\Casa DIgital\projeto de ciencias de dados\Desafio_Log'

    # Diretório de saída para os arquivos CSV
    output_directory = r'C:\Users\morsh\Desktop\Casa DIgital\projeto de ciencias de dados\Desafio_Log\ship_project'

    try:
        # Processa todos os arquivos XML e XLSX
        process_all_xml_files(input_directory, output_directory)
        process_all_xlsx_files(input_directory, output_directory)
        
        # Diretório onde os arquivos CSV foram salvos
        csv_directory = output_directory
        process_column_in_csv(input_directory)
        # Combina todos os arquivos CSV
        combine_csv_files(csv_directory)
        
        # Separa os arquivos CSV combinados por navio
        separate_by_ship(os.path.join(csv_directory, 'ships_status_log.csv'), output_directory)
        
        print("Processamento concluído com sucesso!")
    
    except Exception as e:
        print(f"Ocorreu um erro durante o processamento: {str(e)}")

if __name__ == "__main__":
    main()
