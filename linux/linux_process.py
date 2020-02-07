import subprocess
import re
from regexs_ import ip_regex, Time_regex, Method_regex, Path_regex, Status_regex, DataSize_regex, Suspicious_Extension_regex

"""
웹 서버 업로드 공격하거나 DB자체에 공격할 수 있음 
Web Shell
1. 웹쉘이 유입될수도 있고
2. 웹쉘이 이미 존재한 상태일 수도 있음

SQL injection
Sql injection 관련 대응 - https://dzone.com/articles/how-to-detect-sql-injection-attacks-using-extended

RFI/LFI

1. mysql errolg 활성화 필요
ps ax | grep mysql
/var/log/secure
/var/log/httpd
/var/log/apache2/access.log(간추릴 필요 있음 )


백도어 탐지

crontab 확인 
/var/spool/cron에 해당 계정명으로 생성되어 있음 
"""

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

def CheckProcessList():
    subprocess.call('ps -ef', shell=True)

def CheckNetwork():
    subprocess.call('netstat -an', shell=True)

def CheckSetUID(path):
    subprocess.call('find {} -perm -4000'.format(path), shell=True)

def Collectlog(logname): #wtpm, btm, last, xfer, cron, secure, httpd
    subprocess.call('cp /var/log/{} {}.bin'.format(logname, logname), shell=True)
    subprocess.call('string {}.bin'.format(logname), shell=True)

def check_FileExtension(Method_, Path_):
    bool_check = False
    Extension = bool(re.search(Suspicious_Extension_regex, Path_))
    if Extension == True:
        bool_check = True
    else:
        bool_check = False
    return bool_check

def Apache2log():
    f = open("./access.log", "a")
    result = subprocess.check_output('cat /var/log/apache2/access.log', shell=True)
    Data = str(result, "utf-8").split("\n")
    while True:
        result = subprocess.check_output('tail -1 /var/log/apache2/access.log', shell=True)
        str_result = str(result, "utf-8").replace("\n", "")
        if str_result in Data: #No new log
            pass

        else: #New log
            log = str_result + "\n"
            try:
                method = re.compile(Method_regex).findall(log[1])[0]
                path = re.compile(Path_regex).findall(log[1].split(" ")[1])[0]
            except:
                pass
            try:
                check_FileExtension = check_FileExtension(method, path)
                if check_FileExtension == True:
                    f.write(log)
                    print("good!")
                    f.close()
                else:
                    print("No suspicious extension", path)
            except:
                print("good!")
                pass

if __name__ == "__main__":
    file_path = subprocess.call('pwd')
    Apache2log()