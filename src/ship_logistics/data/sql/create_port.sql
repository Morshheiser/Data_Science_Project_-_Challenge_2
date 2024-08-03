CREATE TABLE PORT {
  ID_PORT integer [primary key]
  PORT_NAME varchar(255) [unique]
  COUNTRY varchar(255)
  LATITUDE numeric
  LONGITUDE numeric
};
