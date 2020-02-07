import subprocess
import re
from regexs_ import ip_regex, Time_regex, Method_regex, Path_regex, Status_regex, DataSize_regex, Suspicious_Extension_regex

def check_FileExtension(Method_, Path_):
    bool_check = False
    Extension = bool(re.search(Suspicious_Extension_regex, Path_))
    if Extension == True:
        bool_check = True
    else:
        bool_check = False
    return bool_check

def Apache2log():
    file_path = "./access.log"
    result = subprocess.check_output('cat /var/log/apache2/access.log', shell=True)
    Data = str(result, "utf-8").split("\n")

    while True:
        result = subprocess.check_output('tail -1 /var/log/apache2/access.log', shell=True)
        str_result = str(result, "utf-8").replace("\n", "")
        if str_result in Data: #No new log
            pass
        else: #New log
            log = str_result + "\n"

            try: #parsing log
                method = re.compile(Method_regex).findall(log[1])[0]
                path = re.compile(Path_regex).findall(log[1].split(" ")[1])[0]
            except:
                Data.append(log.replace("\n",""))

            try: # check strange extension
                check_FileExtension = check_FileExtension(method, path)
                if check_FileExtension == True:
                    with open(file_path, "a") as f:
                        f.write(log)
                        print("good!")
                        Data.append(log.replace("\n",""))
                else:
                    Data.append(log.replace("\n",""))
                    print("No suspicious extension", path)
            except: # no file extension
                with open(file_path, "a") as f:
                    f.write(log)
                    print("goog!")
                    Data.append(log.replace("\n",""))
    f.close()
if __name__ == "__main__":
    Apache2log()