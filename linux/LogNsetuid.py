import subprocess
import time

def mkdir():
    subprocess.call("mkdirt /home/")

def CheckSetUID(count):
    subprocess.call('find / -perm -4000 > /home/investigate/setUid{}.txt'.format(count), shell=True)
    

def CollectVarLog(logname, count): #wtmp, btmp, lastlog, xferlog, cron, secure, httpd/access_log, httpd/error_log
    subprocess.call('cat /var/log/{} > /home/investigate/{}_{}.bin'.format(logname, logname, count), shell=True)
    subprocess.call('string /home/investigate/{}_{}.bin'.format(logname, count), shell=True)

def CollectHttpdLog(logname, count):
    subprocess.call('cat /var/log/httpd/{} > /home/investigate/{}_{}.bin'.format(logname, logname, count))
if __name__ == "__main__":
    time_input = int(input("time cycle? : "))
    subprocess.call("mkdir /home/investigate", shell=True)
    for i in range(1, 4):
        try:
            CheckSetUID(i)
            CollectVarLog("wtmp", i)
            CollectVarLog("btmp", i)
            CollectVarLog("lastlog", i)
            CollectVarLog("xferlog", i)
            CollectVarLog("cron", i)
            CollectVarLog("secure", i)
            CollectVarLog("messages", i)
            CollectHttpdLog("access_log", i)
            CollectHttpdLog("error_log", i)
            time.sleep(time_input)
        except:
            continue
        


