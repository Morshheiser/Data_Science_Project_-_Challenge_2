CREATE TABLE Ship_Data (
    Ship_ID INTEGER,
    Name_Ship VARCHAR(50) UNIQUE,
    Time_stamp TIMESTAMP,
    Latitude FLOAT,
    Longitude FLOAT,
    Speed FLOAT,
    Direction FLOAT,
    Status_Ship VARCHAR(50)
);
