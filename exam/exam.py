# 1 일차 
# 문제 : 함수를 사용해서 코드량을 확 줄여주세요.

# def gugudan(dan):
   
#     i = 1
#     while i <= 9:
#         print("{} * {} = {}".format(dan, i, dan * i))
#         i += 1


# for i in range(1,10):
#     print("== 구구단 {}단 출력 ==".format(i))
#     gugudan(i)


# 문제 : 입력받은 정수가 소수인지 아닌지 알려주는 함수를 구현해주세요.

def is_prime_number(num):
  
  for i in range(2, num):
      if num % i == 0:
          return False
            
  return True

print("3은 소수입니다 : {}".format(is_prime_number(3)))
print("4는 소수입니다 : {}".format(is_prime_number(4)))
print("5는 소수입니다 : {}".format(is_prime_number(5)))
print("6는 소수입니다 : {}".format(is_prime_number(6)))
print("7는 소수입니다 : {}".format(is_prime_number(7)))
print("1000은 소수입니다 : {}".format(is_prime_number(1000)))