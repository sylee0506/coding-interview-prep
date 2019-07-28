#Google Kick Start Round D 2019 #3 Food Stalls

num = int(input())
for i in range(num):
    K, N = input().split(' ')
    dist = list(input().split(' '))
    cost = list(input().split(' '))
    K = int(K)
    N = int(N)
    result_list = []
    
    for j in range(N):
        ware = int(cost[j])
        stall = []
        for n in range(N):
            if n == j:
                continue
            else:
                stall.append(abs(int(dist[n])-int(dist[j])) + int(cost[n]))
        stall.sort()
        result = ware
        for k in range(K):
            result += int(stall[k])
        result_list.append(result)
    
    result_list.sort()
    print("Case #%d: %d"%(i+1, int(result_list[0])))
