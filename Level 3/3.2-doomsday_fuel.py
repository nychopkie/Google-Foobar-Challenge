# google foobar 3.2 
from fractions import Fraction
from math import gcd #in actual foobar gcd is imported from the fractions module since its 2.7
# i miss numpy i miss linalg.inv i will never trash talk you again numpy please come home from war
# referenced the https://math.dartmouth.edu/archive/m20x06/public_html/Lecture14.pdf

# === Below inversing matrix functions are copied from online sources ===
def eliminate(r1, r2, col, target=0):
    fac = (r2[col]-target) / r1[col]
    for i in range(len(r2)):
        r2[i] -= fac * r1[i]

def gauss(a):
    for i in range(len(a)):
        if a[i][i] == 0:
            for j in range(i+1, len(a)):
                if a[i][j] != 0:
                    a[i], a[j] = a[j], a[i]
                    break
        for j in range(i+1, len(a)):
            eliminate(a[i], a[j], i)
    for i in range(len(a)-1, -1, -1):
        for j in range(i-1, -1, -1):
            eliminate(a[i], a[j], i)
    for i in range(len(a)):
        eliminate(a[i], a[i], i, target=1)
    return a

def inverse(a):
    tmp = [[] for _ in a]
    for i,row in enumerate(a):
        assert len(row) == len(a)
        tmp[i].extend(row + [0]*i + [1] + [0]*(len(a)-i-1))
    gauss(tmp)
    ret = []
    for i in range(len(tmp)):
        ret.append(tmp[i][len(tmp[i])//2:])
    return ret

# === above inverse functions are copied online ===

def solution(m):
    """
    Keyword arguments:
        m -- a 2d matrix on the transitions of the states

    Return: list [n1,n2,...,d] 
        nx -- simplified numerators of the probability of each terminal states
        d -- the common denominator
    """
    row = len(m) # it must be square matrix
    if (row == 1):
        return [1,1]
    
    # normalize the matrix
    sum_row = []
    for k in range(row):
        sum_row.append(sum(m[k]))
    
    for i in range(row):
        if (sum_row[i]):
            for j in range(row):
                m[i][j] = Fraction(m[i][j],sum_row[i])

    # just need Q and R for calculations, so no need to bother with the others
    trancient = []
    terminal = []
    for i in range(row):
        if (sum_row[i] != 0):
            trancient.append(i)
        else:
            terminal.append(i)

    # sort it into canonical form Q and R
    Q = [[Fraction(m[i][j]).limit_denominator() for j in trancient] for i in trancient]
    R = [[Fraction(m[i][j]).limit_denominator() for j in terminal] for i in trancient]
    for i in range(len(Q)):
        for j in range(len(Q)):
            if (i == j):
                Q[i][j] = 1 - Q[i][i]
            else:
                Q[i][j] *= -1  
    N = inverse(Q)
    ans = [0 for _ in range(len(R[0]))]
    for b in range(len(R[0])):
        for c in range(len(N[0])):
            ans[b] += N[0][c] * R[c][b]
    
    # get the common denominator
    denominators = [r.limit_denominator().denominator for r in ans]
    lcm = denominators[0]
    for d in denominators[1:]:
        lcm = lcm // gcd(lcm, d) * d
    
    # absolute mental derangement
    haha = [int(aaaa*lcm) for aaaa in ans]
    haha.append(lcm)
    return haha

print(solution([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))
# test 4 most likly denominator over 100
# python 2.7.13 / performs int division, so need to be specific abt types