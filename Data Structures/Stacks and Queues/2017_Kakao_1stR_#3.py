#2017 Kakao Blind Coding Test 1차 캐시(#3)
#question link: http://tech.kakao.com/2017/09/27/kakao-blind-recruitment-round-1/
#cache replacement using LRU algorithm ; used queue

def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5
    
    ans = 0
    cache = []
    for i in range(len(cities)):
        city = cities[i].lower()        
        '''
        # this will not work for case like same cities came in before cache becomes full
        if i < cacheSize:
            cache.append(city)
            ans += 5
            continue
        '''        
        if city in cache: #cache hit
            cache.remove(city)
            cache.append(city)
            ans += 1
        else: #cache miss
            if len(cache) < cacheSize:
                cache.append(city)
                ans += 5
                continue
            else:
                del cache[0]
                cache.append(city)
                ans += 5
    
    return ans
