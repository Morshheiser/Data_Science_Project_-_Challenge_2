CREATE TABLE Fees_Ports (
    Name_Port VARCHAR(100) UNIQUE,
    Rate_type VARCHAR(50),
    Value_per_ship FLOAT,
    Value_Per_Tonne FLOAT,
    ID_Port INTEGER,
    FOREIGN KEY (ID_Port) REFERENCES Port_Name(ID_Port)
);
