from NewInfohandler import GetNewInfo, GetNewinfo_Size
import subprocess
import os

def Gethistory():
    User_list = str(subprocess.check_output('grep /bin/bash /etc/passwd | cut -f1 -d:', shell=True),encoding="utf-8").split('\n')
    for user in User_list:
        while True:
            if user == '':
                pass
            elif user == 'root':
                GetNewinfo_Size("/root/.bash_history","/home/investigate/root_history")
                    
            else:
                GetNewinfo_Size("/home/{}/.bash_history".format(user),"/home/investigate/{}_history".format(user))
                
if __name__ == "__main__":
    Gethistory()