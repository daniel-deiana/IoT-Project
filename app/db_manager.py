from database import Database

class dbManager:
    database = Database()
    
    def store_sensor_data(self,node,topic,value,timestamp):
        database = Database()
        database.connect_db()

        querystring = " INSERT INTO sensor_data(`sensor_id`, `type`, `value`, `timestamp`,`wagon`) VALUES (%s,%s,%s,%s,%s);"
        parameters = (node, topic, value, timestamp, 1)
        database.execute_query(querystring,parameters,0)

    def get_actuator_ip(self,sensor_id,atype):
        database = Database()
        database.connect_db()
        querystring = " SELECT A.ip_address, A.state  FROM actuator A inner join wagon W on W.wagon_id = A.wagon INNER JOIN sensor_data D on D.wagon = W.wagon_id WHERE D.sensor_id = %s and A.type = %s;"
        result = database.execute_query(querystring,(sensor_id,atype),0)
        return result

    def set_actuator_state(self,ip,state):
        database=Database()
        database.connect_db()
        querystring= "UPDATE iot.actuator A SET A.state = %s WHERE A.ip_address = %s;"
        parameters = (state,ip)
        result = database.execute_query(querystring,parameters,0)
        return result

    def get_wagon_status(self,wagon_index):
        database = Database()
        database.connect_db()
        querystring = "SELECT W.wagon_id, A.type, A.state FROM iot.wagon W inner join iot.actuator A WHERE wagon_id = %s"
        parameters = (wagon_index)
        result = database.execute_query(querystring,parameters,1)
        return result
    
    def get_wagon_thresholds(self,wagon_index):
        database = Database()
        database.connect_db()
        querystring = "select W.max_br_temp, W.max_consumption from iot.wagon W where W.wagon_id = %s"
        parameters = (wagon_index)
        result = database.execute_query(querystring,parameters,0)
        return result
    
    def set_wagon_thresholds(self,max_temp,max_consumption,wagon_index):
        database = Database()
        database.connect_db()
        querystring = "update iot.wagon W set W.max_br_temp = %s, W.max_consumption = %s where W.wagon_id = %s"    
        parameters = (max_temp,max_consumption,wagon_index)
        result = database.execute_query(querystring, parameters,0)
        return result
    