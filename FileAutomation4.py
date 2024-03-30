from sys import *
import os
import time 

def DirectoryTravel(DirName):
    print("We are going to scan the Directory :",DirName)

    total_size = 0

    for foldername, subfoldername, filename in os.walk(DirName): #display main folder and its files
       #for foldername, subfoldername, filename in os.walk(DirName):
        for fname in filename:
            print(fname, ":", os.path.getsize(foldername+"/"+fname), "bytes")

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
        starttime = time.time()
        DirectoryTravel(argv[1])
        endtime = time.time()

        print("The Script took time to execute as : ", endtime-starttime)

if __name__ == "__main__":
    main() 