a = [1,2,3,2,5,1,78,2,3,2,4,3,8,2,3,4,1,2,8]

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
                sub_list.append(a[start:end+1])
            end += 1
        else:
            start += 1

    return (sub_list,count)

print(solution(a, 10))
        
