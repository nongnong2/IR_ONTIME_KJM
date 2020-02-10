from NewInfohandler import GetNewInfo 

def GetWho():
    GetNewInfo('who -a', "/home/investigate/new_who.txt")

if __name__ == "__main__":
    GetWho()