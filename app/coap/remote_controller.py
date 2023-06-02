# Remote controller for CoAP actuators written in python

# Test - Issuing a request to a CoAP server in the WSN

from coapthon.client.helperclient import HelperClient 
from coapthon.utils import parse_uri

class coapActuatorHandler:

    port = 5683
    path = ""
    def __init__ (self,res):
        self.path = res


    def cooling_actuator_send(self, address, command):
        print("coapActuatoHandler - sending command \n")
        client = HelperClient(server=(address, self.port))
        response = client.post(self.path,command)
        if (response == None):
            print("coapActuatorHandler - no response from actuator")
            return

        print(response.pretty_print())
        client.stop()
        return response

