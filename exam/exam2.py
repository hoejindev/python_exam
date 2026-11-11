# 문제1 : 리스트에 순서대로 2, 1, 5, 6, 7를 한 번에 담아주세요.
# l = [2,1,5,6,7]
# print(l)

# 문제2 : 비어있는 리스트를 만들고, 순서대로 2, 1, 5, 6, 7를 하나씩 담아주세요.
# l = []

# l.append(2)
# l.append(1)
# l.append(5)
# l.append(6)
# l.append(7)

# print(l)

# 문제3 : 리스트에 순서대로 '월', '화', '수', '목', '금'을 한번에 담아주세요. 그리고 '+=' 연산자를 이용해서 '토', '일' 을 한번에 추가해주세요.
# days = ['월','화','수','목','금']
# days += ['토','일']

# print(days)

# 문제4 : 리스트에 순서대로 '월', '화', '수', '목', '금'을 한번에 담아주세요. 그리고 가장 마지막 요소를 출력해주세요.
# days = ['월','화','수','목','금']
# print(days[len(days)-1])

# 문제5 : 리스트에 순서대로 '월', '화', '수', '목', '금'을 한번에 담아주세요. 그리고 while문을 이용해서 요소 전부 출력해주세요.
# days = ['월','화','수','목','금']
# while days:
#     print(days.pop(0))

# 문제6 : 리스트에 순서대로 2, 1, '오', 6, 7를 한번에 담아주세요. 그리고 리스트 안에 있는 '오'를 정수 5로 변경해주세요.
# l = [2,1,'오',6,7]
# l[l.index('오')] =5
# print(l)

# 문제 7. 리스트에 순서대로 '월', '화', '수', '목', '금'을 한 번에 담아주세요. '화'가 리스트 안에 들어있는지 알려주세요.
# days = ['월','화','수','목','금']
# if '화' in days:
#     print("있다")
# else:
#     print("없다")

# 문제 8. 리스트에 순서대로 '월', '화', '수', '목', '금'을 한 번에 담아주세요. '화'가 리스트 안에서 몇 번째 데이터인지 알려주세요.
# days = ['월','화','수','목','금']
# print(days.index)

# 문제 9. 리스트에 순서대로 '월', '화', '수', '목', '금'을 한 번에 담아주세요. 리스트에 있는 '금'을 삭제하는 3가지 방법을 보여주세요.
# days = ['월','화','수','목','금']
# # del days[4]
# # del days[-1]
# # del days[days.index('금')]
# days.remove('금')
# print(days)

# 문제 1. 딕셔너리에 각 달의 마지막 날들을 한 번에 담기
# month_end_days = {'1월':31,
#                   '2월':28,
#                    '3월':31}
# print(month_end_days)

# 문제 2. 딕셔너리에 각 달의 마지막 날들을 반복문을 통해 담기
# month_end_days = {}

# for i in range(1, 12+1):
#     month = str(i)+"월"
#     end_day = 31

#     if i == 2:
#         end_day = 28
#     elif i in [4, 6, 9, 11]:
#         end_day = 30

#     month_end_days[month] = end_day

# print(month_end_days)

# 예제 1 문자열 슬라이싱
# print("== 예제 1 ==")
# s = "안녕하세요."
# #   [0,1,2,3,4,5]

# print("s길이 출력")
# print(len(s))

# print("s를 이루는 문장 중에서 앞에 거 2개 출력")
# print(s[0:2])
# print("s를 이루는 문장 중에서 문자 하나 건너 뛰고 1개 출력")
# print(s[1:2])
# print("s를 이루는 문장 중에서 문자 4개 출력")
# print(s[0:4])
# print("s를 이루는 문장 중에서 앞에 문자 3개 건너 뛰고 나머지 전체 출력")
# print(s[3:len(s)])
# print("s를 이루는 문장 중에서 앞에 문자 3개 건너 뛰고 뒤 인덱스 생략")
# print(s[3:])

# 예제 2 문자열 슬라이싱
# print("== 예제 2==")
# s = "안녕하세요."
# # print("s를 이루는 문자 하나씩 출력, while")
# # i=0
# # while i < len(s):
# #     print(s[i])
# #     i+=1

# # print("s를 이루는 문자 역순으로 하나씩 출력, while")
# # i=len(s)-1
# # while i >=0:
# #     print(s[i])
# #     i-=1

# print("s를 이루는 문자 하나씩 출력, for")
# for c in s:
#     print(c)

# 예제 3 문자열 슬라이싱
# print("== 예제 3==")
# s = "a안b녕c하d세e요f"

# print("s를 이루는 문장 중에서 한글만 출력")
# print(s[1]+s[3]+s[5]+s[7]+s[9])

# print("s를 이루는 문장 중에서 한글만 출력, for, if, or, continue")
# for c in s:
#     if c=='a' or c=='b' or c=='c' or c=='d' or c=='e' or c=='f':
#         continue
#     print(c)

# print("s를 이루는 문장 중에서 한글만 출력, for, if, and")
# for c in s:
#     if c!='a' and c!='b' and c!='c' and c!='d' and c!='e' and c!='f':
#         print(c)

# print("s를 이루는 문장 중에서 한글만 출력, for, not in")
# for c in s:
#     if c not in ['a','b','c','d','e','f']:
#         print(c)


# 예제 예외처리
# while True:
#     user_input = input("숫자를 입력하세요 (종료하려면 q 입력): ")

#     # q를 입력하면 반복문 종료
#     if user_input == "q":
#         print("프로그램을 종료합니다.")
#         break

#     try:
#         # 입력받은 문자열을 정수로 변환 시도
#         # 숫자가 아닌 문자열이면 ValueError 발생
#         number = int(user_input)

#         # 변환에 성공한 경우에만 실행
#         print("입력한 숫자:", number)

#     except ValueError:
#         # 정수로 변환할 수 없는 경우 실행
#         # 예외를 처리한 후 while문의 다음 반복 진행
#         print("숫자가 아닙니다. 다시 입력해주세요.")
#     except ZeroDivisionError:
#         print("0으로 나눌 수 없습니다.")
#     else:
#         print("예외 없음")
#     finally:
#         print("예외 처리 완료")

# 클래스 개념
# class Person:
#     def hello(self):
#         print('hi')

# jin = Person() #jin은 Person의 인스턴스
# jin.hello()

# class Person():
#     def hello(self):
#         print('hello')

#     def hi(self):
#         self.hello()

# jin = Person()
# jin.hi()

# class Person():
#     def __init__(self, name, age, hobby):
#         self.hello = '안녕하세요'
#         self.name = name
#         self.age = age
#         self.hobby = hobby

#     def introduce(self):
#         print(f"{self.hello}, 저는 {self.age}살 {self.name}입니다.")

# jin = Person('진', 22, '운동')
# jin.introduce()

# class Person:
#     pass

# jin = Person() # 인스턴스 생성
# jin.name = '진' # 인스턴스 생성한 뒤 속성 추가
# print(jin.name)

# class Person:
#     def __init__(self, name, age, weight):
#         self.name = name
#         self.age = age
#         self.__weight = weight

#     def diet(self, loss_weight):
#         self.__weight -= loss_weight
#         print(self.__weight)

# jin = Person('진', 22, 80)
# jin.diet(20)

# class Person():
#     def __init__(self, name, age, hobby):
#         self.hello = '안녕하세요'
#         self.name = name
#         self.age = age
#         self.hobby = hobby

# 클래스 속성
class Person:
    def __init__(self):
        self.folder = [] # 인스턴스 속성

    def add_files(self, file):
        self.folder.append(file)

jin = Person()
jin.add_files('txt')

kim = Person()
kim.add_files('img')

print(jin.folder)
print(kim.folder)
print("hello")
print("hi")
