# google foobar 3.1 triangle number thing the_grandest_staircase_of_them_all 
# basically dynamic programming
def solution(n):
    # Your code here
    arr = [0 for _ in range(n+1)]
    arr[0]=1
    for i in range(1,n):
        for j in range(n,i-1,-1):
            arr[j] += arr[j-i]
    return arr[n]

print(solution(3))

        
    