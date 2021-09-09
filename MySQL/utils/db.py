import mysql.connector
import json
import os

class Db():

    def execute(self, query, params=None):
        conn = None
        result = None

        try:             
            conn =  mysql.connector.connect(
                host=os.environ.get('host'),
                port=os.environ.get('port'),
                user=os.environ.get('user'),
                passwd=os.environ.get('pass'),
                database=os.environ.get('schema')
                )
            #print(conn)
            cursor = conn.cursor(dictionary=True)

            cursor.execute(query, params)

            result = json.loads(json.dumps(cursor.fetchall(), default=str,sort_keys=True))
            
            cursor.close()
            conn.close()
        except (Exception) as error:
            print(error)

        finally:
            if conn is not None:
                conn.close()

        return result
