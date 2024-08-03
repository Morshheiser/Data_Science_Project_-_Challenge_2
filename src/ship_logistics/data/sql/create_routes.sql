CREATE TABLE ROUTES {
  ID_ROUTE integer [primary key]
  ID_PORT_ORIGIN integer [ref: > PORT.ID_PORT]
  ID_PORT_DESTINATION integer [ref: > PORT.ID_PORT]
  DISTANCE numeric
  AVERAGE_TIME numeric
};
