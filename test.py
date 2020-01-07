import Evtx.Evtx as evtx 
import Evtx.Views as e_views
from bs4 import BeautifulSoup
import subprocess
import re

def check_EvidnSig():
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
                #sigcheck 사용 
                cmd = ['sigcheck.exe', NewProcessName]
                fd_popen = subprocess.Popen(cmd, stdout=subprocess.PIPE).stdout 
                data = fd_popen.read().strip() 
                fd_popen.close() 
                print(data)

def main():
    while True:
        check_EvidnSig()

if __name__ == "__main__":
    main()
