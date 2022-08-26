#-*-coding:euc-kr

import pyexcel.cookbook as pc
import sys
from euc_to_utf import change_form


# pip install pyexcel pyexcel-xlsx
# pyexcel은 utf8인코딩 사용. 윈도우는 주로 euc-kr 사용.

print("작업 ㄱㄱ")

# sys.argv는 인자를 입력받아줌. 아래와 같이 명령어로 실행
# python s3_csv_to_xlsx.py merge_ID.csv test.xlsx
input_file=sys.argv[1]
result_file=sys.argv[2]

print(input_file)
print(type(input_file))

# pyexcel이 기본적으로 제공해주는 함수
# 인코딩 문제 있을 시 여기서부터 오류처리 필요

try:
    pc.merge_all_to_a_book([input_file], result_file)
except UnicodeDecodeError:
    change_form(input_file)
    input_file="utf8_" + input_file
    pc.merge_all_to_a_book([input_file], result_file)

print("작업 끝남")