from time import time

"""
투 포인터 알고리즘
1. 시작점, 끝점이 첫 번째 원소의 인덱스(0)를 가리키도록 한다.
2. 현재 부분합이 M과 같다면 카운트한다.
3. 현재 부분합이 M보다 작거나 같다면 end를 1 증가시킨다.
4. 현재 부분합이 M보다 크다면, start를 1 증가시킨다.
5. 모든 경우를 확인할 때까지 2~4 과정을 반복
"""

a = [1] * 100000

"""합이 K인 부분 연속 수열의 개수 구하기"""

def solution(a, K):
    """배열 a와 합 K를 파라미터로 하는 함수"""

    start = 0
    end = 0
    count = 0
    sub_list = []

    while start != len(a) and end != len(a):
        if sum(a[start:end+1]) <= K:
            if sum(a[start:end+1]) == K:
                count += 1
                # sub_list.append(a[start:end+1])
            end += 1
        else:
            start += 1

    return count
    # return (sub_list,count)


def solution_2(a, K):
    result = 0
    summary = 0
    end = 0

    for start in range(len(a)):
        while summary < K and end < len(a):
            summary += a[end]
            end += 1
        
        if summary == K:
            result += 1
        summary -= a[start]

    return result

first = time()
print(solution(a, 10))
print("걸린 시간 : {}", format(time() - first))


second = time()
print(solution_2(a, 10))
print("걸린 시간 : {}", format(time() - second))
