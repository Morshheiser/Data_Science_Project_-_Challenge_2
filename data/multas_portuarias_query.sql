CREATE TABLE MultasNavios (
    ID_Multa SERIAL PRIMARY KEY,
    ID_Navio INTEGER,
    Porto VARCHAR(50),
    Data_Multa TIMESTAMP,
    Motivo VARCHAR(100),
    Valor NUMERIC(15, 2)
);
