# check maximum matching???
# blossom algorithm possibly
# should use blossom's algorithm technially but i mean this works i guess
# this is the bruteforce method

from math import gcd # for GFB its from fractions
def is_power_of_two(n):
    # bitwise operation to check power of 2
    return (n & (n - 1) == 0) and n != 0

def solution(banana_list):
    # 2 big problem : will you loop? max looping pairs
    # p1: will you loop?
    # if odd even pair must inf loop
    # is there possibly other conditions?? 
    # sum div by GCD not power of 2
    
    # queue of vals to be matched
    temp = [banana_list[-1]]
    
    for banana in banana_list[:-1]:
        next_banana = False
        # loop thru temp to see any can be matched to new ones
        for i in temp:
            if (is_power_of_two((i+banana)//gcd(i,banana)) == False and i != banana):
                # can form pair aka remove from temp
                temp.remove(i)
                next_banana = True
                break
        if next_banana == False:
            temp.append(banana)
    
    return len(temp)

print(solution([1,7,3,21,13,19]))
print(solution([1,1]))



