from navigation import Navigation
from WGUPS import WGUPS
import datetime

# Cody Biller ID: 001345937
# WGU C950


print("Welcome to WGUPS Delivery System")
delivery_system = WGUPS()

delivery_system.load_trucks()
total_mileage = delivery_system.get_mileage()
print("Total route mileage is " + str(total_mileage) + " miles")
print("To display status of all packages at a specific time, type 'DISPLAY ALL (HH:MM)")
print("To display status of a specific package at a specific time, type 'DISPLAY (package id) (HH:MM)")

user_input = ""

# collect user input until quit command has been received
class Main:
    while user_input != "q" or "Q":

        # collect input and throw ValueErrors if malformed
        try:
            user_input = input("$: ")
            parsed_input = user_input.split(' ')

            # terminate program if user gives quit input
            if user_input in {'Q', 'q'}:
                exit()

            # give user help manual if prompted
            if user_input in {"Help", "help"}:
                print("To display status of all packages at a specific time, type 'DISPLAY ALL (HH:MM)")
                print("To display status of a specific package at a specific time, type 'DISPLAY (package id) (HH:MM)")
                print("To Exit the Program, type 'Q' or 'q'")

            # handle user input
            if parsed_input[0] == "DISPLAY":
                # if user queries for all packages
                if parsed_input[1] == "ALL":
                    # parse time and supply errors if malformed, otherwise return all packages and their status
                    if parsed_input[2] is not None:
                        parsed_time = parsed_input[2].split(":")
                        print(parsed_time)
                        if len(parsed_time) != 2:
                            raise ValueError
                        if int(parsed_time[0]) not in range(0, 25) or int(parsed_time[1]) not in range(0, 60):
                            print("Invalid Time")
                        else:
                            h = int(parsed_time[0])
                            m = int(parsed_time[1])
                            print("***** Status Check @ " + str(h) + ":" + str(m) + " *****")
                            print("--------------------------------------------")
                            delivery_system.get_all_package_status(datetime.timedelta(hours=h,
                                                                                      minutes=m))
                # handle user input for specific packages, return errors if package number is outside of range,
                # otherwise return specific package information
                elif 0 < int(parsed_input[1]) < 41:
                    if parsed_input[2] is not None:
                        parsed_time = parsed_input[2].split(":")
                        if len(parsed_time) != 2:
                            raise ValueError
                        if int(parsed_time[0]) not in range(0, 25) or int(parsed_time[1]) not in range(0, 60):
                            print("Invalid Time")
                        else:
                            # return specific package information
                            h = int(parsed_time[0])
                            m = int(parsed_time[1])
                            print("***** Status Check @ " + str(h) + ":" + str(m) + " *****")
                            print("--------------------------------------------")
                            delivery_system.get_package_status(int(parsed_input[1]),
                                                               datetime.timedelta(hours=h,
                                                                                  minutes=m))
                else:
                    raise ValueError

        # error handle for invalid input
        except ValueError:
            print("Invalid Input")
            print("Type help for usage information")
        # error handle for malformed input
        except IndexError:
            print("Invalid Input")
