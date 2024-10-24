#2017 Kakao Blind Coding Test 1차 다트게임(#2)
#question link: http://tech.kakao.com/2017/09/27/kakao-blind-recruitment-round-1/
#string manipulation

def solution(dartResult):
    ans = 0
    num = []
    set = -1
    
    for i in range(len(dartResult)):
        if dartResult[i] == 'S':
            num[set] = num[set]**1
        elif dartResult[i] == 'D':
            num[set] = num[set]**2
        elif dartResult[i] == 'T':
            num[set] = num[set]**3
        elif dartResult[i] == '*':
            if set == 0:
                num[set] *= 2
            else:
                num[set] *= 2
                num[set-1] *= 2
        elif dartResult[i] == '#':
            num[set] *= -1
        else:
            if dartResult[i] == '0' and dartResult[i-1] == '1':#when score is 10
                num.pop()
                num.append(10)
            else:
                num.append(int(dartResult[i]))
                set += 1
    
    print(num)
    for i in range(3):
        ans += num[i]
    return ans
