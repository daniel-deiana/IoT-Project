# Remote controller for CoAP actuators written in python

# Test - Issuing a request to a CoAP server in the WSN

ip = "fd00::201:1:1:1"
port = 5683
server = CoAPServer(ip, port)

try:
    server.listen(10)
except KeyboardInterrupt: 
    print("Server Shutdown") 
    server.close() 
    print("Exiting...")
