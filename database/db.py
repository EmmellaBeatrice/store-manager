import psycopg2
from tables import tables_list

class Database:
    def __init__(self):
        self.db = "store_manager"
        self.user = "postgres"
        self.host = "localhost"
        self.password = "admin"
        self.port = 5432

        try:
            self.connection = psycopg2.connect(dbname=self.db,user=self.user,\
                                password=self.password, host=self.host,port=self.port)
            self.cursor = self.connection.cursor()
            self.connection.autocommit = True
            # print("Connected successfully")
            for query in tables_list:
                self.cursor.execute(query)
        except Exception as error:
            print("Connection Failed {}".format(error))

Database()