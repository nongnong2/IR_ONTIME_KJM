import subprocess
import re

#check Web, DB services

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

def CheckSetUID(count):
    subprocess.call('find / -perm -4000 > setUid{}.txt'.format(count), shell=True)

def CollectVarLog(logname, count): #wtmp, btmp, lastlog, xferlog, cron, secure, httpd/access_log, httpd/error_log
    subprocess.call('cat /var/log/{} > {}_{}.bin'.format(logname, logname, count), shell=True)
    subprocess.call('string {}_{}.bin'.format(logname, count), shell=True)

def Gethistory():
    User_list = str(subprocess.check_output('grep /bin/bash /etc/passwd | cut -f1 -d:', shell=True),encoding="utf-8").split('\n')
    for user in User_list:
        if user == '':
            pass
        elif user == 'root':
            subprocess.call('cat /root/.bash_history > root_history', shell=True)
        else:
            subprocess.call('cat /home/{}/.bash_history > {}_history.txt'.format(user, user), shell=True)

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

def GetWho():
    GetNewInfo('who -a', "new_who.txt")

def GetNetworkInfo():
    GetNewInfo('netstat -nalp', "new_network.txt")
                
def GetProcessInfo():
    GetNewInfo('ps -aux', "new_process.txt")

if __name__ == "__main__":
    

    