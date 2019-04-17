#2017 Kakao Blind Coding Test 1차 비밀지도(#1)
#question link: http://tech.kakao.com/2017/09/27/kakao-blind-recruitment-round-1/
#bit operation

def solution(n, arr1, arr2):
    answer = []
    ans = ''
    
    for i in range(n):
        num = str(bin(arr1[i] | arr2[i]))
        num = num[2:]
        
        if len(num) != n:
            for k in range(n-len(num)):
                num = ' ' + num
            
        for j in range(len(num)):
            if num[j] == '1':
                ans += '#'
            else:
                ans += ' '
        
        answer.append(ans)
        ans = ''
        
    return answer

#python good code)
#use zip => able to use one loop
#use rjust to fill '0' in front of string
'''
def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0') #총 스트링의 길이가 n이 될 만큼 앞에 '0' 채워준다
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer
'''
