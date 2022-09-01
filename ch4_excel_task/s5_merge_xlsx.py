#-*-coding:euc-kr

import os
import pyexcel as px
import sys

# python s5_merge_xlsx.py personal_fake_info
directory = sys.argv[1]

output_name = "merged_ID.xlsx"
input_files = os.listdir(directory)

# 이번에는 모든 xlsx 파일의 내용을 한 곳(list)에 저장한 다음 그 리스트를 다시 xlsx로 변환해주는 작업
total_content=[]

for filename in input_files:
    if ".xlsx" not in filename:
        continue

    # 엑셀파일을 list 형태로 변환하는 함수
    # 행마다 묶어서 배열 구성. 즉 print(data_array)하면 이중배열꼴로 나타남.
    data_array = px.get_array(file_name=directory + "/" + filename)

    # 각 파일마다 헤더가 있으니 헤더와 컨텐츠 분리
    # 헤더는 단일 슬라이싱 -> 출력 시 리스트에 담긴 요소 그대로 출력
    # 데이터 어레이는 범위 슬라이싱 -> 출력 시 리스트에 담겨 출력
    header = data_array[0]
    data_array = data_array[1:]

    # 헤더 입력
    # 현재 헤더는 리스트 형태이므로 append 함수 이용
    if len(total_content) == 0:
        total_content.append(header)

    # 현재 data_array는 이중배열 꼴
    # append를 하면 total_content리스트 안에 이중배열이 들어가는 꼴
    # 따라서 리스트의 요소만 더해주기 위해 + 사용
    total_content += data_array

px.save_as(array=total_content, dest_file_name=output_name)
