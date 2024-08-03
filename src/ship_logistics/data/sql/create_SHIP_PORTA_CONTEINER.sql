CREATE TABLE SHIP_PORTA_CONTEINER {
  ID integer [primary key, increment]
  ID_TYPE integer [ref: > TYPE_SHIP.ID_TYPE]
  ID_SHIP integer [ref: > SHIP.ID_SHIP]
  DATE_ date
  ID_PORT integer [ref: > PORT.ID_PORT]
  TYPE_COST varchar(255)
  VALUE numeric
  NUMBER_OF_CONTAINERS numeric
  LOAD_NAME varchar(255)
};