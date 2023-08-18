# google foobar 1 >> The cake is not a lie! >>  find the repeating subsets
def solution(s):
    L = len(s)
    for i in range(L):
        sub = s[:i]
        l = len(sub)
        occurs = s.count(sub)
        if occurs * l == L:
            return occurs
    return 1