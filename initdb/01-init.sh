#!/bin/bash
set -e
export POSTGRES_PASSWORD=$POSTGRES_PASSWORD;
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
  CREATE USER $DB_USER WITH PASSWORD '$DB_PASSWORD';
  ALTER USER $DB_USER CREATEDB;
  CREATE DATABASE $DB_NAME;
  GRANT ALL PRIVILEGES ON DATABASE $DB_NAME TO $DB_USER;
  ALTER DATABASE $DB_NAME OWNER TO $DB_USER;
  \connect $DB_NAME $DB_USER
  BEGIN;
    CREATE TABLE IF NOT EXISTS event (
      id CHAR(26) NOT NULL CHECK (CHAR_LENGTH(id) = 26) PRIMARY KEY,
	    aggregate_id CHAR(26) NOT NULL CHECK (CHAR_LENGTH(aggregate_id) = 26),
	    event_data JSON NOT NULL,
	    version INT,
	    UNIQUE(aggregate_id, version)
    );
    CREATE INDEX idx_event_aggregate_id ON event (aggregate_id);
  COMMIT;
EOSQL
