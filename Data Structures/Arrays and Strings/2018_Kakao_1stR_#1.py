#2018 Kakao Blind Coding Test 1차 오픈채팅방(#1)
#question link: http://tech.kakao.com/2018/09/21/kakao-blind-recruitment-for2019-round-1/
#string manipulation & dictionary

def solution(record):
    mydict = {}
    ans = []
    for i in range(len(record)):
        L = record[i].split(" ")
        if (L[0] == "Enter") or (L[0] == "Change"):
            mydict[L[1]] = L[2]
        #this occurs runtime error ; do not modify dictionary in loop!
        '''
        elif L[0] == "Leave":
            del mydict[L[1]]
        '''
            
    for i in range(len(record)):
        L = record[i].split(" ")
        if L[0] == "Enter":
            ans.append("%s님이 들어왔습니다."%mydict[L[1]])
        elif L[0] == "Leave":
            ans.append("%s님이 나갔습니다."%mydict[L[1]])
    
    return ans
