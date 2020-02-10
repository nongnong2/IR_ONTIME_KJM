from NewInfohandler import GetNewInfo

def GetNetworkInfo():
    GetNewInfo('netstat -nalp', "/home/investigate/new_network.txt")

if __name__ == "__main__":
    GetNetworkInfo()