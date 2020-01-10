import Evtx.Evtx as evtx 
import Evtx.Views as e_views
from bs4 import BeautifulSoup
import subprocess
import re
import os

def check_Evid():
    path = r"C:\Windows\System32\winevt\Logs\Security.evtx"
    R_EventID = re.compile("[0-9]+(?=<)")
    R_NewProcessName = re.compile("(?<=<Data Name=>).+(?=<)")
    R_CreationTime = re.compile("(?<=SystemTime=\").+(?=\">)")

    with evtx.Evtx(path) as log:
        for record in log.records():
            xmlStr = str(record.xml())
            EventID = R_EventID.findall(xmlStr)
            if int(EventID[0]) == 4688:
                print("새 프로세스 생성 감지")
                NewProcessName = R_NewProcessName.findall(xmlStr)
                CreationTime = R_CreationTime.findall(xmlStr)
                print(CreationTime)
                print(NewProcessName)

def Check_PE():
    root = "./"
    PE_files = []
    for (root, dir, Objects) in os.walk(root):
        for Object in Objects:
            path = os.path.join(root, Object)            
            check_file = open(path, 'rb')
            byte = check_file.read(2)

            if byte == b'MZ':
                PE_files.append(Object)

            else: 
                continue

    for PE_file in PE_files:
        path = os.path.join(root, Object)            
        cmd = ['sigcheck.exe', path]
        fd_popen = subprocess.Popen(cmd, stdout=subprocess.PIPE).stdout 
        data = fd_popen.read().strip() 
        fd_popen.close() 
        print(PE_file, ':', data)

def main():
    Check_PE()

if __name__ == "__main__":
    main()
