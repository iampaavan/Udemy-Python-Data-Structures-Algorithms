def solution(A):
    # write your code in Python 3.6
    m = max(A)
    if(m <=0):
        m = 1
    count = {}
    for e in range(1,m+2):
        count[e] = 0
    for e in A:
        if(e<=0): continue
        count[e] = 1
    for e in range(1, m+2):
        if(count[e] == 0):
            return e


#solution([1, 3, 6, 4, 1, 2])
#solution([1,2,3])
print(solution([-1, -3]))