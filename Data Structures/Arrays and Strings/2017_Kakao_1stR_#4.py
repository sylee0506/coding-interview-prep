#2017 Kakao Blind Coding Test 1차 셔틀버스(#4)
#question link: http://tech.kakao.com/2017/09/27/kakao-blind-recruitment-round-1/
#string manipulation, array, time calculation as string

def solution(n, t, m, timetable):
    bus = n
    time = "09:00"
    timetable.sort()
    
    while bus > 0:
        if bus == 1: #last bus is coming
            if len(timetable) < m:
                return time
            else:
                lastTime = timetable[m-1]
                break
                
        for i in range(m):
            if timetable[0] <= time:
                del timetable[0]
            else:
                break
                
        time = nextbus(time, t)
        bus -= 1  
        
    answer = subtime(lastTime)
    if answer > time:
        answer = time
    
    return answer

def nextbus(time, t): #get next bus arriving time as string format
    hour = int(time[:2])
    minute = int(time[3:])
    minute += t
    if minute >= 60:
        hour += 1
        minute -= 60
    if hour < 10:
        hour = '0' + str(hour)
    if minute < 10:
        minute = '0' + str(minute)
        
    return str(hour) + ":" + str(minute)

def subtime(time): #subtract one minute of time and return as string format
    hour = int(time[:2])
    minute = int(time[3:])
    if minute == 0:
        minute = 60
        hour -= 1
    minute -= 1
    if hour < 10:
        hour = '0' + str(hour)
    if minute < 10:
        minute = '0' + str(minute)
        
    return str(hour) + ":" + str(minute)
