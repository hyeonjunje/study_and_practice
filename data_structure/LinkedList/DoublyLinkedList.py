class Node:
    """더블리 링크드 리스트의 노드 클래스"""
    def __init__(self, data) -> None:
        self.data = data # 노드가 저장하는 데이터
        self.next = None # 다음 노드에 대한 레퍼런스
        self.prev = None # 이전 노드에 대한 레퍼런스

        
class LikedList:
    """더블리 링크드 리스트 클래스"""

    def __init__(self) -> None:
        self.head = None
        self.tail = None


    def delete(self, node_to_delete):
        """더블리 링크드 리스트 삭제 연산 메소드 next, prev가 있기 때문에 이전 인덱스가 아닌 삭제할려는 인덱스를 파라미터로 사용"""
        
        # 링크드 리스트에서 마지막 남은 데이터를 삭제할 때
        if node_to_delete is self.head and node_to_delete is self.tail:
            self.head = None
            self.tail = None
        
        # 링크드 리스트 가장 앞 데이터 삭제할 때
        elif node_to_delete is self.head:
            self.head = node_to_delete.next
            node_to_delete.next.prev = None

        # 링크드 리스트 가장 뒤 데이터 삭제할 때
        elif node_to_delete is self.tail:
            self.tail = node_to_delete.prev
            node_to_delete.prev.next = None
        
        # 두 노드 사이에 있는 데이터 삭제할 때
        else:
            node_to_delete.prev.next = node_to_delete.next
            node_to_delete.next.prev = node_to_delete.prev

        # 삭제하는 노드 데이터 리턴
        return node_to_delete.data

    def prepend(self, data):
        """링크드 리스트 가장 앞에 데이터를 추가시켜주는 메소드"""
        new_node = Node(data) # 새로운 노드 생성

        # 링크드 리스트가 비었을 때
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            # 링크드 리스트가 안 비었을 때
            new_node.next = self.head # 새로운 노드의 다음 노드를 head 노드로 지정
            self.head.prev = new_node # head 노드의 전 노드를 새로운 노드로 지정
            self.head = new_node # head 노드 업데이트            
    

    def insert_after(self, previous_node, data):
        """더블리 링크드 리스트 삽입 연산"""
        new_node = Node(data) # 새로운 노드 생성

        # tail 노드 다음에 노드를 삽입할 때
        if previous_node is self.tail:
            previous_node.next = new_node # 새로운 노드를 tail 노드의 다음 노드로 지정한다.
            new_node.prev = previous_node # tail 노드를 새로운 노드의 전 노드로 지정한다.
            self.tail = new_node # 새로운 노드를 tail 노드로 지정한다.
        else:
            # 새롭게 생성한 노드를 이미 있는 링크드 리스트에 연결시키고
            new_node.next = previous_node.next
            new_node.prev = previous_node
            # 이미 있는 노드들의 앞과 다음 레퍼런스를 새롭게 생성한 노드로 지정한다.
            previous_node.next.prev = new_node 
            previous_node.next = new_node
      


    def append(self, data):
        """링크드 리스트 추가 연산 메소드"""
        new_node = Node(data) # 새로운 데이터를 저장하는 노드

        # 링크드 리스트가 비어 있는 경우
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else: # 링크드 리스트에 데이터가 이미 있는 경우
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node


    def find_node_at(self, index):
        """더블리 링크드 리스트 덥근 연산 메소드. 파라미터 인덱스는 항상 있다고 가정"""
        iterator = self.head

        for _ in range(index):
            iterator = iterator.next
        
        return iterator


    def __str__(self) -> str:
        """더블리 링크드 리스트를 문자열로 표현해서 리턴하는 메소드"""
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
# 빈 링크드 리스트 정의
my_list = LikedList()

# 링크드 리스트에 데이터 추가
my_list.append(2)
my_list.append(3)
my_list.append(5)
my_list.append(7)

print(my_list)
#------------------------------------------------------------------------------------
# 삽입 
# node_1 = my_list.find_node_at(1)
# my_list.insert_after(node_1, 10)
# print(my_list)
#------------------------------------------------------------------------------------
# prepend 가장 앞에 데이터를 추가시키기
# my_list.prepend(30)
# print(my_list)
#------------------------------------------------------------------------------------
# delete 삭제
node_2 = my_list.find_node_at(2)
print(my_list.delete(node_2))
print(my_list)
#------------------------------------------------------------------------------------