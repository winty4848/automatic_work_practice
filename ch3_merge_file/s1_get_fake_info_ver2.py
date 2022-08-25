import time
import random
import os
from datetime import datetime

print("가상정보 생성 시작")

# 처리시간 출력용
start_time=time.time()

# 정보 생성 개수 제어
num_sample=1000

# 메일, 메일도메인, 이름 생성용
alphabet_list="abcdefghizklmnopqrstuvwxyz1234567890"
domain_list=["naver","google","nate","kakao","tistory"]
first_name_samples = "김이박유최정전강조윤장임한서신황안"
middle_name_samples = "민서예지도하주윤채현"
last_name_samples = "준윤우원호효후서연현아은진희"

# 현재 시간 저장
now = datetime.now()
now_year=now.year

# 영어글자 생성
def random_string(length):
    result = ""
    for i in range(length):
        result += random.choice(alphabet_list)
    return result

# 이름 생성
def random_name():
    result = ""
    result += random.choice(first_name_samples)
    result += random.choice(middle_name_samples)
    result += random.choice(last_name_samples)
    return result

# 결과물 저장할 폴더 생성
os.mkdir("personal_fake_info")

for i in range(num_sample):
    name=random_name()

    # 결과물 파일에 이름 붙이기(F2 누른거랑 같음)
    filename = "personal_fake_info/" + str(i) + "_" + name + ".txt"

    # 파일 생성
    outfile = open(filename, 'w')

    outfile.write("이름 : " + name + "\n")

    # 20이상 60이하 정수를 뽑아 나이를 설정
    # concat은 문자데이터만 됨.
    age=random.randint(22, 60)

    outfile.write("나이 : " + str(age) + "\n")

    # 양식 통일하기 위해서 10 이하 수는 0 문자값 부여.
    temp_month = random.randint(1,12)
    if temp_month<10:
        temp_month="0"+str(temp_month)
    else:
        temp_month=str(temp_month)

    # 2월 윤달 설정하기 귀찮아서 그냥 일은 1~27까지만 나오게 함...
    temp_date = random.randint(1,27)
    if temp_date<10:
        temp_date="0"+str(temp_date)
    else:
        temp_date=str(temp_date)
    outfile.write("입사일 : " + str(now_year-age+20+random.randint(0,age-20)) + '-' + str(temp_month) + '-' + str(temp_date) + "\n")

    # 미리 설정해둔 도메인 중에서 하나 뽑아 이메일 구성
    outfile.write("e-mail : " + random_string(random.randint(5, 12)) + "@" + random.choice(domain_list) + ".com\n")

    # 속도가 빨라서 그런지 시간값 이용하면 결과물이 뭉텅이로 비슷해지는 이슈 발견
    # 그냥 시간값이랑 섞어서 random int 부여해줌
    outfile.write("전화번호 : 010-" + str(time.time())[-4:] + "-" + str(random.randint(0,9)) + str(time.time())[-6:-4] + str(random.randint(0,9)) + str(random.randint(0,9)) + '\n')

    outfile.write("성별 : " + random.choice(["남", "여"]))

    outfile.close()

print("가상정보 생성 끝")
end_time=time.time()
print("소요시간 : " + str(end_time-start_time) + "초")