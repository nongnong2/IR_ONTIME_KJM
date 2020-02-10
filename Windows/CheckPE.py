import os
import re
import pefile
import psutil
import subprocess
from collections import defaultdict
from basic_process import basic_process

def GetChecklist(check_path):
    root = check_path
    checkList = []

    for (root, dir, Objects) in os.walk(root):
        for Object in Objects:
            path = os.path.join(root, Object)
            checkList.append(path)
    return checkList

def Check_PeNSigned(check_path, sigcheck_path):
    PeList = []
    NotSigned = []
    checkList = GetChecklist(check_path)
    for item in checkList:         
        check_file = open(item, 'rb')
        byte = check_file.read(2)
        if byte == b'MZ':
            PeList.append(item)

        else: 
            continue

    for Pe_file in PeList:           
        cmd = [sigcheck_path, Pe_file]
        fd_popen = subprocess.Popen(cmd, stdout=subprocess.PIPE).stdout 
        data = str(fd_popen.read().strip(),encoding="utf-8")
        if "Signed" in data:
            continue
        else:
            NotSigned.append(path)
        
    return NotSigned

def GetProcess(): #psutuil module
    proc_list = []
    for proc in psutil.process_iter():
        if proc.name() in basic_process:
            continue
        else:
            proc_list.append(proc.name())
    return proc_list

def Check_IAT(check_path, Listdlls_path): #Listdlls.exe
    checkList = GetProcess()
    IAT_list = []
    for item in checkList:
        cmd = [Listdlls_path, item]
        fd_popen = subprocess.Popen(cmd, stdout=subprocess.PIPE).stdout
        try:
            data = str(fd_popen.read().strip(), encoding="utf-8")
            IAT_list.append(data)
        except:
            pass

if __name__ == "__main__":
    Check_IAT(r"C:\tools", r"C:\tools\Listdlls.exe")
    



