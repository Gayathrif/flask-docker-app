from flask import Flask
import psycopg2
import os

app = Flask(__name__)

# Database connection details
db_host = os.getenv("DB_HOST", "db")
db_name = os.getenv("DB_NAME", "testdb")
db_user = os.getenv("DB_USER", "user")
db_password = os.getenv("DB_PASSWORD", "password")

def get_db_connection():
    return psycopg2.connect(host=db_host, database=db_name, user=db_user, password=db_password)

@app.route('/')
def home():
    return "Hello, Gayathri C Nair & Register Number 2022BCD0011"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
