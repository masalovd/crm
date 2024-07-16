#!/bin/bash

# Load environment variables from .env file
if [ ! -f .env ]; then
  echo "Error: .env file not found."
  exit 1
fi

export $(cat .env | xargs)

# Function to create database and user
create_db_user() {
  sudo su postgres <<EOF
psql -c "CREATE DATABASE $DB_NAME;"
psql -c "CREATE USER $DB_USERNAME WITH PASSWORD '$DB_PASSWORD';"
psql -c "ALTER DATABASE $DB_NAME OWNER TO $DB_USERNAME;"
EOF
  echo "Database '$DB_NAME' and user '$DB_USERNAME' created successfully."
}

# Function to drop database and user
drop_db_user() {
  sudo su postgres <<EOF
psql -c "REVOKE ALL PRIVILEGES ON DATABASE $DB_NAME FROM $DB_USERNAME;"
psql -c "DROP DATABASE $DB_NAME;"
psql -c "DROP USER $DB_USERNAME;"
EOF
  echo "Database '$DB_NAME' and user '$DB_USERNAME' dropped successfully."
}

# Parse command-line arguments
if [ "$1" == "create" ]; then
  create_db_user
elif [ "$1" == "delete" ]; then
  drop_db_user
else
  echo "Usage: $0 [create|delete]"
  exit 1
fi
