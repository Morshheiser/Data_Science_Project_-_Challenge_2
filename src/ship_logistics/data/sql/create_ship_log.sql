-- Remove a tabela se ela já existir
DROP TABLE IF EXISTS ship_logs;

-- Cria a nova tabela
CREATE TABLE ship_logs (
    id_log SERIAL PRIMARY KEY,
    SHIP_NAME VARCHAR(255),
    DATE_ DATE,
    Porto VARCHAR(255),
    TYPE_COST VARCHAR(255),
    VALUE DECIMAL(10, 2),
    Descrição TEXT,
    LOAD_NAME VARCHAR(255),
    VOLUME DECIMAL(10, 2),
    TEMP DECIMAL(5, 2),
    WEIGHT_TONNAGE DECIMAL(10, 2),
    NUMBER_OF_CONTAINERS INT,
    NUMBER_OF_VEHICLES INT
);
