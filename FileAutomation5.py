from sys import *
import os
import hashlib

def hashfile(path, blocksize = 1024):
    afile = open(path, 'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)

    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    
    return hasher.hexdigest()

def DisplayChecksum(path):
    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)

    exist = os.path.isdir(path)

    if exist:
        for dirname, subdirs, fileList in os.walk(path):
            print("Current folder is :", +dirName)
            for filen in fileList:
                path = os.path.join(dirname, filen)
                file_hash = hashfile(path)
        print("error : Invalid number of arguments")
        exit()

    if(argv[1] == "-h" or argv[1] == "-H"):   
            print("This script is used to traverse specific directory")
            exit()

        elif (argv[1]== "-u"or argv[1] == "-U"):   
            print("Usage : Applicationname AbsolutePath_og_Directory")
            exit()

    try:
        DirectoryWatcher(argv[1])

    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception:
        print("Error : Invalid Input")

if __name__ == "__main__":
    main()

            print(path)
            print(file_hash)
            print(' ')

    else:
        print("Invalid path")

def main():
    print("----Marvellous Infosystems by Piyush Khairnar-----")

    print("Application name :" +argv[0])

    if(len(argv) !=2):
        print("Invalid number of argumnets")
        exit()

        if(argv[1] == "-h" or argv[1] == "-H"):  
            print("This Script is used to traverse specific directory and display checksum of files..")
            exit()

        elif (argv[1]== "-u"or argv[1] == "-U"):  
            print("Usage : Applicationname AbsolutePath_og_Directory Extension ")
            exit()

        try:
            arr = DisplayChecksum(argv[1])

        except ValueError:
            print("error : Invalid datatype of input")

        except Exception as E:
            print("error : Invalid input", E)
if __name__ == "__main__":
    main()

    