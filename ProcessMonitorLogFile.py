import os
import psutil
import time
from sys import *

def ProcessDisplay(log_dir = "Marvellous"):
    listprocess = []

    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass

    separator = "*" * 80
    log_path = os.path.join(log_dir, "Marvellouslog%s.log" %(time.ctime()))
    f = open(log_path, 'w')
    f.write(separator + "\n")
    f.write("Pythonn Machine Learning:"+time.ctime()+ "\n")
    f.write(separator +"\n")

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attr=['pid', 'name', 'username'])
            vms = proc.memory_info().vms/(1024*1024)
            pinfo['vms']= vms
            listprocess.append(pinfo)
        except(psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombleProcess):
            pass

    for elem in listprocess:
        f.write("%s\n" %elem)
def main():
    print("Appliaction name :" + argv[0])
    if(len(argv) != 2):  
        print("Error : Invalid number of arguments")
        exit()   

    if(argv[1] == "-h" or argv[1] == "-H"):   #flag for display help
        print("This script is used log record of running processes")
        exit()

    if (argv[1]== "-u"or argv[1] == "-U"):   #flag for diaplay the usage of script
        print("Usage : Application AbsolutePath_of_Directory")
        exit()

    try:
        ProcessDisplay(argv[1])

    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception:
        print("Error : Invalid Input")
          
if __name__ == "__main__":
    main() 
