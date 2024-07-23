CREATE TABLE Routes (
    ID_Route SERIAL PRIMARY KEY,
    Port_Origin VARCHAR(100),
    Port_Destiny VARCHAR(100),
    Distance FLOAT,
    Time_Average FLOAT
);
