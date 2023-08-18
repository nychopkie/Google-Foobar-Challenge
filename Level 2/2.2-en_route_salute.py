# google foobar 2.2 >> En Route Salute
def solution(s):
    # clean unnessesary blank space and only keep the people
    people = s.replace("-","")

    # find the list of people who will definitely bump into someone
    i1 = people.find(">")
    i2 = people.rfind("<")
    c = people[i1:i2+1]

    n = 0
    encounter = 0
    # use the < people to calculate how many salute
    for i in c:
        if (i == ">"):
            n += 1
        else:
            encounter = encounter + 2*n
            
    return encounter

print(solution(">><><>"))
