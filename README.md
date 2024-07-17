# CRM App

A basic CRM built using pure Django 🦄

## Installation Guide

### Step 1: Install Python 3.12
Download and install Python 3.12 from the official website:

[Download Python 3.12](https://www.python.org/downloads/)

### Step 2: Install Poetry

Follow the instructions on the Poetry website to install Poetry:

[Install Poetry](https://python-poetry.org/docs/)

### Step 3: Create a repository in which the project files will be placed

```bash
mkdir ./path/to/repository/
```

And go there:

```bash
cd ./path/to/repository/
```


### Step 4: Create and Activate a Virtual Environment

Create a virtual environment by running the following command:
```bash
python -m venv .venv
```

Activate the virtual environment:

- Windows:

```bash
.venv\Scripts\activate
```

- macOS and Linux:
```bash
source .venv/bin/activate
```

### Step 5: Initialize Git Repository

Initialize the project repository as a Git repository:

```bash
git init
```

### Step 6: Clone the Project

Clone the project repository from GitHub:

```bash
git clone git@github.com:masalovd/crm-app.git
```

And go there:
```bash
cd ./crm_app
```

### Step 7: Set Up PostgreSQL Database

> Before running the script to configure the database, make sure you have psql installed.

Add the database name, username and password in the .env file:

```bash
# ./crm_app/.env

...

DB_NAME=<db-name>
DB_USERNAME=<username-of-db-user>
DB_PASSWORD=<password-for-user>
DB_HOSTNAME=localhost
DB_PORT=5432
```

And then run the script:

```bash
./db_conf.sh create
```

### Step 8: Install Dependencies and Pre-commit Hooks

Run the following command to install the dependencies, apply the migrations, and set up pre-commit hooks:

```bash
make update
```

### Step 9: Generate Django Secret Key

Generate a Django SECRET_KEY using [Djecrety](https://djecrety.ir/) and add it to your .env file.

```bash
# ./crm_app/.env

SECRET_KEY="your-secret-key"
...
```

### Step 10: Run the Server

Start the server with the following command:

```bash
make run-server
```
