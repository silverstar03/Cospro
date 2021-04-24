# 비밀번호
# def solution1(password):
#     capital_count, small_count, digit_count = 0,0,0
#     for p in password:
#         if p >='A' and p<='Z':
#             capital_count += 1
#         elif p>='a' and p<='z':
#             small_count += 1
#         elif p>= '0' and p <= '9':
#             digit_count += 1
#     if capital_count >= 1 and small_count >= 2 and digit_count >= 2:
#         return True
#     else:
#         return False
#
# password1="mirimworld"
# ret1 = solution1(password1)
# print("solution 함수의 반환 값은", ret1, "입니다.")
#
# password2="Mirim123"
# ret2 = solution1(password2)
# print("solution 함수의 반환 값은", ret2, "입니다.")



# 주민등록번호
# def mask_security_number(security_number):
#     security_number_list = list(security_number)
#     if len(security_number_list) == 14:
#         security_number_list[10:15] = ["*", "*", "*", "*"]
#     else:
#         security_number_list[9:14] = ["*", "*", "*", "*"]
#     return ''.join(security_number_list)
#
# def mask_security_number_ex(security_number):
#     return security_number[:len(security_number)-4]+"****"
#
# print(mask_security_number("880720-1234567"))
# print(mask_security_number("8807201234567"))
# print(mask_security_number_ex("930124-7654321"))
# print(mask_security_number_ex("9301247654321"))


# 특정문자
# def solution2(sentence):
#     result = []
#     for sen in sentence:
#         temp = ""
#         for s in sen:
#             if s in ",.?!":
#                 temp += s
#         if temp == "":
#             result.append("특정한 문자가 없습니다.")
#         else:
#             result.append(temp)
#     return result
#
# sentence = []
# n = int(input())
# for i in range(n):
#     sentence.append(input())
# result = solution2(sentence)
# print(result)



# 소수 구하기
# def prime(num):
#     if num < 2:
#         return False
#     for i in range(2,num):
#         if num%i == 0:
#             return False
#     return True
#
# n = 77
# print(prime(n))

# 입력한 숫자까지 중 소수 구하기
# def prime(num):
#     for i in range(2,num+1):
#         chk = True
#         for j in range(2, i):
#             if i%j == 0:
#                 chk = False
#                 break
#         if chk:
#             print(i, end=" ")
#
# n = int(input())
# print(prime(n))


# 피보나치 수열
def fibo(n):
    #return fibo(n-1) + fibo(n-2) if n >= 2 else n
    if n >= 2:
        return fibo(n-1) + fibo(n-2)
    else:
        return n

for n in range(0, 11):
    print(n, fibo(n))



# 섭씨 -> 화씨 서로 변환
# (0°C × 9/5) + 32 = 32°F
# def tempC(temp):
#      Ftemp = (temp * 9/5) + 32
#      return Ftemp

# 화씨 -> 섭씨 서로 변환
# (0°F - 32) * 5/9
# def tempF(temp):
#      Ctemp = (temp-32) * 5/9
#      return Ctemp

# a = int(input("섭씨 온도 : "))
# print("화씨 온도 : ", tempC(a))

# b = int(input("화씨 온도 : "))
# print("섭씨 온도 : ", tempF(b))



# 숫자 덧셈뺄셈
# def number(n):
#     n1 = int(n)
#     n2 = int(n[::-1])
#     sub = 0
#     if n1 > n2:
#         sub = n1 - n2
#     elif n1 < n2:
#         sub = n2 - n1
#     add = n1 + n2
#     print("덧셈에 대한 출력 : ", add)
#     print("뺄셈에 대한 출력 : ", sub)
#
# num = input("숫자 입력: ")
# number(num)


# 중복 문자 제거 후 출력
def solution3(characters):
   result = ""
   result += characters[0]
   for i in range(1, len(characters)):
       if characters[i - 1] != characters[i]:
           result += characters[i]
   return result

characters = "senteeeencccccceeee"
ret = solution3(characters)
print(ret)



# 중복 문자 True False
def solution4(characters):
   for i in range(1, len(characters)):
       if characters[i - 1] == characters[i]:
           return True

   return False

characters = "ad"
characters2 = "aaddcc"
ret = solution4(characters)
ret2 = solution4(characters2)
print(ret)
print(ret2)


# 중복 문자 개수
def strzip(sentence):
    result = ""
    result += sentence[0]
    count = 0

    for s in sentence:
        if s == result[-1]:
            count += 1
        else:
            result += str(count) + s
            count = 1
    result += str(count)
    return result

s = "aabbbbcccd"
print(strzip(s))