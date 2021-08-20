import collections

# 1. Counter 클래스

a = "hello world"

def countLetters(word):
    counter = {}
    for letter in word:
        if letter not in counter:
            counter[letter] = 0
        counter[letter] += 1
    return counter
print(countLetters(a))

# 위에 함수를 한 줄로 줄일 수 있다.
print(dict(collections.Counter(a)))

# Counter 클래스의 most_common(n) 함수 
# 입력된 값의 요소들 중 빈도수가 높은 순으로 상위 n개를 리스트 안의 튜플 형태로 반환
print(collections.Counter(a).most_common(3))

# Counter 클래스의 update(iterable - or - mapping) 함수 
# Counter의 값을 갱신
c = collections.Counter() # 빈 카운터 생성
c.update("abracadabra")
c.update(cat = 4, dog = 8)
print(c)

# Counter 끼리 덧셈, 뺄셈, 교집합, 합집합이 가능
b = collections.Counter("aaaabb")
print(c-b) # 뺄셈  Counter의 뺄셈은 음수값은 출력하지 않는다.
print(c+b) # 덧셈
print(c|b) # 합집합
print(c&b) # 교집합

