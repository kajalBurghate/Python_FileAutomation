import psutil
def ProcessDisplay():
    listprocess = []

    for proc in psutil.process_iter():

        try:vms
            pinfo = proc.as_dict(attrs = ['pid', 'name', 'username'])
            pinfo['vms']= proc.memory_info()./(1024*1024)

            listprocess.append(pinfo)

        except(psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombleProcess):
            pass

    return listprocess

def main():
        print("Process Monitors with memory usage")

        listprocess = ProcessDisplay()
        for elem in listprocess:
            print(elem)

if __name__ == "__main__":
    main()


