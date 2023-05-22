#Database classs

import pymysql.cursors


class Database:
    connection = None

    def __init__(self):
        print("init database")

    def connect_db(self):
        if self.connection is not None:
            return self.connection
        else:
            self.connection = pymysql.connect(host="localhost",
                                              user='root',
                                              password="root",
                                              database="iot",
                                              cursorclass=pymysql.cursors.DictCursor)
            return self.connection
    
    # execute a query on database
    def execute_query(self, querystring, parameters):

        with self.connection:
            with self.connection.cursor() as cursor:
                cursor.execute(querystring,parameters)
                result = cursor.fetchone();
        
            self.connection.commit();

        return result



