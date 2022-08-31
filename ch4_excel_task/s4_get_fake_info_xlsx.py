# ch3_s7과 ch4_s1을 짬뽕한 느낌

import time
import random
import os
import pyexcel as px

print("가상정보 생성 시작")

# 처리시간 출력용
start_time = time.time()

# 정보 생성 개수 제어
num_sample = 1000

# 메일, 메일도메인, 이름 생성용
alphabet_list = "abcdefghizklmnopqrstuvwxyz1234567890"
domain_list = ["naver", "google", "nate", "kakao", "tistory"]
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

# csv때와 마찬가지로 헤더를 그냥 미리 정의한다.
header = ["name", "age", "e-mail", "telephone", "sex"]

for i in range(num_sample):
    name = random_name()

    # 결과물 파일에 이름 붙이기(F2 누른거랑 같음)
    filename = "personal_fake_info/" + str(i) + "_" + name + ".xlsx"

    # 실행할 때마다 초기화해서 실행시마다 깨끗한 곳에 정보를 넣어주자
    temp_content=[]

    temp_content.append(name)
    temp_content.append(str(random.randint(20, 60))) ##### int형으로 넣어주면 엑셀에서도 문자값아니라 숫자값으로 인식함. 참고하시길
    temp_content.append(random_string(random.randint(5, 12)) + "@" + random.choice(domain_list) + ".com")
    temp_content.append("010-" + str(time.time())[-4:] + "-" + str(time.time())[-6:-2])
    temp_content.append(random.choice(["male", "female"]))

    temp_result=[header, temp_content]

    # dest_file=destination file(디렉토리)
    px.save_as(array=temp_result, dest_file_name=filename)

# 저자는 csv 생성보다 약 30배 처리시간 증가한다고 함. 나의 똥컴으로 실행했을 땐 약 24초 소요,,,
print("가상정보 생성 끝")
end_time = time.time()
print("소요시간 : " + str(end_time - start_time) + "초")