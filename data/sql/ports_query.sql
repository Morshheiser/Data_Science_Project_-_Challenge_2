CREATE TABLE Port_Name (
    ID_Port SERIAL PRIMARY KEY,
    Name_Port VARCHAR(100) UNIQUE,
    Country VARCHAR(100),
    Type_load VARCHAR(100),
    Latitude FLOAT,
    Longitude FLOAT
);
