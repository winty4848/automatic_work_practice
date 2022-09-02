# 저자는 무작위로 엑셀파일 셀렉팅하여 내용 바꾸기 이런식으로 서술
# 이 코드 자체로는 실무에서 쓸 일은 없을 것 같지만 조건에 따른 수정 등으로 활용 가능할 듯

#-*-coding:euc-kr
import time
import os
import pyexcel as px
import sys
import random

# python s6_change_value_in_xlsx.py personal_fake_info (0~100사이 유리수)
directory = sys.argv[1]
percent = float(sys.argv[2]) / 100

input_files = os.listdir(directory)
# 무작위로 변경파일 설정 시. 일정 조건을 걸 경우 이하 절을 바꾸자
change_count = int(len(input_files)*percent)
random.shuffle(input_files)
change_list=input_files[:change_count]

# 3가지 방식으로 파일을 바꿈.
shift_1 = change_count/3*2
shift_2 = change_count/3

for filename in change_list:
    if ".xlsx" not in filename:
        continue
    # 그동안 사용한 s5의 get_array()는 파이썬 list 자료형으로 불러옴
    # get_sheet는 pyexcel 자체 자료형이어서 xlsx를 편집하기 위한 다양한 함수 활용 가능
    file=px.get_sheet(file_name=directory + "/" + filename)
    # 원본 삭제. 보존하려면 생성파일/원본파일 중 하나 이름바꿔야 함
    os.remove(directory+"/"+filename)

    num_columns=len(file[0])
    target_columns=random.randint(0, num_columns-1)

    if change_count > shift_1:
        file.delete_columns([target_columns])

    elif change_count > shift_2:
        file.column += file.column[target_columns].copy()

    else:
        # 같은 값으로 대치하기에 짧은 for문 사용
        # 영 눈에 안들어오면 그냥 편한대로 for 바꿔 쓰자
        cat=["고양이" for i in range(file.number_of_rows())]
        file.column[target_columns]=cat

    px.save_as(array=file, dest_file_name=directory + "/" + filename)
    change_count -= 1