# google foobar 2.1 version control
def solution(l):
    # check major, then minor and revison
    result = l

    result.sort(key=lambda s: [int(u) for u in s.split('.')])
                    
    return result

print(solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]))
