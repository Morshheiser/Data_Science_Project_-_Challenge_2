
CREATE TABLE SHIP (
    ID_SHIP serial PRIMARY KEY,
    SHIP_NAME VARCHAR(255) UNIQUE NOT NULL,
    ID_TYPE INTEGER REFERENCES TYPE_SHIP(ID_TYPE)
);
