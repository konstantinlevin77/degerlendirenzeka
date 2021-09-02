import os
import psycopg2


class BaseDao:

    def __init__(self):

        self.DATABASE_URL = os.environ['DATABASE_URL']
    
    def execute_query(self,query,parameters=(),does_return=False):

        conn = psycopg2.connect(self.DATABASE_URL, sslmode='require')

        cursor = conn.cursor()

        if not does_return:
            cursor.execute(query,parameters)
            conn.commit()
            conn.close()

        elif does_return:
            cursor.execute(query,parameters)
            results = cursor.fetchall()
            conn.close()
            return results