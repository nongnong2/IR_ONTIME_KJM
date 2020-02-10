import subprocess
import time
import GetService from GetService

def CheckSetUID(count):
    subprocess.call('find / -perm -4000 > /home/investigate/setUid{}.txt'.format(count), shell=True)
    
def CollectVarLog(logname, count): #wtmp, btmp, lastlog, xferlog, cron, secure, httpd/access_log, httpd/error_log
    subprocess.call('cat /var/log/{} > /home/investigate/{}_{}.bin'.format(logname, logname, count), shell=True)

def CollectHttpdLog(logname, count):
    subprocess.call('cat /var/log/httpd/{} > /home/investigate/{}_{}.bin'.format(logname, logname, count), shell=True)
    
if __name__ == "__main__":
    time_input = int(input("time cycle? : "))
    for i in range(1, 4):
        CollectVarLog("wtmp", i)
        CollectVarLog("btmp", i)
        CollectVarLog("lastlog", i)
        CollectVarLog("xferlog", i)
        CollectVarLog("cron", i)
        CollectVarLog("secure", i)
        CollectVarLog("messages", i)
        CollectHttpdLog("access_log", i)
        CollectHttpdLog("error_log", i)
        CheckSetUID(i)
        time.sleep(time_input)
    
    Service_list = GetService()
    if "mongodb" in Service_list:
        subprocess.call("cp /var/log/mongodb/error.log /home/investigate/")

    elif "mysql" in Service_list:
        subprocess.call("cp /var/log/mysql/error.log /home/investigate")

    elif "mariadb" om Service_list:
        subprocess.call("cp /var/log/mariadb/error.log /home/investigate")

    subprocess.call("netstat -nalp > /home/investigate/final_netsta.txt")
    subprocess.call("ps -aux > /home/investigate/final_process.txt")
    subprocess.call("cp /var/spool/cron /home/investigate/")

    """
    mongodb : /var/log/mongodb/mongod.log
    mysql : /var/log/mongodb/mysql
    mariadb : /var/log/mongodb/mysql
    """
#Find conf file and do apply the path to code....

        


