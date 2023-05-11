vehicleState= "stop"
command = ""
while True:
    command = input(">").lower()
    if command == "start":
        if vehicleState != "start":
            vehicleState = "start"
            print("Car started...")
        else:
            print("Car Already Started!!")
    elif command == "stop":
        if vehicleState != "stop":
            vehicleState = "stop"
            print("Car stopped")
        else:
            print("Car already stopped!!")
    elif command == "help":
        print("""
            start - to start the car 
            stop - to stop the car 
            quit - to quit
        """)
    elif command == "quit":
        break
    else:
        print("Sorry I don't understand that.")



