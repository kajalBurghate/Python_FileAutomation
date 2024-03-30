from sys import *
import os

def DirectoryTravel(DirName):
    print("We are going to scan the Directory :",DirName)

    for foldername, subfoldername, filename in os.walk(DirName): #display main folder and its files
        print("Current Directory Name :", foldername)

        for subname in subfoldername:  #display subfolder and its files
            print("Subfolder name is :",subname)

        for fname in filename:   #display files within folder within folder
            print(fname)

def main():
    print("------------Automation Script________________")

    print("Automation Script name :", argv[0])

    if(len(argv) != 2):
        print("Invalid number of argumnets")
        exit()

        if(argv[1] == "-h" or argv[1] == "-H"):   #flag for display help
            print("This Automation script is perform File Automations")
            exit()

        elif (argv[1]== "-u"or argv[1] == "-U"):   #flag for diaplay the usage of script
            print("Usage : Name_Of_Script First_Argument ")
            print("Example : Demo.py Python")  # python folder name
            exit()

        else:
            print("There is no such option to handle..")
            exit()
 

    else: 
        DirectoryTravel(argv[1])

if __name__ == "__main__":
    main() 