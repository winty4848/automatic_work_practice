#-*-coding:euc-kr

# 기존 예제들하고 다르게 인수로 mode를 설정하는게 있길래 묘하게 킹받음..
# mode 인수가 뭔지알고 하라는거지 ㅡㅡ... 급발진해서 예외처리로 구현해줌
# python s8_find_and_fix.py <TEMPLATE\> <DIRECTORY\> <MODE\>
# EX) python s8_find_and_fix.py merged_ID.xlsx personal_fake_info separate

import os
import pyexcel as px
import sys

def main(template, directory, mode):
    input_files = os.listdir(directory)
    # 기준 템플릿 파일를 리딩하여 헤더만 저장함.
    standard_header=px.get_array(file_name=template)[0]

    if mode.lower()=="delete":
        count=0
    elif mode.lower()=="report":
        report_file=open('report.txt','w')
    elif mode.lower()=="separate":
        # 이전에 사용했던 os.mkdir과 달리 여러 디렉토리 생성가능
        # + 옵션 설정으로 폴더가 이미 존재할 경우 넘어가고 없으면 만듬.
        os.makedirs("wrong_files", exist_ok=True)
        import shutil # 이 경우 파일 이동을 수행하기 위한 라이브러리 호출
    else:
        sys.argv[0.1] # 고의로 오류 발생시켜 도움말 띄움.

    for filename in input_files:
        if ".xlsx" not in filename:
            continue
        file=px.get_array(file_name=directory + "/" + filename)
        temp_header=file[0]

        if standard_header==temp_header:
            continue

        if mode.lower() == "delete":
            os.remove(directory + "/" + filename)
            count += 1
        elif mode.lower() == "report":
            report_file.write(filename+'\n')
        elif mode.lower() == "separate":
            shutil.move(directory + "/" + filename, "wrong_files/" + filename)

    if mode.lower() == "delete":
        print("Total " + str(count) + " files were removed.")
    if mode.lower() == "report":
        report_file


try:
    first_input = sys.argv[1]
    second_input = sys.argv[2]
    third_input = sys.argv[3]
    main(first_input, second_input, third_input)
except IndexError:
    print("\n\n\n\ninput : python <file_name.py> <template> <directoy> <mode> \n\n")
    print("template : standard form file(excel file to be referenced) \n\n")
    print("directory : target folder\n\n")
    print("mode : you can use three options\n")
    print("1. delete : delete files DO NOT match the standard form\n")
    print("2. report : report files DO NOT match the standard form by txt\n")
    print("3. separate : move files DO NOT match the standard form to another folder\n")



