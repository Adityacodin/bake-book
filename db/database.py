import pymysql

class Database:
    def __init__(self,host,port,user,password,database):
        self.connection = pymysql.connect(host = host,port = 3306,user = user,password = password, database = database)
        self.cursor = self.connection.cursor()

    def execute_query(self,query,params = None):
        self.cursor.execute(query,params)
        self.connection.commit()

    def fetch_results(self,query,params = None):
        self.cursor.execute(query,params)
        return self.cursor.fetchall()
    
    def close(self):
        self.cursor.close()
        self.connection.close()
