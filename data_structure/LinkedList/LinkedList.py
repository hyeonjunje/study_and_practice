class Node:
    """링크드 리스트의 노드 클래스"""
    def __init__(self, data) -> None:
        self.data = data # 노드가 저장하는 데이터
        self.next = None # 다음 노드에 대한 레퍼런스


class LikedList:
    """링크드 리스트 클래스"""

    def __init__(self) -> None:
        self.head = None
        self.tail = None


    def pop_left(self):
        """링크드 리스트의 가장 앞 노드 삭제 메소드. 단, 링크드 리스트에 항상 노드가 있다고 가정한다."""
        # 지우려는 데이터가 링크드 리스트의 마지막 남은 데이터일 때
        data = self.head.data # 삭제할 노드를 미리 저장해놓는다.

        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            # 리크드 리스트의 head를 지금 head의 다음 노드로 지전해준다
            self.head = self.head.next

        return data # 삭제된 노드의 데이터를 리턴한다.

    def delete_after(self, previous_node):
        """링크드 리스트 삭제연산. 주어진 노드 뒤 노드를 삭제한다."""
        data = previous_node.next.data

        # 지우려는 노드가 tail 노드일 때:
        if previous_node.next is self.tail:
            previous_node.next = None
            self.tail = previous_node
        # 두 노드 사이 노드를 지울 때
        else:
            previous_node.next = previous_node.next.next
        
        return data # 삭제하는 노드의 값을 리턴하는 것이 delete의 관습

        


    def prepend(self, data):
        """링크드 리스트의 가장 앞에 데이터 삽입"""
        new_node = Node(data)

        # 링크드 리스트가 비었는지 확인
        if self.head is None:
            # 새 노드를 링크드 리스트의 유일한 노드로 만들어준다.
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head # 새로운 노드의 다음 노드를 head 노드로 정해주고
            self.head = new_node # 리스트의 hed_node를 새롭게 삽입한 노드로 정해준다.


    def insert_after(self, previous_node, data):
        """링크드 리스트 주어진 노드 뒤 삽입 연산 메소드"""
        new_node = Node(data)

        # 가장 마지막 순서 삽입
        if previous_node is self.tail:
            previous_node.next = new_node
            self.tail = new_node
        else: # 두 노드 사이에 삽입
            new_node.next = previous_node.next
            previous_node.next = new_node


    def find_node_at(self, index):
        """링크드 리스트 덥근 연산 메소드. 파라미터 인덱스는 항상 있다고 가정"""
        iterator = self.head

        for _ in range(index):
            iterator = iterator.next
        
        return iterator


    def append(self, data):
        """링크드 리스트 추가 연산 메소드"""
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node


    def __str__(self) -> str:
        """링크드 리스트를 문자열로 표현해서 리턴하는 메소드"""
        res_str = "|"

        # 링크드 리스트 안에 모든 노드를 돌기 워한 변수. 일단 가장 앞 노드로 정의한다.
        iterator = self.head

        # 링크드 리스트 끝까지 돈다
        while iterator is not None:
            # 각 노드의 데이터를 리턴하는 문자열에 더해준다.
            res_str += f" {iterator.data} |"
            iterator =iterator.next # 다음 노드로 넘어간다.

        return res_str

#------------------------------------------------------------------------------------
# 데이터 2, 3, 5, 7, 11을 담는 노드들 생성

# head_node = Node(2)
# node_1 = Node(4)
# node_2 = Node(5)
# node_3 = Node(7)
# tail_node = Node(11)

# # 노드들을 연결
# head_node.next = node_1
# node_1.next = node_2
# node_2.next = node_3
# node_3.next = tail_node

#------------------------------------------------------------------------------------
# 새로운 링크드 리스트 생성 
my_list = LikedList()
my_list.append(2)
my_list.append(3)
my_list.append(5)
my_list.append(7)
my_list.append(11)

print(my_list)

#------------------------------------------------------------------------------------
# 링크드 리스트 접근 

# print(my_list.find_node_at(3).data)
# my_list.find_node_at(2).data = 13

#------------------------------------------------------------------------------------
# 삽입과 삭제

# node_2 = my_list.find_node_at(2) # 인덱스 2에 있는 노드 접근
# my_list.insert_after(node_2, 6) 인덱스 2 뒤 데이터 6 삽입
# my_list.delete_after(node_2) # 인덱스 2 뒤 데이터 삭제

# print(my_list)

# second_to_last_node = my_list.find_node_at(2) # 맨 끝에서 두 번째 노드 접근
# print(my_list.delete_after(second_to_last_node)) # 삭제하는 노드의 값 출력

# print(my_list)

#------------------------------------------------------------------------------------
# popleft : 링크드 리스트 가장 앞 삭제

my_list.pop_left()

print(my_list)

#------------------------------------------------------------------------------------