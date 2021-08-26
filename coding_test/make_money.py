"""
N가지 종류의 화폐가 있습니다. 이 화폐들의 개수를 최소한으로 이용해서 그 가치의 합이 M원이 되도록 
하려고 합니다. 이때 각 종류의 화폐는 몇 개라도 사용할 수 있습니다.

예를 들어 2원, 3원 단위의 화폐가 있을 때는 15원을 만들기 위해 3원을 5개 사용하는 것이 가장 최소한의 
화폐 개수입니다.

M원을 만들기 위한 최소한의 화폐 개수를 출력하는 프로그램을 작성하세요.
"""

# cnt = int(input())

# coin = list(map(int,input().split()))

# num = int(input())

# d = [10001] * (num + 1) 

# for i in range(1,num+1):
#     if i in coin:
#         d[i] = 1
#     else:
#         for j in coin:
#             if i-j >= 0:  
#                 if d[i] > d[i-j]:
#                     d[i] = d[i-j] + 1

# for idx, val in enumerate(d):
#     if val == 10001:
#         d[idx] = -1


# print(d[num])
# print(d)

print("=" * 80)
# ==========================================================================================
# 답안예시

n, m = map(int, input().split())

array = []
for i in range(n):
    array.append(int(input()))

d = [10001] * (m+1)

d[0] = 0
for i in range(n):
    for j in range(array[i], m+1):
        if d[j - array[i]] != 10001: # (i - k)원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j], d[j - array[i]] + 1)

if d[m] == 10001: # 최종적으로 M원을 만드는 방법이 없는 경우
    print(-1)
else:
    print(d[m])