import subprocess
import re
import os
from regexs_ import ip_regex, Time_regex, Method_regex, Path_regex, Status_regex, DataSize_regex, Suspicious_Extension_regex, Sql_injection_regx, CssAttack_regx

def check_File(Path, regex, file_path, log):
    check = bool(re.search(regex, Path))
    if check == True:
        with open(file_path, "a") as f:
            f.write(log)
            print(log)
            return True
    else:
        return False

def Get_StrangeApache2log(log_full_path, write_full_path):
    result = subprocess.check_output('cat {}'.format(log_full_path), shell=True)
    Data_size = os.path.getsize(log_full_path)
    while True:
        Data_size = os.path.getsize(log_full_path)
        result = subprocess.check_output('tail -1 {}'.format(log_full_path), shell=True)
        str_result = str(result, "utf-8").replace("\n", "")
        Data_size_compare = os.path.getsize(log_full_path)

        if Data_size == Data_size_compare: #No new log
            pass
        else: #New log
            log = str_result + "\n"
            
            path = log.split(" ")[6]
            Sql_Check = check_File(path, Sql_injection_regx, write_full_path, log)
            Sus_Extension = check_File(path, Suspicious_Extension_regex, write_full_path, log)
            Css_Check = check_File(path, CssAttack_regx, write_full_path, log)

    f.close()
if __name__ == "__main__":
    Get_StrangeApache2log("/var/log/apache2/access.log", "/home/ksm/Desktop/accesslog.txt")
    Get_StrangeApache2log("/var/log/apache2/error.log", "/home/ksm/Desktop/errorlog.txt")