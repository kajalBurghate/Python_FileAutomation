from sys import *
import os
import time

def DirectoryTravel(DirName, name):
    print("We are going to Scan the Directory : ",DirName)

    flag = os.path.isabs(DirName)  #

    if flag == False:
        DirName = os.path.abspath(DirName)

    exist = os.path.isdir(DirName)  #check whether path is valid or not isdir check whether directory is present or not and return true or false

    if exist:   # if exist == True
        for foldername, subfoldername, filename in os.walk(DirName):
            print("Current Directory name : ",foldername)

            for subname in subfoldername:
                print("Subfolder name is : ",subname)
                
            for fname in filename:
                if (fname == name):
                    print("File is present in the directory with name :", fname)
                    os.remove(os.path.join(foldername, fname))

                    
                    print("File deleted Successfully")
                #print(fname, " : ", os.path.getsize(os.path.join(foldername, fname)), " bytes")
        
    else:
        print("Invalid path")

def main():
    print("-------------- Automation Script --------------")

    print("Automation Script Name : ",argv[0])

    if(argv[1] == "-h" or argv[1] == "-H"):    # Flag for displaying help
        print("This automation script is used to perform File Automations")
        exit()
    
    elif(argv[1] == "-u" or argv[1] == "-U"):    # Flag for displaying the usage of script
        print("Usage : Name_Of_Script First_Argument Second Argument")
        print("Example : Demo.py Marvellous Demo.txt")
        exit()

    else:
        starttime = time.time()
        DirectoryTravel(argv[1], argv[2])
        endtime = time.time()

        print("The script took time to execute as : ",endtime-starttime)

if __name__ == "__main__":
    main()

# python FileAutomation.py Directory_Name


