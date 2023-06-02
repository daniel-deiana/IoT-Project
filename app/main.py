from threading import Thread
from db_manager import dbManager
from mqtt.mqtt_collector import change_cons_sensing_freq
import os

def print_cmd_list():
    print("list of commands:")
    print("--- print state: used to get the actual state of actuators inside a wagon")
    print("--- change parameters: used to change threshold values for a certain wagon")
    print("---")


#def handle_print_state():

#def handle_change_parameters():

#def handle


def handle_command(cmd):
    db = dbManager()

    if cmd == "print state":
        wagon_index = input("select wagon >>")
        state = db.get_wagon_status(wagon_index)
        if (state == None):
            print("Remote control - wagon does not exist!")
        else:
            print(state)
    elif cmd == "change parameters":
        wagon_index = input("select wagon >>")
        state = db.get_wagon_status(wagon_index)
        if state == None:
            print("Remote control - wagon does not exist!")
            return
        max_temp = input("Set maximum brake temperature: ")
        max_consumption = input("Set maximum consumption: ")   
        result = db.set_wagon_thresholds(max_temp,max_consumption,wagon_index)
        if result != None:
            print("New thresholds for wagon " + wagon_index + "Set")
    elif cmd == "change energy sensing frequency":
        wagon_index = input("select wagon >>")
        state = db.get_wagon_status(wagon_index)
        if state == None:
            print("Remote control - wagon does not exist!")
            return
        freq = input("insert freq")
        change_cons_sensing_freq(wagon_index,freq)
        
        
    else: 
        print("Command not recognized - Check syntax")
        print_cmd_list()

def main():
    print("##################################################")
    print("#################################################")
    print("Smart railway mantainance - Remote control started")
    print("Command line interface starting")


    try:
        while 1:
            cmd = input("cmd >> ")
            handle_command(cmd)
            

    except KeyboardInterrupt:
        print("\nSmart Railway mantainance - Remote control shutdown")
        print("################################################")
        print("###############################################")

if __name__ == "__main__":
    main()
