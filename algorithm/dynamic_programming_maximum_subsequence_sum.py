"""
연속된 원소를 더한 부분수열의 최댓값을 구하는 문제

-3 3 5 -3 -7 9 -2 10 -5 -2
<알고리즘>
1. 수의 합을 반복적으로 구합니다.
2. 이 때 합이 음수이면 그 다음 수부터 다시 시작 합니다.
3. 합의 최댓값을 도출합니다.
"""


def mss(li_):
    if max(li_) < 0:
        return max(li_)

    maxi = 0
    temp = 0

    for i in range(len(li_)):
        temp += li_[i]
        if temp > maxi:
            maxi = temp
        elif temp < 0:
            temp = 0

    return maxi

li_ = [-3,3,5,-3,-7,9,-2,10,-5,-2]
print(mss(li_))