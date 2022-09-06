#-*-coding:euc-kr

import os
import pyexcel as px
import sys

# python s10_merge_xlsx_by_SameForm.py personal_fake_info
directory = sys.argv[1]
result_folder="merged_"+directory
os.makedirs(result_folder, exist_ok=True)
# 저자 코드에는 아래와 같이 되어있으나 난 위에가 더 좋은 것 같다
'''
if out_dir not in os.listdir():
    os.mkdir(out_dir)
'''

input_files = os.listdir(directory)

merge_header=[]
merge_content=[]

'''
전체 헤더 리스트를 만들고 발견될 때마다 저장. 마찬가지로 전체 컨텐츠 리스트를 만듬.
if 기존에 있던 헤더를 가지고 있다면
    1. 해당 헤더의 인덱스 추출
    2. 컨텐츠[그 인덱스] 에 컨텐츠 넣어줌 -> 한 파일로 이어져야 하기 때문에 + 연산자
else
    1. 전체 헤더 리스트에 삽입
    2. 전체 컨텐츠 리스트에 삽입 -> 개별 파일로 분리되어야 하기 때문에 append() 즉 print해보면 3중 리스트가 나올 것임.
'''

for filename in input_files:
    if ".xlsx" not in filename:
        continue

    file = px.get_array(file_name=directory + "/" + filename)


    header = file[0]
    content = file[1:]

    # 불러온 파일의 헤더가 이미 읽어왔던 파일과 일치하는지 분석합니다.
    # 아래 코드는 새로운 헤더가 발견될 때에만 작동합니다.
    if header not in merge_header:
        # 처음 발견된 헤더라면 기록해 둡니다.
        merge_header.append(header)
        # 출력할 파일 템플릿 리스트를 제작하여 저장해 둡니다.
        merge_content.append([header])

    # 저장할 파일 리스트를 불러옵니다.
    index = merge_header.index(header)

    # 리스트에 데이터 값을 입력합니다.
    merge_content[index] += content

# 합쳐진 데이터들을 각각 엑셀 파일로 저장합니다.
for i in range(len(merge_content)):
    px.save_as(array=merge_content[i], dest_file_name=result_folder + "/" + str(i) + "_merged_File.xlsx")
