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

def Apache2log():
    file_path = "./access.log"
    result = subprocess.check_output('cat /var/log/apache2/access.log', shell=True)
    # Data= str(result, "utf-8").split("\n")
    Data_size = os.path.getsize("/var/log/apache2/access.log")
    while True:
        Data_size = os.path.getsize("/var/log/apache2/access.log")
        result = subprocess.check_output('tail -1 /var/log/apache2/access.log', shell=True)
        str_result = str(result, "utf-8").replace("\n", "")
        Data_size_compare = os.path.getsize("/var/log/apache2/access.log")

        if Data_size == Data_size_compare: #No new log
            pass
        else: #New log
            log = str_result + "\n"
            
            path = log.split(" ")[6]
            new_Data.append(log) #append new log to list
            Sql_Check = check_File(path, Sql_injection_regx, file_path, log)
            Sus_Extension = check_File(path, Suspicious_Extension_regex, file_path, log)
            Css_Check = check_File(path, CssAttack_regx, file_path, log)

    f.close()
if __name__ == "__main__":
    Apache2log()