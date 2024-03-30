import os
import time
import psutil
import urllib2
import smtplib
import schedule
from sys import *
from email import encoders
from email.mime.text import MIMEText
from emial.mime.base import MIMEbase
from email.mime.multipart import MIMEMultipart

def is_connected():   #used to check internet connection if connected returns true else false
    try:
        urllib2.urlopen('http://www.gmail.com', timeout = 1)
        return True
    except urllib2.URLError as err:
        return False

def MailSender(filename, time):
    try:
        fromaddr = "kajal.nagane12792@gmail.com"
        toaddr = "burghate.ashish@gmail.com"

        msg = MIMEmultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr

        body = """
        Hello

        Thanks & Regards,
        Kajal 
        """%(toaddr, time)

        Subject = "Automated email"
        

        msg['Subject'] = Subject

        msg.attach(MIMEText(body, 'plain'))
        attachment = open(filename, "rb")
        p = MIMEbase('application', 'octet-stream')
        p.set_payload((attachment).read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', "Attachment; filename = %s" %filename)
        msg.attach(p)
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(fromaddr, "knagane12792@gmail.com", "Kajal@1207")
        text = msg.as_string()
        s.sendmail(fromaddr, toaddr, text)
        s.quit()

        print("Log File successfully sent through mail")

    except Exception as E:
        print("Unable to send mail.", E)
def ProcessLog(log_dir = 'Marvellous'):
    listprocess = []

    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass

    separator = "*" * 80
    log_path = os.path.join(log_dir, "MarvellousLog%s.log"%(time.ctime()))
    f = open(log_path, 'w')
    f.write(separator +"\n")
    f.write("marvellous Info Process logger :"+time.ctime()+"\n")
    f.write(separator+"\n")
    f.write("\n")

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attr=['pid', 'name', 'username'])
            vms= proc.memory_info().vms/(1024*1024)
            pinfo['vms'] = vmslistprocess.append(pinfo)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombleProcess):
            pass
        for element in listprocess:
        f.write("%s\n"%element)

        print("Log File is successfully generated at location %s", %(log_path))

        connect = is_connected()

        if connected:
            starttime = time.time()
            MailSender(log_path,time.ctime())
            endTime = time.time()

            print('Took %s seconds to send mail' %(endTime - startTime))

        else:
            print("There is no internet connection")

def main():
    print("Applictaion name :" +argv[0])
    
    if(len(argv) != 2):  
        print("Error : Invalid number of arguments")
        exit()   

    if(argv[1] == "-h" or argv[1] == "-H"):   #flag for display help
        print("This script is used log record of running processes")
        exit()

    if (argv[1]== "-u"or argv[1] == "-U"):   #flag for diaplay the usage of script
        print("Usage : ApplicationName AbsolutePath_of_Directory")
        exit()

    try:
        schedule.every(int(argv[1])).minutes.do(ProcessLog)
        while True:
            schedule.run_pending()
            time.sleep(1)


    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception:
        print("Error : Invalid Input",E)
          
if __name__ == "__main__":
    main() 






