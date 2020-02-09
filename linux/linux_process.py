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

def CheckProcessList(count):
    subprocess.call('ps -ef > pslite{}.txt'.format(count), shell=True)

def CheckNetwork(count):
    subprocess.call('netstat -an > netlist{}.txt'.format(count), shell=True)

def CheckSetUID(count):
    subprocess.call('find / -perm -4000 > Uid{}.txt'.format(count), shell=True)

def CollectVarLog(logname, count): #wtmp, btmp, lastlog, xferlog, cron, secure, httpd/access_log, httpd/error_log
    subprocess.call('cat /var/log/{} > {}/{}_{}.bin'.format(logname, logname, logname, count), shell=True)
    subprocess.call('string {}/{}_{}.bin'.format(logname, logname, count), shell=True)

def Gethistory():
    User_list = str(subprocess.check_output('grep /bin/bash /etc/passwd | cut -f1 -d:', shell=True),encoding="utf-8").split('\n')
    for user in User_list:
        if user == '':
            pass
        elif user == 'root':
            subprocess.call('cat /root/.bash_history > root_history', shell=True)
        else:
            subprocess.call('cat /home/{}/.bash_history > {}_history.txt'.format(user, user), shell=True)

def Who():
    subprocess.call('who -a > who.txt')

def GetNetworkInfo(count):
    subprocess.call('cat netstat -naop > network_{}'.format(count), shell=True)

def GetProcessInfo(count):
    subprocess.call('cat ps -ef -naop > process_{}'.format(count), shell=True)

if __name__ == "__main__":
    
    