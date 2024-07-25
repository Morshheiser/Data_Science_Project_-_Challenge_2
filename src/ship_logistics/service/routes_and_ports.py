import pandas as pd

caminho_arquivo = r'C:\Users\morsh\Desktop\Casa DIgital\projeto de ciencias de dados\Desafio_Log\arquivos tratados\rotas.csv'
# Carregar o arquivo CSV para um DataFrame
try:
    df = pd.read_csv(caminho_arquivo)
    print(df)  # Exibe todas as linhas e colunas do DataFrame carregado
except PermissionError as e:
    print(f'Erro de permissão ao acessar o arquivo: {e}')