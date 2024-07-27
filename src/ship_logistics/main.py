import os
import sys
from pathlib import Path
import logging

# Configura o logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Adiciona o diretório pai ao PYTHONPATH
sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.ship_logistics.service.update_volume_ships_refrigerators import update_volume_column
from src.ship_logistics.service.copy_csv_files import copy_csv_files
from src.ship_logistics.service.extract_zip_files import extract_zip_files
from src.ship_logistics.service.extract_xml import process_all_xml_files
from src.ship_logistics.service.extract_xlsx import process_all_xlsx_files
from src.ship_logistics.service.create_tables import run_sql_scripts
from src.ship_logistics.service.ship_union import combine_csv_files
from src.ship_logistics.service.mapping import process_all_files 
BASE_PATH = Path(__file__).parent / "data"
SOURCE_DIRECTORY = BASE_PATH / "zip"
ALL_FILES_DIRECTORY = BASE_PATH / "all_files"
INPUT_DIRECTORY = BASE_PATH / "csv" / "input"
OUTPUT_DIRECTORY = BASE_PATH / "csv" / "output"
SQL_DIRECTORY = BASE_PATH / "sql"
FILENAME = 'navio_frigorifico.csv'

logging.info(f"Base path: {BASE_PATH}")

def main():
    try:
        logging.info("Iniciando o processamento de arquivos...")

        # Processa todos os arquivos XML e XLSX
        extract_zip_files(SOURCE_DIRECTORY, ALL_FILES_DIRECTORY)
        process_all_xml_files(ALL_FILES_DIRECTORY, INPUT_DIRECTORY)
        process_all_xlsx_files(ALL_FILES_DIRECTORY, INPUT_DIRECTORY)
        copy_csv_files(ALL_FILES_DIRECTORY, INPUT_DIRECTORY)
        update_volume_column(INPUT_DIRECTORY, FILENAME)
        process_all_files(INPUT_DIRECTORY)
        combine_csv_files(INPUT_DIRECTORY, INPUT_DIRECTORY)

        logging.info("Executando scripts SQL para criar tabelas no banco de dados...")
        run_sql_scripts()

        logging.info("Processamento concluído com sucesso!")

    except Exception as e:
        logging.error(f"Ocorreu um erro durante o processamento: {str(e)}")

if __name__ == "__main__":
    main()
