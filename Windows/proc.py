"""
1. 프로세스- 운영체제 파악 - 기본 프로세스 제거, sigcheck(powershell, cmd, 한글, doc 등 제외), dll체크
2. 레지스트리
3. 이벤트로그 psloglist
4. 웹브라우저

8. 서비스 psservice
9. 임시인터넷 파일
10. 파일시스템 로그
"""
import platform
import subprocess
import getpass

def GetUsername():
    Username = getpass.getuser()
    return Username

def GetOsInfo():
    system = platform.system()
    release = platform.release()
    bit = platform.architecture()[0]

def GetReg(ripExe_path, Reg_path, profile): #rip.exe 
    # ex. rip -r c:\case\system -f system
    user = GetUsername()
    SystemReg_cmd = [ripExe_path, "r" , Reg_path, "-f", profile]
    fd_popen = subprocess.Popen(SystemReg_cmd, stdout=subprocess.PIPE).stdout 

def GetHivenMftnEvt(forecopy_path, hive_path, save_location):
    hive_cmd = [forecopy_path, "-f", hive_path, save_location]
    fd_popen = subprocess.Popen(hive_cmd, stdout=subprocess.PIPE).stdout 

def GetMft(forecopy_path, mft_path, save_location):
    mft_cmd = [forecopy_path, "-f", mft_path, save_location]
    fd_popen = subprocess.Popen(mft_cmd, stdout=subprocess.PIPE).stdout 

def GetEvt(forecopy_path, evt_path, save_location)
    evt_cmd = [forecopy_path, "-f", evt_path, save_location]    
    fd_popen = subprocess.Popen(evt_cmd, stdout=subprocess.PIPE).stdout

def GetNetwork()

def Autoruns()# 시작프로그램 check
