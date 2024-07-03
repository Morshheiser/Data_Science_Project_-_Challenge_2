import os
import pandas as pd

# Função que formata os valores monetários
def formatar_valor_monetario(valor):
    try:
        # Verifica se o valor é um número (float ou int)
        valor = float(valor)
        # Formata o valor como um valor monetário sem símbolo de moeda
        return "{:,.2f}".format(valor)
    except ValueError:
        return valor

# Função que processa a coluna 'Valor (USD)' em um DataFrame e formata os valores monetários
def process_value_column(df):
    column_name = 'Valor (USD)'
    # Verifica se a coluna está presente no DataFrame
    if column_name in df.columns:
        # Aplica a formatação monetária a cada valor na coluna
        df[column_name] = df[column_name].apply(formatar_valor_monetario)
        return df
    else:
        print(f'A coluna "{column_name}" não está presente no DataFrame.')
        return df

# Função para percorrer arquivos CSV no diretório e aplicar a função de processamento
def process_column_in_csv(directory):
    try:
        # Lista todos os arquivos CSV no diretório
        csv_files = [file for file in os.listdir(directory) if file.endswith('.csv')]

        for csv_file in csv_files:
            try:
                file_path = os.path.join(directory, csv_file)

                # Carrega o arquivo CSV em um DataFrame
                df = pd.read_csv(file_path)

                # Processa a coluna 'Valor (USD)' no DataFrame
                df = process_value_column(df)

                # Salva as alterações de volta no arquivo CSV original
                df.to_csv(file_path, index=False)
                print(f'Arquivo atualizado: {csv_file}')

            except Exception as e:
                print(f'Ocorreu um erro ao processar o arquivo {csv_file}: {str(e)}')

    except Exception as e:
        print(f'Ocorreu um erro ao listar arquivos no diretório {directory}: {str(e)}')


