# google foobar 3.3
# use the sieve of eratosthenes
def solution(l):
    num = len(l)
    
    # to store hit count
    dup = [ 0 for _ in l]
    # better way is to just add to trip instead of list but oh well
    trip= [ 0 for _ in l]

    # find all num of duple lists
    for i in range(num-1):
        for j in range(i+1,num):
            if (l[j] % l[i] == 0):
                dup[j] += 1
                trip[j] += dup[i]
    return sum(trip)
    
print(solution([1,1,1]))