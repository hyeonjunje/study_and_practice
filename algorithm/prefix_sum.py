"""구간 합 빠르게 계산하기"""
data = [10,20,30,40,50]

def prefix_sum(data, R, L):
    p = [0]
    num = 0

    for i in data:
        num += i
        p.append(num)
    
    return p[R] - p[L-1]

print(prefix_sum(data, 3, 1))  # 1번째에서 3번째 합 구하기 10+20+30