from functools import partialmethod


class Node:
    """이진 트리 노드 클래스"""
    def __init__(self, data) -> None:
        """데이터와 두 자식 노드에 대한 레퍼런스를 갖는다."""
        self.data = data
        self.left_child = None
        self.right_child = None


#---------------------------------------------------------------------------------------

# """노드 인스턴스 생성"""
# root_node = Node(2)
# node_B = Node(3)
# node_C = Node(5)
# node_D = Node(7)
# node_E = Node(11)

# """B와 C를 root 노드의 자식으로 지정"""
# root_node.right_child = node_C
# root_node.left_child = node_B

# """D와 E를 B의 자식으로 지정"""
# node_B.right_child = node_E
# node_B.left_child = node_D

# # root 노드에서 왼쪽 자식 노드 받아오기
# test_node_1 = root_node.left_child

# print(test_node_1.data)

# # 노드 B의 오른쪽 자식 노드 받아오기
# test_node_2 = test_node_1.right_child

# print(test_node_2.data)

#---------------------------------------------------------------------------------------
def traverse_inorder(node):
    """in - order 순회 함수"""
    if node is not None: 
        traverse_inorder(node.left_child) # 재귀적으로 왼쪽 부분 트리 순회
        print(node.data) # 데이터 출력
        traverse_inorder(node.right_child) # 재귀적으로 오른쪽 부분 트리 순회
        

#---------------------------------------------------------------------------------------
# # 여러 노드 인스턴스 생성
# node_A = Node("A")
# node_B = Node("B")
# node_C = Node("C")
# node_D = Node("D")
# node_E = Node("E")
# node_F = Node("F")
# node_G = Node("G")
# node_H = Node("H")
# node_I = Node("I")

# # 생성한 노드 인스턴스들 연결
# node_F.left_child = node_B
# node_F.right_child = node_G

# node_B.left_child = node_A
# node_B.right_child = node_D

# node_D.left_child = node_C
# node_D.right_child = node_E

# node_G.right_child = node_I

# node_I.left_child = node_H

# # 노드 F를 root 노드로 만든다
# root_node = node_F

# # 만들어 놓은 트리를 in-order로 순회한다
# traverse_inorder(root_node)

#---------------------------------------------------------------------------------------
def swap(tree, index_1, index_2):
    """완전 이진 트리의 노드 index_1과 노드 index_2의 위치를 바꿔준다."""
    temp = tree[index_1]
    tree[index_1] = tree[index_2]
    tree[index_2] = temp

#---------------------------------------------------------------------------------------
def heapify(tree, index, tree_size):
    """heapify 함수"""

    # 왼쪽 자식 노드의 인덱스와 오른쪽 자식 노드의 인덱스를 계산
    left_child_index = index * 2
    right_child_index = index * 2 + 1

    largest = index # 일단 부모 노드의 값이 가장 크다고 설정

    # 왼쪽 자식 노드의 값과 비교
    if 0 < left_child_index < tree_size and tree[largest] < tree[left_child_index]:
        largest = left_child_index
    
    # 오른쪽 자식 노드의 값과 비교
    if 0 < right_child_index < tree_size and tree[largest] < tree[right_child_index]:
        largest = right_child_index
    
    if largest != index:
        swap(tree, index, largest)
        heapify(tree, largest, tree_size)

#---------------------------------------------------------------------------------------
# heapify하려고 하는 완전 이진 트리
# tree = [None, 15, 5, 12, 14, 9, 10, 6, 2, 11, 1] 
# heapify(tree, 2, len(tree))  # 노드 2에 heapify 호출
# print(tree) 

#---------------------------------------------------------------------------------------
def heapsort(tree):
    """힙 정렬 함수"""
    tree_size = len(tree)

    # 마지막 인덱스부터 처음 인덱스까지 heapify를 호출한다.
    for i in range(tree_size-1, 0, -1):
        heapify(tree, i, tree_size)

    # 마지막 인덱스부터 처음 인덱스까지
    for i in range(tree_size-1, 0, -1):
        swap(tree, 1, i) # root 노드와 마지막 인덱스를 바꿔준 후
        heapify(tree, 1, i) # root 노드에 heapify를 호출한다.
        """
        tree_size를 i로 넘겨주면 heapify 함수가 인식하는 히스트의 크기가 
        매번 줄어든다. 즉 tree라는 전체 리스트의 사이즈는 그대로지만 
        실제로 heapify의 대상이 되는 리스트의 크기는 하나씩 줄어들게 된다.
        """

#---------------------------------------------------------------------------------------
# data_to_sort = [None, 6, 1, 4, 7, 10, 3, 8, 5, 1, 5, 7, 4, 2, 1]
# heapsort(data_to_sort)
# print(data_to_sort)

#---------------------------------------------------------------------------------------
def reverse_heapify(tree, index):
    """삽입된 노드를 힙 속성을 지키는 위치로 이동시키는 함수"""
    parent_index = index // 2 # 삽입된 노드의 부모 노드의 인덱스 계산

    # 부모 노드가 존재하고, 부모 노드의 값이 삽입된 노드의 값보다 작을 때
    if 0 < parent_index < len(tree) and tree[index] > tree[parent_index]:
        swap(tree, index, parent_index) # 부모 노드와 삽입된 노드의 위치 교환
        reverse_heapify(tree, parent_index) # 삽입된 노드를 대상으로 다시 reverse_heapify 호출


class PriorityQueue:
    """힙으로 구현한 우선순위 큐"""
    def __init__(self) -> None:
        self.heap = [None] # 파이썬 리스트로 구현한 힙
    
    def insert(self, data):
        self.heap.append(data) # 힙의 마지막에 데이터 추가
        reverse_heapify(self.heap, len(self.heap)-1) # 삽입된 노드(추가된 데이터)의 위치를 재배치

    def extract_max(self):
        """최우선순위 데이터 추출 메소드"""
        swap(self.heap, 1, len(self.heap)-1) # root 노드와 마지막 노드의 위치 바꿈
        value = self.heap.pop() # 힙에서 마지막 노드 추출(삭제)해서 변수에 저장
        heapify(self.heap, 1, len(self.heap)) # 새로운 root 노드를 대상으로 heapify 호출해서 힙 속성 유지

        return value # 최우선순위 데이터 리턴
    
    def __str__(self) -> str:
        return str(self.heap)

#---------------------------------------------------------------------------------------
# 실행 코드
priority_queue = PriorityQueue()

priority_queue.insert(6)
priority_queue.insert(9)
priority_queue.insert(1)
priority_queue.insert(3)
priority_queue.insert(10)
priority_queue.insert(11)
priority_queue.insert(13)

print(priority_queue)

print(priority_queue.extract_max())
print(priority_queue.extract_max())
print(priority_queue.extract_max())
print(priority_queue.extract_max())
print(priority_queue.extract_max())
print(priority_queue.extract_max())
print(priority_queue.extract_max())