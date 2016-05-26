DROP TABLE IF EXISTS resources;
CREATE TABLE resources
(
  id smallint unsigned NOT NULL auto_increment,
  requestDate date NOT NULL,
  requestSummary mediumtext NOT NULL,
  organization text NOT NULL,
  address text NOT NULL,
  lattitude varchar(255) NOT NULL,
  longitude varchar(255) NOT NULL,
  priority smallint unsigned NOT NULL,
  
  PRIMARY KEY (id)
);
