from database import Database




class dbManager:
    database = Database()
    
    def store_sensor_data(self,node,topic,value,timestamp):
        database = Database()
        database.connect_db()

        querystring = " INSERT INTO sensor_data(`sensor_id`, `type`, `value`, `timestamp`,`wagon`) VALUES (%s,%s,%s,%s,%s);"
        parameters = (node, topic, value, timestamp, 1)
        database.execute_query(querystring,parameters)
        

    def get_actuator_ip(self,sensor_id):
        database = Database()
        database.connect_db()
        querystring = " SELECT A.ip_address, A.state  FROM actuator A inner join wagon W on W.wagon_id = A.wagon INNER JOIN sensor_data D on D.wagon = W.wagon_id WHERE D.sensor_id = %s;"
        result = database.execute_query(querystring,(sensor_id))
        return result

    def set_actuator_state(self,ip,state):
        database=Database()
        database.connect_db()
        querystring= "UPDATE iot.actuator A SET A.state = %s WHERE A.ip_address = %s;"
        parameters = (state,ip)
        result = database.execute_query(querystring,parameters)
        return result
