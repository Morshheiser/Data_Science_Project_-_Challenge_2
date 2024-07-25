import os
import sys
from pathlib import Path
from src.ship_logistics.service.update_volume_ships_refrigerators import update_volume_column
from src.ship_logistics.service.copy_csv_files import copy_csv_files
from src.ship_logistics.service.extract_zip_files import extract_zip_files
from src.ship_logistics.service.extract_xml import process_all_xml_files
from src.ship_logistics.service.extract_xlsx import process_all_xlsx_files
from src.ship_logistics.service.ship_union import combine_csv_files
from src.ship_logistics.service.ship_id import separate_by_ship
from src.ship_logistics.service.translation_files import translate_csv_name 
from src.ship_logistics.service.csv_column_processor import process_column_in_csv
# Nao faz sentido importar essa lista pra ca pra passar como parametro depois
# Vale colocar ela como parametro default na criacao da funcao
from src.ship_logistics.service.create_tables import run_sql_scripts

BASE_PATH = Path(__file__).parent / "data"
SOURCE_DIRECTORY = BASE_PATH / "zip"
ALL_FILES_DIRECTORY = BASE_PATH / "all_files"
INPUT_DIRECTORY = BASE_PATH / "csv"/ "input"
OUTPUT_DIRECTORY = BASE_PATH / "csv" / "output"
SQL_DIRECTORY =  BASE_PATH / "sql"
FILENAME = 'navio_frigorifico.csv'

print(BASE_PATH)

def main():
    try:
        # Processa todos os arquivos XML e XLSX
        extract_zip_files(SOURCE_DIRECTORY, ALL_FILES_DIRECTORY)
        process_all_xml_files(ALL_FILES_DIRECTORY, INPUT_DIRECTORY)
        process_all_xlsx_files(ALL_FILES_DIRECTORY, INPUT_DIRECTORY)
        copy_csv_files(ALL_FILES_DIRECTORY, INPUT_DIRECTORY)
        update_volume_column(INPUT_DIRECTORY, FILENAME)

        # Executa os scripts SQL para criar as tabelas no banco de dados
        run_sql_scripts()

        print("Processamento concluído com sucesso!")

    except Exception as e:
        print(f"Ocorreu um erro durante o processamento: {str(e)}")

if __name__ == "__main__":
    main()
