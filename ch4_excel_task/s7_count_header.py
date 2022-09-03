#-*-coding:euc-kr
# 일종의 피벗테이블
# 파일 모두 리딩해서 헤더 형식에 따라 카운팅하고 있음

import time
import os
import pyexcel as px
import sys
import random

# python s7_count_header.py personal_fake_info count_header.txt
directory = sys.argv[1]
result_name = sys.argv[2]

input_files = os.listdir(directory)

# json처럼 key : value 구조
# 헤더 양식을 key로 보고 개수를 카운트해서 value에 넣겠다는 의미임
total_header={}

for filename in input_files:
    if ".xlsx" not in filename:
        continue

    file=px.get_array(file_name=directory + "/" + filename)
    # 단일 슬라이스이므로 리스트형태. str 변환하여 [~~~] 꼴 자체를 문자화함.
    temp_header=str(file[0])

    if temp_header in total_header:
        total_header[temp_header] += 1 # 이미 있는 값이므로 value+=1
    else:
        total_header[temp_header] = 1 # 새로운 값이므로 value 초기화

report=""

for key in total_header:
    report += "Header : "+key+"\n"
    report += "Count : "+str(total_header[key])+"\n\n"

print(report)

report_file=open(result_name, 'w')
report_file.write(report)
report_file.close()