CREATE TABLE PORT_COSTS {
  ID_COST integer [primary key, increment]
  ID_PORT integer [ref: > PORT.ID_PORT]
  RATE_TYPE varchar(255)
  VALUE_PER_SHIP numeric
  VALUE_PER_TON numeric
};
