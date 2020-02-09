import subprocess
import multiprocessing
import re
import time

#check Web, DB services
def GetNewInfo(command, fileName):
    first_list = str(subprocess.check_output(command, shell=True), encoding="utf-8").split("\n")
    Dup_check_list = []
    while True:
        check_new_list = str(subprocess.check_output(command, shell=True), encoding="utf-8").split("\n")
        for item in check_new_list:
            if item in first_list:
                check_new_list.remove(item)
        
        for item in check_new_list:
            with open(fileName, "a") as f:
                if item in Dup_check_list or item == "":
                    continue
                else:
                    f.write(item + "\n")
                    Dup_check_list.append(item)

def CheckService():
    Service_list = []
    result = subprocess.check_output('service --status-all|grep +', shell='True')
    if "apache2" in result :
        Service_list.append("apache2")

    if "mongodb" in result :
        Service_list.append("mongodb")

    if "mysql" in result :
        Service_list.append("mysql")

    if "mariadb" in result :
        Service_list.append("mariadb")

    return Service_list
    
def Gethistory():
    User_list = str(subprocess.check_output('grep /bin/bash /etc/passwd | cut -f1 -d:', shell=True),encoding="utf-8").split('\n')
    for user in User_list:
        if user == '':
            pass
        elif user == 'root':
            GetNewInfo('cat /home/{}/.bash_history > /home/investigate/{}_history.txt'.format(user, user),"{}_history.txt".format(user))
            # subprocess.call('cat /root/.bash_history > root_history', shell=True)
        else:
            GetNewInfo('cat /home/{}/.bash_history > /home/investigate{}_history.txt'.format(user, user),"{}_history.txt".format(user))

def GetWho():
    GetNewInfo('who -a', "/home/investigate/new_who.txt")

def GetNetworkInfo():
    GetNewInfo('netstat -nalp', "/home/investigate/new_network.txt")
                
def GetProcessInfo():
    GetNewInfo('ps -aux', "/home/investigate/new_process.txt")

if __name__ == "__main__":
    Gethistory()
    GetWho()
    GetNetworkInfo()
    GetProcessInfo()



    