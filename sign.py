import win32.win32evtlog as win32evtlog
import time
import datetime
time = time.time() #탐지 프로그램 시작 시간 

server = 'localhost'
logtype = 'Security' # 새 프로세스 생성은 EventID는 4688로 Security에 포함
hand = win32evtlog.OpenEventLog(server, logtype)
flags = win32evtlog.EVENTLOG_BACKWARDS_READ|win32evtlog.EVENTLOG_SEQUENTIAL_READ
total = win32evtlog.GetNumberOfEventLogRecords(hand)

while True:
    events = win32evtlog.ReadEventLog(hand, flags, 0)
    if events:
        for event in events:
            evtTime = str(event.TimeGenerated)
            dt = datetime.datetime(int(evtTime[0:4]),int(evtTime[5:7]),int(evtTime[8:10]),int(evtTime[11:13]),int(evtTime[14:16]),int(evtTime[17:19])).timestamp()
            if dt <= time and event.EventID == 4688: #아니 근데 이거 계속 읽는 건가...;;;
                print("새 프로세스 생성 감지")
                print("Source Name: ", event.SourceName)
                print("Time generated: ", event.TimeGenerated)


#https://stackoverflow.com/questions/42944791/reading-windows-event-log-using-win32evtlog-module

