import win32.win32evtlog as win32evtlog
import time
import datetime
time = time.time() #탐지 프로그램 시작 시간 

while True:
    server = 'localhost'
    logtype = 'Security' # 새 프로세스 생성은 EventID는 4688로 Security에 포함
    hand = win32evtlog.OpenEventLog(server, logtype)
    flags = win32evtlog.EVENTLOG_BACKWARDS_READ|win32evtlog.EVENTLOG_SEQUENTIAL_READ
    total = win32evtlog.GetNumberOfEventLogRecords(hand)
    events = win32evtlog.ReadEventLog(hand, flags, 0)
    print(total)
    if events:
        for event in events:
            evtTime = str(event.TimeGenerated)
            dt = datetime.datetime(int(evtTime[0:4]),int(evtTime[5:7]),int(evtTime[8:10]),int(evtTime[11:13]),int(evtTime[14:16]),int(evtTime[17:19])).timestamp()
            if dt >= time and event.EventID == 4688: #실행 이전 로그는 살펴볼 필요 없는데 어찌 구현하누??;;;; 굳이 비교도 안해도 될거 같은데...
                print("새 프로세스 생성 감지")
                print("Source Name: ", event.SourceName)
                print("Time generated: ", event.TimeGenerated)

#생각해볼것들
#1. 실행 이후의 이벤트로그만 보면 된다. 이전꺼는 볼 필요도 없는데 어떻게 구현할까?
#2. 디지털 서명 확인 & 비실행 파일 포함 여부 확인 

#https://stackoverflow.com/questions/42944791/reading-windows-event-log-using-win32evtlog-module

