from threading import Thread
import os


def handle_command(cmd):

    if cmd == "get":
        print("get command invocated")
    else:
        print("unknown command")

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
