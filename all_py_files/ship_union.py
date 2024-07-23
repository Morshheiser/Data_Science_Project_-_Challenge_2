import os
import pandas as pd

def add_unique_id_log(file_path):
    try:
        # Carrega o arquivo CSV
        df = pd.read_csv(file_path)

        # Adiciona uma coluna de id_log com IDs únicos para cada linha
        df['id_log'] = range(1, len(df) + 1)

        # Reordena as colunas para que id_log seja a primeira coluna
        cols = ['id_log'] + [col for col in df.columns if col != 'id_log']
        df = df[cols]

        # Salva o DataFrame de volta ao mesmo arquivo CSV
        df.to_csv(file_path, index=False)
        print(f'Coluna id_log adicionada ao arquivo {file_path}')

    except Exception as e:
        print(f'Ocorreu um erro ao adicionar a coluna id_log: {str(e)}')

def combine_csv_files(input_directory, output_directory):
    try:
        # Lista todos os arquivos CSV no diretório que começam com "navio_"
        csv_files = [file for file in os.listdir(input_directory) if file.startswith('navio_') and file.endswith('.csv')]

        # Lista para armazenar todos os DataFrames carregados
        dfs = []

        # Itera sobre cada arquivo CSV
        for csv_file in csv_files:
            try:
                # Carrega o arquivo CSV
                df = pd.read_csv(os.path.join(input_directory, csv_file))

                # Adiciona o DataFrame à lista
                dfs.append(df)

            except Exception as e:
                print(f'Ocorreu um erro ao processar o arquivo {csv_file}: {str(e)}')

        if dfs:
            try:
                # Concatena todos os DataFrames em um único DataFrame final
                df_final = pd.concat(dfs, ignore_index=True)

                # Ordena por data cronológica e, em seguida, por ordem alfabética de Nome do Navio
                if 'Data' in df_final.columns and 'Nome do Navio' in df_final.columns:
                    df_final.sort_values(by=['Data', 'Nome do Navio'], inplace=True)

                # Define o caminho completo para o arquivo de saída no diretório de saída
                output_file = os.path.join(output_directory, 'ships_status_log.csv')
                
                # Salva o DataFrame final em um único arquivo CSV
                df_final.to_csv(output_file, index=False)
                print(f'Dados combinados foram salvos em {output_file}')

                # Adiciona a coluna id_log ao arquivo final
                add_unique_id_log(output_file)

            except Exception as e:
                print(f'Ocorreu um erro ao combinar os DataFrames: {str(e)}')

        else:
            print('Nenhum dado encontrado para processar.')

    except Exception as e:
        print(f'Ocorreu um erro ao listar arquivos no diretório {input_directory}: {str(e)}')
