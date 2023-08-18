# GFB 4.1
import itertools
# reference to wikipedia that pseudocode 

def convert_to_path(perm):
    perm = list(perm)
    perm = [0] + perm + [-1]
    path = list()
    for i in range(1, len(perm)):
        path.append((perm[i - 1], perm[i]))
    return path

def solution(times, times_limit):
    # read up bellman-ford algorithm may be an alternation to that
    # no need find min, just need to get as close to the times_limit
    # a modification of the shortest path problem??
    n = len(times)
    distance = [[100000 for _ in times] for _ in times]
    for i in range(n):
        distance[i][i] = 0
    
    # check all possible paths thats not negative cycle
    for i in range(n):
        for _ in range(n-1):
            for u in range(n):
                for v in range(n):
                    if (distance[i][u] + times[u][v] < distance[i][v]):
                        distance[i][v] = distance[i][u] + times[u][v]
                        
        # check path if there exist a negative cycle
        for u in range(n):
            for v in range(n):
                if (distance[i][u] + times[u][v] < distance[i][v]):
                    # it exist a negative cycle, so possible to escape with all bunnies
                    return [i for i in range(n-2)]
                    # test 4 exists []
                    # test 7 is negative cycle

    # no negative cycle, so need to see path with closest val to limit
    # brute force, since only at most 5 
    for i in reversed(range(n-1)):
        for perm in itertools.permutations(range(1, n-1), i):
            total_time = 0
            path = convert_to_path(perm)
            for start, end in path:
                total_time += distance[start][end]
            if total_time <= times_limit:
                return sorted(list(i - 1 for i in perm))

    
print(solution([[0, 9, 9, 9, 1], [9, 0, 9, 9, 9], [9, 9, 0, 9, 9], [9, 9, 9, 0, 9], [9, 9, 9, 9, 0]], 3))
print(solution([[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]], 1))
    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    