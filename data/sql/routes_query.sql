CREATE TABLE Routes (
    ID_Route SERIAL PRIMARY KEY,
    Port_Origin_ID INTEGER,
    Port_Destiny_ID INTEGER,
    Distance FLOAT,
    Time_Average FLOAT,
    FOREIGN KEY (Port_Origin_ID) REFERENCES Port_Name(ID_Port),
    FOREIGN KEY (Port_Destiny_ID) REFERENCES Port_Name(ID_Port)
);
