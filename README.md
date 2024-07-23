# Data_Science_Project_-_Challenge_2

Data_Science_Project_-_Challenge_2/
├── all_files_py/                        # Scripts Python
│   ├── extract_xml.py
│   ├── extract_xlsx.py
│   ├── ship_union.py
│   ├── ship_id.py
│   ├── csv_column_processor.py
│   └── main.py                          # Script principal
├── all_files/                           # Diretório de entrada de arquivos
│   ├── xml/                             # Subpasta para arquivos XML
│   ├── xlsx/                            # Subpasta para arquivos XLSX
│   └── html/                            # Subpasta para arquivos HTML
├── ship_project/                        # Diretório para arquivos relacionados a navios
│   ├── input/                           # Diretório de entrada para arquivos CSV
│   │   ├── data1.csv
│   │   ├── data2.csv
│   │   └── outros_arquivos.csv          # Outros arquivos CSV
│   ├── output/                          # Diretório de saída para arquivos processados
│   │   ├── ships_status_log.csv         # Arquivo CSV combinado de status de navios
│   │   └── separated_by_ship/           # Subpasta para arquivos separados por navio
│   │       ├── ship1.csv
│   │       ├── ship2.csv
│   │       └── outros_navios.csv
├── data/                                # Dados persistentes do banco de dados e scripts relacionados
│   ├── postgres/                        # Dados do PostgreSQL
│   ├── sql/                             # Diretório para arquivos SQL
│   │   ├── create_tables.sql            # Script para criar tabelas no banco de dados
│   │   └── insert_data.sql              # Script para inserir dados nas tabelas
│   └── scripts/                         # Diretório para scripts de upload de dados para o banco
│       ├── upload_data.py               # Script Python para upload de dados para o banco
├── docker-compose.yml                   # Arquivo Docker Compose
└── README.md                            # Documento explicativo do projeto
