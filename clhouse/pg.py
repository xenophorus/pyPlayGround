from psycopg2 import OperationalError, connect
from psycopg2.extensions import connection

def create_connection(db_name:str, db_user:str, db_password:str, db_host:str, db_port:int) -> connection:
    conn = None
    try:
        conn = connect(database=db_name,
                       user=db_user,
                       password=db_password,
                       host=db_host,
                       port=db_port)
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:(
        print(f"The error '{e}' occurred"))
    return conn

def execute_query(conn, query):
    # connection.autocommit = True
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        conn.commit()
        print("Query executed successfully")
        cursor.close() # закрываем курсор
    except OperationalError as e:
        cursor.close() # закрываем курсор
        print(f"The error '{e}' occurred")

connection = create_connection(
    "dns_tt",
    "alex",
    "21779835",
    "127.0.0.1",
    5432)

create_users_table = """
CREATE TABLE IF NOT EXISTS users ( id SERIAL PRIMARY KEY,
name TEXT NOT NULL, 
age INTEGER,
gender TEXT,
nationality TEXT
)
"""

with connection as conn:
    execute_query(conn, create_users_table)

users = [
    ("James", 25, "male", "USA"),
    ("Leila", 32, "female", "France"),
    ("Brigitte", 35, "female", "England"),
    ("Mike", 40, "male", "Denmark"),
    ("Elizabeth", 21, "female", "Canada"),
]

user_records = ", ".join(["%s"] * len(users))

insert_query = f"INSERT INTO users (name, age, gender, nationality) VALUES {user_records}"

cursor = connection.cursor()

cursor.execute(insert_query, users)
connection.commit()

cursor.close()


