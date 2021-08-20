

class Node:
    """이진 트리 노드 클래스"""
    def __init__(self, data) -> None:
        """데이터와 두 자식 노드에 대한 레퍼런스를 갖는다."""
        self.data = data
        self.parent = None
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
# priority_queue = PriorityQueue()

# priority_queue.insert(6)
# priority_queue.insert(9)
# priority_queue.insert(1)
# priority_queue.insert(3)
# priority_queue.insert(10)
# priority_queue.insert(11)
# priority_queue.insert(13)

# print(priority_queue)

# print(priority_queue.extract_max())
# print(priority_queue.extract_max())
# print(priority_queue.extract_max())
# print(priority_queue.extract_max())
# print(priority_queue.extract_max())
# print(priority_queue.extract_max())
# print(priority_queue.extract_max())

#---------------------------------------------------------------------------------------
# BinarySearchTree

class BinarySearchTree:
    """이진 탐색 트리 클래스"""
    def __init__(self) -> None:
        self.root = None

    def delete(self, data):
        """이진 탐색 트리 삭제 메소드"""
        node_to_delete = self.search(data) # 삭제할 노드를 가지고 온다.
        parent_node = node_to_delete.parent # 삭제할 노드의 부모 노드

        # 경우 1: 지우려는 노드가 leaf 노드일 때
        if node_to_delete.left_child is None and node_to_delete.right_child is None:
            if self.root is node_to_delete:
                self.root = None
            else: # 일반적인 경우
                if node_to_delete is parent_node.left_child:
                    parent_node.left_child = None
                else:
                    parent_node.right_child = None
        
        # 경우 2: 지우려는 노드가 자식이 하나인 노드일 때
        elif node_to_delete.left_child is None: # 지우려는 노드가 오른쪽 자식만 있을 때
            # 지우려는 노드가 root 노드일 때
            if node_to_delete is self.root:
                self.root = node_to_delete.right_child
                self.root.parent = None
            # 지우려는 노드가 부모의 왼쪽 자식일 때
            elif node_to_delete is parent_node.left_child:
                parent_node.left_child = node_to_delete.right_child
                node_to_delete.right_child.parent = parent_node
            # 지우려는 노드가 부모의 오른쪽 자식일 때
            else:
                parent_node.right_child = node_to_delete.right_child
                node_to_delete.right_child.parent = parent_node
        
        elif node_to_delete.right_child is None: # 지우려는 노드가 왼쪽 자식만 있을 때
            # 지우려는 노드가 root 노드일 때
            if node_to_delete is self.root:
                self.root = node_to_delete.left_child
                self.root.parent = None
            # 지우려는 노드가 부모의 왼쪽 자식일 때
            elif node_to_delete is parent_node.left_child:
                parent_node.left_child = node_to_delete.left_child
                node_to_delete.left_child.parent = parent_node
            # 지우려는 노드가 부모의 오른쪽 자식일 때
            else:
                parent_node.right_child = node_to_delete.left_child
                node_to_delete.left_child.parent = parent_node

        # 경우 3: 지우려는 노드가 2개의 자식이 있을 때
        else:
            successor = self.find_min(node_to_delete.right_child)
            self.delete(successor.data)
            node_to_delete.data = successor.data
            
    @staticmethod
    def find_min(node):
        """(부분)이진 탐색 트리의 가장 작은 노드 리턴"""
        temp = node  # 탐색 변수. 파라미터 node로 초기화

        # temp가 node를 뿌리로 갖는 부분 트리에서 가장 작은 노드일 때까지 왼쪽 자식 노드로 간다
        while temp.left_child is not None:
            temp = temp.left_child      

        return temp 


    def search(self, data):
        """이진 탐색 트리 탐색 메소드, 찾는 데이터를 갖는 노드가 없으면 None을 리턴한다."""
        temp = self.root # 탐색용 변수, root 노드로 초기화

        # 원하는 데이터를 갖는 노드를 찾을 때까지 돈다.
        while temp is not None:
            # 원하는 데이터가 노드의 데이터보다 작으면 왼쪽 자식 노드로 간다.
            if data < temp.data:
                temp = temp.left_child
            # 원하는 데이터가 노드의 데이터보다 크면 오른쪽 자식 노드로 간다.
            elif data > temp.data:
                temp = temp.right_child
            # 원하는 데이터를 갖는 노드를 찾으면 리턴
            else:
                return temp

        return None # 원하는 데이터가 트리에 없으면 None 리턴


    def insert(self, data):
        """이진 탐색 트리 삽입 메소드"""
        new_data = Node(data) # 삽입할 데이터를 갖는 노드 생성

        # 트리가 비었으면 새로운 노드를 root 노드로 만든다.
        if self.root == None:
            self.root = new_data
            return 

        
        temp = self.root # 저장하려는 위치를 찾기 위해 사용할 변수, root 노드로 초기화한다.

        # 원하는 위치를 찾아간다.
        while temp is not None:
            if data < temp.data: # 삽입하려는 데이터가 현재 노드 데이터보다 크다면
                # 오른쪽 자식이 없으면 새로운 노드를 현재 노드 오른쪽 자식으로 만듦
                if temp.left_child is None:
                    new_data.parent = temp
                    temp.left_child = new_data
                    return 
                # 오른쪽 자식이 있으면 오른쪽 자식으로 간다.
                else:
                    temp = temp.left_child
            else: # 삽입하려는 데이터가 현재 노드 데이터보다 작다면
                # 왼쪽 자식이 없으면 새로운 노드를 현재 노드 왼쪽 자식으로 만듦
                if temp.right_child is None:
                    new_data.parent = temp
                    temp.right_child = new_data
                    return
                # 왼쪽 자식이 있다면 왼쪽 자식으로 간다.
                else:
                    temp = temp.right_child

    def print_sorted_tree(self):
        """이진 탐색 트리 내의 데이터를 정렬된 순서로 출력해주는 메소드"""
        traverse_inorder(self.root)

#---------------------------------------------------------------------------------------

# 비어 있는 이진 탐색 트리 생성
bst = BinarySearchTree()

# 데이터 삽입
bst.insert(7)
bst.insert(11)
bst.insert(9)
bst.insert(17)
bst.insert(8)
bst.insert(5)
bst.insert(19)
bst.insert(3)
bst.insert(2)
bst.insert(4)
bst.insert(14)
# 이진 탐색 트리 출력
bst.print_sorted_tree()
print("-------------------------------------------------------")

print(bst.search(7).data)
print(bst.search(19).data)
print(bst.search(2).data)
print(bst.search(20))
print("-------------------------------------------------------")
# # leaf 노드 삭제
# bst.delete(2)
# bst.delete(4)
# # 자식이 하나만 있는 노드 삭제
# bst.delete(5)
# bst.delete(9)
# 자식이 두 개 다 있는 노드 삭제
bst.delete(7)
bst.delete(11)

bst.print_sorted_tree()