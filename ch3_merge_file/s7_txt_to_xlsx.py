# s6와 달리 숫자값도 문자값으로 저장해서 엑셀 켜보면 좌측 상단에 삼각형 붙어짐. 이로 인해 용량이 줄어듬
# csv 거치는 과정이 없어서 그런가 소요 시간도 단축됨.
# pyexcel은 csv대신 배열구조를 엑셀에 넣어줄 수 있다고 함.

#-*-coding:euc-kr

import os
import pyexcel as px
import sys

# python s7_txt_to_xlsx.py personal_fake_info
directory = sys.argv[1]

output_name = "merged_ID.xlsx"
input_files = os.listdir(directory)

# 이하 s4와 거의 동일한데 파일 전체 배열을 사용한다는 점이 차이
result_content=[]
output_header = False # 초기값 F 지정

# 헤더값만 임시 저장. 자세한 설명은 반복문 참고
# 한번밖에 사용되니까 반복문에 넣어서 지역변수처럼 쓸라했다가 반복할 때마다 초기화하는 거 자체가 코스트일 것 같아 전역변수로 설정때림.
temp_header=[]

for filename in input_files:
    if ".txt" not in filename:
        continue
    file = open(directory + "/" + filename)

    # 파일 내용 임시저장할 리스트. 반복할 때 마다 초기화
    each_txt_file_content = []

    # 현재 행마다 데이터가 나뉘어져 있으니 한 줄씩 데이터 리딩
    for line in file:
        # 양식과 다른 라인은 제외. s4에서는 왜 이렇게 안했는지 모르겠음.
        if ":" not in line:
            continue
        # " : " 기준으로 헤더 컨텐츠 분할
        file_header, file_content = line.strip().split(" : ")

        # line 한개씩 처리중이기 때문에 첫번째 반복문으로 복귀 시 output_header TRUE로 바꿔줌.
        # 또 첫 행에는 헤더를 넣고 두번째 행에는 첫번째 파일의 내용물을 넣어줘야 하기에 헤더 정보를 저장할 리스트 생성 필요함
        if not output_header:
            temp_header.append(file_header)

        each_txt_file_content.append(file_content)

    if not output_header:
        result_content.append(temp_header)
        output_header = True
    result_content.append(each_txt_file_content)
    file.close()

px.save_as(array=result_content, dest_file_name=output_name)