import psycopg2
import os

DATABASE_URL = os.environ["DATABASE_URL"]

conn = psycopg2.connect(DATABASE_URL,sslmode='require')
cursor = conn.cursor()

cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS questions 
        (id INT GENERATED ALWAYS AS IDENTITY,
        question_text VARCHAR NOT NULL,
        PRIMARY KEY(id)
        );
        """)

cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS answers(
        id INT GENERATED ALWAYS AS IDENTITY,
        question_id INT NOT NULL,
        answer VARCHAR NOT NULL,
        PRIMARY KEY(id),
        CONSTRAINT fk_answer FOREIGN KEY(question_id) REFERENCES questions(id)
        );
        """)

conn.commit()