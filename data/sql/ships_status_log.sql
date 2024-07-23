CREATE TABLE Cost_Ship (
   ID_Log INTEGER PRIMARY KEY,
    Name_Ship VARCHAR(100),
    _Date_ DATE,
    Port VARCHAR(100),
    Type_cost VARCHAR(100),
    Value_USD FLOAT,
    _Description_ TEXT,
    Type_Load VARCHAR(100),
    Volume FLOAT,
    Temperature FLOAT,
    Tonnage FLOAT,
    Number_of_Containers INTEGER,
    Type_of_Containers VARCHAR(100),
    Number_of_Vehicles INTEGER,
    Type_of_Vehicles VARCHAR(100),
    ID_Navio INTEGER,
);


   