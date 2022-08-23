#-*-coding:euc-kr
import time
import os

print("작업시작")

start_time=time.time()

# 합칠 파일들이 저장된 폴더명
directory="personal_fake_info"

# 단일화된 파일 이름 정의
# 3_2와 코드 한줄만 다른거였다... 확장자만 바꿔줌
output_name="merge_ID.csv"

# 결과물 파일 생성
output=open(output_name, 'w')

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