import numpy as np 
import pandas as pd
import os  
import face_detection_function
def title_bar():
    os.system('cls')  # for windows

    # title of the program

    print("\t**********************************************")
    print("\t***** Face Detection *****")
    print("\t**********************************************")

def mainMenu():
    title_bar()
    print()
    print(10 * "*", "WELCOME to Matellio Smart Door Lock System", 10 * "*")
    print("[1] Open The Door")
    print("[2] Are You Visitor")
    print("[6] Quit")

    while True:
        try:
            choice = int(input("Enter Choice: "))

            if choice == 1:
                detectFace()
                break
            elif choice==2:
                print("Conntecting Admin.... ")
                break
            elif choice == 6:
                print("Thank You")
                break
            else:
                print("Invalid Choice. Enter 1-4")
                mainMenu()
        except ValueError:
            print("Invalid Choice. Enter 1-4\n Try Again")
        exit


# ---------------------------------------------------------
# calling the camera test function from check camera.py file


def detectFace():
    fc=face_detection_function.face_count()
    print("Detected Face Count is {}".format(fc))
    if fc==1:
        print("Please wait for face verification")
    else:
        print("Sorry!! system detected multiple face at same time")
    #key = input("Enter any key to return main menu")
    #mainMenu()
    
mainMenu()