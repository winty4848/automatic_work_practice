#-*-coding:euc-kr
# s5와 s8을 약간 짬뽕한 느낌

import os
import pyexcel as px
import sys

# python s9_merge_correct_xlsx.py <TEMPLATE\> <DIRECTORY\>
template = sys.argv[1]
directory = sys.argv[2]
input_files = os.listdir(directory)

standard_header = px.get_array(file_name=template)[0]

# 데이터 저장할 리스트 만들고 헤더도 미리 넣어줌.
total_content=[standard_header]

for filename in input_files:
    if ".xlsx" not in filename:
        continue

    file = px.get_array(file_name=directory + "/" + filename)

    header = file[0]
    # 검사파일 헤더와 기준파일 헤더가 다르면 돔황쳐
    if standard_header != header:
        continue

    # 실습 데이터에서는 엑셀파일이 헤더+데이터 총 2줄이지만 실제 업무 활용을 위하여 범위 슬라이싱 활용
    total_content += file[1:]

px.save_as(array=total_content, dest_file_name="merged_FILE.xlsx")
print("Total " + str(len(total_content) - 1) + " files were merged.")