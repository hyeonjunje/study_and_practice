# deque 는 파이썬 collections 모듈에서 가지고 온다.
from collections import deque

# -----------------------------------------------------------------------------------------------
# deque 써보기
# queue = deque()

# # 큐의 맨 끝에 데이터 삽입
# queue.append("태호")
# queue.append("현승")
# queue.append("지웅")
# queue.append("동욱")
# queue.append("신의")

# print(queue) # 큐 출력

# # 큐의 가장 앞 데이터에 접근
# print(queue[0])

# # 큐 맨 앞 데이터 삭제
# print(queue.popleft())
# print(queue.popleft())
# print(queue.popleft())

# print(queue)

# -----------------------------------------------------------------------------------------------
class CustomerComplaint:
    """고객 센터 문의를 나타내는 클래스"""
    def __init__(self, name, email, content) -> None:
        self.name = name
        self.email = email
        self.content = content

class CustomerServiceCenter:
    """호텔 서비스 센터 클래스"""
    def __init__(self) -> None:
        self.queue = deque() # 대기 중인 문의를 저장할 큐 생성

    def process_complaint(self):
        """접수된 고객 센터 문의 내용 처리하는 메소드"""
        if self.queue:  # 대기 중인 문의가 있는지 확인
            """
            파이썬 deque(를 비롯한 다른 여러 데이터 항목을 담는 자료형과 마찬가지로)
            이 비었는지 확인하는 방법은 if 뒤에 deque 인스턴스를 넣으면 됨
            """
            complaint = self.queue.popleft()
            print(f"{complaint.name}님의 {complaint.content} 문의 내용 접수 되었습니다. 담당자가 배정되면 {complaint.email}로 연락드리겠습니다!")
        else:
            print("더 이상 대기 중인 문의가 없습니다!")

    def add_complaint(self, name, email, content):
        """새로운 문의를 큐에 추가 시켜주는 메소드"""
        new_complaint = CustomerComplaint(name, email, content)
        self.queue.append(new_complaint)
        

# -----------------------------------------------------------------------------------------------

# 고객 문의 센터 인스턴스 생성
# center = CustomerServiceCenter()

# # 문의 접수한다
# center.add_complaint("강영훈", "younghoon@codeit.com", "음식이 너무 맛이 없어요")

# # 문의를 처리한다
# center.process_complaint()
# center.process_complaint()

# # 문의 세 개를 더 접수한다
# center.add_complaint("이윤수", "yoonsoo@codeit.kr", "에어컨이 안 들어와요...")
# center.add_complaint("손동욱", "dongwook@codeit.us", "결제가 제대로 안 되는 거 같군요")
# center.add_complaint("김현승", "hyunseung@codeit.ca", "방을 교체해주세요")

# # 문의를 처리한다
# center.process_complaint()
# center.process_complaint()

# -----------------------------------------------------------------------------------------------
# stack

# stack = deque()
# # stack = [] # deque 말고 list를 써도 시간복잡도나 결과가 같다.

# # 스택 맨 끝에 데이터 추가
# stack.append("T")
# stack.append("a")
# stack.append("e")
# stack.append("h")
# stack.append("o")

# print(stack) # 스택 출력

# # 맨 끝 데이터 접근
# print(stack[-1])

# # 맨 끝 데이터 삭제
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())

# print(stack)

# -----------------------------------------------------------------------------------------------
# 괄호 짝 확인하기
def parentheses_checker(string):
    """주어진 문자열 인풋의 모든 괄호가 짝이 있는지 확인해주는 메소드"""
    
    print(f"테스트하는 문자열: {string}")
    stack = deque()

    # 문자열의 각 문자르 돌면서
    for i in range(len(string)):
        # 열리는 괄호가 있는 위치를 스택에 저장한다.
        if string[i] == "(":
            stack.append(i)
        # 닫히는 괄호가 있으면
        elif string[i] == ")":
            # 스택에 열린 괄호 위치 데이터가 있으면 삭제하고
            if stack:
                stack.pop()
            # 아니면 현재 위치에 있는 닫는 괄호에 맞는 열리는 괄호가 없다고 출력한다.
            else:
                print(f"문자열 {i} 번째 위치에 있는 닫는 괄호에 맞는 여는 괄호가 없습니다")
    
    # 스택에 열린 괄호 위치 데이터가 남아 있으면 해당 괄호는 짝이 맞는 닫힌 괄호가 없다는 뜻이다.
    while stack:
        print(f"문자열 {stack.pop()} 번째 위치에 있는 괄호가 닫히지 않았습니다")

case1 = "(1+2)*(3+5)"
case2 = "((3*12)/(41-31))"
case3 = "((1+4)-(3*12)/3"
case4 = "(12-3)*(56/3))"
case5 = ")1+14)/3"
case6 = "(3+15(*3"

parentheses_checker(case1)
parentheses_checker(case2)
parentheses_checker(case3)
parentheses_checker(case4)
parentheses_checker(case5)
parentheses_checker(case6)