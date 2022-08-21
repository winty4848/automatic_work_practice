import time
import random
import os

print("가상정보 생성 시작")

# 처리시간 출력용
start_time=time.time()

# 정보 생성 개수 제어
num_sample=1000

# 메일, 메일도메인, 이름 생성용
alphabet_list="abcdefghizklmnopqrstuvwxyz1234567890"
domain_list=["naver","google","nate","kakao","tistory"]
first_name_samples = "김이박최정강조윤장임"
middle_name_samples = "민서예지도하주윤채현지"
last_name_samples = "준윤우원호후서연아은진"

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

    # 결과물 파일 이름 정하기
    filename = "personal_fake_info/" + str(i) + "_" + name + ".txt"

    # 파일 생성
    outfile = open(filename, 'w')

    # 결과물 파일에 이름 붙이기(F2 누른거랑 같음)
    outfile.write("name : " + name + "\n")

    # 20이상 60이하 정수를 뽑아 나이를 설정
    # concat은 문자데이터만 됨.
    outfile.write("age : " + str(random.randint(20, 60)) + "\n")

    # 미리 설정해둔 도메인 중에서 하나 뽑아 이메일 구성
    outfile.write("e-mail : " + random_string(random.randint(5, 12)) + "@" + random.choice(domain_list) + ".com\n")

    outfile.write("telephone : 010-" + str(time.time())[-4:] + "-" + str(time.time())[-6:-2] + '\n')
    outfile.write("sex : " + random.choice(["male", "female"]))

    outfile.close()

print("가상정보 생성 끝")
end_time=time.time()
print("소요시간 : " + str(end_time-start_time) + "초")