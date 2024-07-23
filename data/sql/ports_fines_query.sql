CREATE TABLE Fines_Ships (
    ID_Fine SERIAL PRIMARY KEY,
    ID_Ship INTEGER,
    Port VARCHAR(50),
    Date_fine TIMESTAMP,
    Reason VARCHAR(100),
    Fine_Value NUMERIC(15, 2),
    ID_Port INTEGER,
    FOREIGN KEY (ID_Port) REFERENCES Port_Name(ID_Port)
);
