from NewInfohandler import GetNewInfo

def GetProcessInfo():
    GetNewInfo('ps -aux', "/home/investigate/new_process.txt")

if __name__ == "__main__":
    GetProcessInfo()