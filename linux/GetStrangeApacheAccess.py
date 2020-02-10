from Apache2 import check_File
from Apache2 import Get_StrangeApache2log

def Get_Stange_Apache_accesslog():
    Get_StrangeApache2log("/var/log/apache2/access.log", "/home/investigate/accesslog.txt")

if __name__ == "__main__":
    Get_Stange_Apache_accesslog()

