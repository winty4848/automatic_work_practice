#책의 s2는 유용성이 적어서 (ch3_s2과 코드는 같은데 확장자만 다름) 패스하고 s3만 다룸.

#-*-coding:euc-kr

import time
import os

print("가즈아")

start_time=time.time()

# 합칠 파일들이 저장된 폴더명
directory="personal_fake_info"

# 단일화된 파일 이름 정의
output_name="merge_ID.csv"

# 결과물 파일 생성
output=open(output_name, 'w')
output_header = False # 초기값 F 지정

# 폴더 내용물 리스트 생성. 실제로 타입 출력해보니 파일명이 list형에 넣어져있음.
# 다만 정렬이 1, 101, 102, ... 이런식으로 뒤바뀌어있음. 1,2,3, ... 순서를 지켜야한다면 파일 생성단부터 바꾸던가 해야할듯
input_files=os.listdir(directory)

for filename in input_files:
    if ".csv" not in filename:
        continue
    file=open(directory + "/" + filename)
    # 지금은 각 파일마다 헤더가 있는 상황이니 분리해주도록 하자.
    # readline()은 1번째 수행이면 첫행, 2번째 수행이면 두번째행 읽어준다
    header=file.readline()
    if not output_header:
        output.write(header.strip())
        output_header=True
    output.write("\n"+file.readline())
    file.close()

output.close()

print("작업종료")
end_time=time.time()
print("소요시간 : " + str(end_time - start_time) + " 초")