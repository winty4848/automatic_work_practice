#-*-coding:euc-kr

import os
import pyexcel.cookbook as PC
import sys

# python s6_txt_via_csv_to_xlsx.py personal_fake_info
directory = sys.argv[1]

# 임시로 생성할 csv파일. 완료 전 삭제 예정
temp_file_name = "temp.csv"
output_name = "merged_ID.xlsx"

# 만들 때부터 인코딩 미리 지정
temp_file = open(temp_file_name, 'w', encoding="utf-8")

input_files = os.listdir(directory)

# 엑셀 헤더 관련 변수 정의 (칼럼명) 이하 s4와 거의 동일
headers=[]
output_header = False # 초기값 F 지정

for filename in input_files:
    if ".txt" not in filename:
        continue
    file = open(directory + "/" + filename)

    # 파일의 내용물을 저장할 리스트를 정의합니다.
    contents = []

    # 현재 행마다 데이터가 나뉘어져 있으니 한 줄씩 데이터 리딩
    for line in file:
        # 현재 텍스트파일은 따옴표를 기점으로 실데이터가 삽입되어 있다는 점 착안
        if ":" in line:
            # split 수행 시 ['age', '43'] 출력됨. 즉 리스트의 마지막 인덱스에 실데이터
            splits = line.split(":")
            # strip()은 문자열에서 양쪽의 공백 제거. 즉 다른데이터 유형에서는 작동 안함.
            contents.append(splits[-1].strip())

            # 헤더 정리. 최초 1회만 실행
            if len(contents) > len(headers):
                headers.append(splits[0].strip())

    # 헤더 파일에 입력. 최초 1회만 실행
    if not output_header:
        header = ",".join(headers)
        temp_file.write(header)
        output_header = True

    # 임시 csv 파일에 내용 기록
    new_line = ",".join(contents)
    temp_file.write("\n" + new_line)

    file.close()

temp_file.close()

# 임시 csv 파일을 엑셀로 변환
PC.merge_all_to_a_book([temp_file_name], output_name)

# 임시로 저장된 결과물을 삭제합니다.
os.remove(temp_file_name)