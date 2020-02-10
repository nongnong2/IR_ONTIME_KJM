from Apache2 import check_File
from Apache2 import Get_StrangeApache2log

def Get_Stange_Apache_errorlog():
    Get_StrangeApache2log("/var/log/apache2/error.log", "/home/investigate/errorlog.txt")

if __name__ == "__main__":
    Get_Stange_Apache_errorlog()

