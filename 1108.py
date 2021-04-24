# def solution(speed, cars):
#     answer = 0
#     for x in cars:
#         if x >= speed * 11 / 10 and x < speed * 12 / 10:
#             answer += 3
#         elif x >= speed * 12 / 10 and x < speed * 13 / 10:
#             answer += 5
#         elif x >= speed * 13 / 10:
#             answer += 7
#     return answer
#
# speed = 110
# cars = [99, 88, 77, 100, 111, 120]
# ret = solution(speed, cars)
#
# print("solution 함수의 반환 값은", ret, "입니다.")


def solution(point):
   if point < 1000:
       return 0
   return point // 100 * 100

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래에는 잘못된 부분이 없으니, 위의 코드만 수정하세요.
point = 2323
ret = solution(point)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
