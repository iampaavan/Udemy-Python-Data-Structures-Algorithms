import math

def solution(A, B):
    # write your code in Python 3.6
    # Edge Case
    if A >= B:
        return 0

    count = 0

    if(A<=0):
        A = 0

    ma = int(math.sqrt(2147483647))

    for e in range(0, ma+1):

        if((e*e)<=ma+1):
            count = count + 1

    return count


print(solution(-2147483648, 2147483647)),
