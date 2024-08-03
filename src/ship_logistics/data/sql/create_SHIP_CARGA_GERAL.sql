CREATE TABLE SHIP_CARGA_GERAL {
  ID integer [primary key, increment]
  ID_TYPE integer [ref: > TYPE_SHIP.ID_TYPE]
  ID_SHIP integer [ref: > SHIP.ID_SHIP]
  DATE_ date
  ID_PORT integer [ref: > PORT.ID_PORT]
  TYPE_COST varchar(255)
  VALUE numeric
  LOAD_NAME varchar(255)
  VOLUME numeric
};
