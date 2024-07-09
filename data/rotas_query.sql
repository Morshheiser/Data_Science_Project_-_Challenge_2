-- Dropa a tabela se ela já existir
DROP TABLE IF EXISTS Rota;

-- Cria a tabela Rota
CREATE TABLE Rota (
    ID_Rota SERIAL PRIMARY KEY,
    Porto_Origem VARCHAR(100),
    Porto_Destino VARCHAR(100),
    Distancia FLOAT,
    Tempo_Medio FLOAT
);

-- Copia os dados do CSV (rotar.csv) para a tabela Rota
COPY Rota (Porto_Origem, Porto_Destino, Distancia, Tempo_Medio)
FROM 'C:/Users/morsh/Desktop/Casa DIgital/Data_Science_Project_-_Challenge_2/all_files/ship_project/rotas.csv' DELIMITER ',' CSV HEADER;
