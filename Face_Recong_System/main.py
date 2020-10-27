import os  # accessing the os functions
import check_camera
import Capture_Image
import Train_Image
import Recognize


# creating the title bar function

def title_bar():
    os.system('cls')  # for windows

    # title of the program

    print("\t**********************************************")
    print("\t***** Smart Door Lock System : Image Collection and Training *****")
    print("\t**********************************************")


# creating the user main menu function

def mainMenu():
    title_bar()
    print()
    print(10 * "*", "Admin Pannel ", 10 * "*")
    print("[1] Camera SetUp")
    print("[2] Capture Image Sample ")
    print("[3] Train Images")
    print("[4] Recognize ")
    print("[5] Report Genration")
    print("[6] Quit")

    while True:
        try:
            choice = int(input("Enter Choice: "))

            if choice == 1:
                checkCamera()
                break
            elif choice == 2:
                CaptureFaces()
                break
            elif choice == 3:
                Trainimages()
                break
            elif choice == 4:
                RecognizeFaces()
                break
            elif choice == 5:
                os.system("py automail.py")
                break
                mainMenu()
            elif choice == 6:
                print("Thank You")
                break
            else:
                print("Invalid Choice. Enter 1-4")
                mainMenu()
        except ValueError:
            print("Invalid Choice. Enter 1-4\n Try Again")
        exit


# ---------------------------------------------------------4
# calling the camera test function from check camera.py file


def checkCamera():
    check_camera.camer()
    key = input("Enter any key to return main menu")
    mainMenu()


# --------------------------------------------------------------
# calling the take image function form capture image.py file

def CaptureFaces():
    Capture_Image.takeImages()
    key = input("Enter any key to return main menu")
    mainMenu()


# -----------------------------------------------------------------
# calling the train images from train_images.py file

def Trainimages():
    Train_Image.TrainImages()
    key = input("Enter any key to return main menu")
    mainMenu()


# --------------------------------------------------------------------
# calling the recognize_attendance from recognize.py file

def RecognizeFaces():
    Recognize.recognize_attendence()
    key = input("Enter any key to return main menu")
    mainMenu()


# ---------------main driver ------------------
mainMenu()
