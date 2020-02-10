import subprocess
import re
import os
from regexs_ import Method_regex, Suspicious_Extension_regex, Sql_injection_regx, CssAttack_regx, Str_dot

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
            Dot_Check = re.compile(Str_dot).findall(path)
            if len(Dot_Check) != 1:
                with open(write_full_path, "a") as f:
                    f.write(log)
                    print(log)
            else:
                pass
    f.close()

