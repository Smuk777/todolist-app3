import psycopg2
from dotenv import load_dotenv

import os

load_dotenv()

def get_conexao():
    conn = psycopg2.connect(
        dbname = os.getenv('DB_DATABASE'),
        user = os.getenv('DB_USER'),
        password = os.getenv('DB_PASSWORD'),
        host = os.getenv('DB_HOST'),
        port = os.getenv('DB_POST')
    )
    return conn