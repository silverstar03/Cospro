# 1
# def 문자열대체(str, old, new):
#     result = ""
#     for i in str:
#         if i == old:
#             i = new
#         result += i
#     return result
#
#
# phone_number = "010-1111-2222"
# a = 문자열대체(phone_number, "-"," ")
# print(a)

# 2
# def 문자열쪼개기(string, sep):
#     list = []
#     str =""
#
#     for i in string:
#         if i == sep:
#             list.append(str)
#             str = ""
#             continue
#         else:
#             str += i
#     list.append(str)
#
#     return list
#
#
# phone_number = "010-1111-2222"
# a = 문자열쪼개기(phone_number, "-")
# print(a)

# 3
# def 아이템삽입(src, index, object):
#     list = []
#
#     for i in range(0, index):
#         list.append(src[i])
#     list.append(object)
#     for i in range(index, len(src)):
#         list.append(src[i])
#
#
#     return list
#
#
# movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']
# a = 아이템삽입(movie_rank, 1, "슈퍼맨")
#
# print(a)

# 4
# def 특정아이템삭제(src, object):
#     list = []
#     flag = False
#
#     for i in src:
#          if i == object and flag == False:
#              flag = True
#              continue
#          else:
#             list.append(i)
#
#     return list
#
# movie_rank = ['럭키', '스플릿', '럭키', '배트맨']
# a = 특정아이템삭제(movie_rank, "럭키")
#
# print(a)


# 5
# def 특정아이템모두삭제(src, object):
#     list = []
#     for i in src:
#         if i == object:
#             continue
#         list.append(i)
#     return list
#
#
# movie_rank = ['럭키', '스플릿', '럭키', '배트맨']
# a = 특정아이템모두삭제(movie_rank, "럭키")
#
# print(a)

# 6
# def 평균(src):
#     sum = 0
#     avg = 0
#     cnt = 0
#
#     for i in src:
#         sum += i
#         cnt += 1
#
#     avg = sum/cnt
#
#     return avg
#
# 리스트 = [1,2,3,4,5]
# a = 평균(리스트)
#
# print(a)


# 7
# def 조인(string, iterable):
#     str = ""
#     for i in iterable:
#         str += i
#         str += string
#
#     return str[:-1]
#
# 리스트 = ["내", "pc", "지키미"]
# a = 조인("/", 리스트)
#
# print(a)