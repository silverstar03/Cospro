# 1
letters = 'python'

print(letters[0], letters[2])

# 2
license_plate = "24가 2210"

print(license_plate[4:])

def 문자열쪼개기(license_plate):
    result =""
    for i in range(len(license_plate)-4, len(license_plate)):
        result += license_plate[i]
    return result

a = 문자열쪼개기(license_plate)
print(a)


# 3
phone_number = "010-1111-2222"

print(phone_number.replace("-"," "))

# 4
url = "http://sharebook.kr"

b = url.split(".")[-1]
print(b)

# 5
t1 = 'python'
t2 = 'java'

print((t1 + " " + t2 + " ")*3)
c = ((t1+" "+t2+" ")*4)[:-1]
print(c)

# 6
상장주식수 = "5,969,782,550"
상장주식수 = int(상장주식수.replace(",",''))
print(상장주식수)

# 7
ticker = "btc_krw"
ticker = ticker.split("_")
print(ticker)
t3 = ticker[:3]
t4 = ticker[-3:]
print(t3)
print(t4)

# 8
movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
movie_rank.append("배트맨")
print(movie_rank)

# 9
movie_rank.insert(1, "슈퍼맨")
print(movie_rank)

# 10
movie_rank.pop(3)
# movie_rank.remove('럭키')
print(movie_rank)

# 11
nums = [1, 2, 3, 4, 5]

sum11 = 0
for i in nums:
    sum11 += i
print(sum11)

# 12
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]
print(len(cook))
# 중복된 거 제외
a12 = dict()
for x in cook:
    a12[x] = 1

print(len(a12))

# 13
nums = [1,2,3,4,5]
sum13 = 0
for i in nums:
    sum13 += i
sum13 /= len(nums)
print(sum13)

# 14
nums14 = [1,2,3,4,5]
print(nums14[::-1])

# 15
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']

print("/".join(interest))

# 16
string = "삼성전자/LG전자/Naver"

interest = string.split("/")
print(interest)

# 17
data = [2, 4, 3, 1, 5, 10, 9]
data.sort()
print(data)

# 18
a18 = input("현재시간 : ")
print(a18[-2:])
if a18[-2:] == "00":
    print("정각 입니다.")
else :
    print("정각이 아닙니다.")

# 19
리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']

for i in 리스트:
    if i[-2:] == ".h":
        print(i)

# 20
for i in range(10):
    print(i/10)

# 21
apart = [ [101, 102], [201, 202], [301, 302]]

for i in apart:
    for j in i:
        print(j, "호")

# 22
def pickup_even(pickup_even):
    result = []
    for i in pickup_even:
        if i % 2 == 0:
            result.append(i)
    return result

print(pickup_even([3, 4, 5, 6, 7, 8]))
