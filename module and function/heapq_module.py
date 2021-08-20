import heapq as hq
"""
이 모듈은 우선순위 큐 알고리즘이라고도 하는 힙(heap) 큐 알고리즘의 구현을 제공한다.
힙은 모든 부모 노드가 자식보다 작거나 같은 값을 갖는 이진 트리이다.
가장 작은 요소가 항상 루트인 heap[0]이다.
"""

heap = []
# 1.heappush 힙 불변성을 유지하면서 item값을 heap으로 푸시한다.
hq.heappush(heap, 3)
hq.heappush(heap, 5)
hq.heappush(heap, 1)
hq.heappush(heap, 4)
hq.heappush(heap, 7)
print(heap)

# 2.heappop 힙 불변성을 유지하면서 heap 에서 가장 작은 item을 팝하고 반환한다.
# 힙이 비어 있으면 IndexError 발생
# 팝하지 않고 가장 작은 항목에 접근할려면 heap[0]을 사용 (heap[1]이 두번째로 작은 수라는 보장은 없음)
root = hq.heappop(heap)
print(root)
print(heap)

# 3.heapify(x) 리스트 x를 선형시간으로 제자리에서 힙으로 변환
any_list = [7,1,3,8,2,4,5,10]
hq.heapify(any_list)
print(any_list)


# 응용 1 최대 힙 만들기
def max_heap(heap):
    summary = []
    answer = []
    for i in heap:
        hq.heappush(summary, (-i, i))

    while summary:
        answer.append(hq.heappop(summary)[1])
    
    return answer

any_list = [7,1,3,8,2,4,5,10]
print(max_heap(any_list))


# 응용 2 힙 정렬
def heapsort(data:list):
    answer = []
    hq.heapify(data)
    while data:
        value = hq.heappop(data)
        answer.append(value)
    return answer

any_any_list = [7,1,3,8,2,4,5,10,80,13,15]
print(heapsort(any_any_list))


# 응용 3 K번째 최소값/최대값
def kth_smallest(nums, k):
    # heap을 사용하면 더 효율적
    summary = 0
    hq.heapify(nums)
    for i in range(k):
        summary = hq.heappop(nums)
    
    return summary

any_any_any_list = [7,1,3,8,2,4,5,10,80,13,15]
print(kth_smallest(any_any_any_list, 3))  # 3번째로 가장 작은 값
