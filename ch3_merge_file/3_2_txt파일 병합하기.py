#-*-coding:euc-kr

import time
import os

print("가즈아")

start_time=time.time()

# 합칠 파일들이 저장된 폴더명
directory="personal_fake_info"

# 단일화된 파일 이름 정의
output_name="merge_ID.txt"

# 결과물 파일 생성
output=open(output_name, 'w')

# 폴더 내용물 리스트 생성. 실제로 타입 출력해보니 파일명이 list형에 넣어져있음.
# 다만 정렬이 1, 101, 102, ... 이런식으로 뒤바뀌어있음. 1,2,3, ... 순서를 지켜야한다면 파일 생성단부터 바꾸던가 해야할듯
input_files=os.listdir(directory)

for filename in input_files:
    # 텍스트파일 아닌거 스킵
    if ".txt" not in filename:
        continue
    file=open(directory + "/" + filename)
    content=file.read()
    output.write(content + "\n\n")
    file.close()

output.close()

print("작업종료")
end_time=time.time()
print("소요시간 : " + str(end_time - start_time) + " 초")