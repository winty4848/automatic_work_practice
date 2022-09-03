#-*-coding:euc-kr

# ���� �������ϰ� �ٸ��� �μ��� mode�� �����ϴ°� �ֱ淡 ���ϰ� ŷ����..
# mode �μ��� �����˰� �϶�°��� �Ѥ�... �޹����ؼ� ����ó���� ��������
# python s8_find_and_fix.py <TEMPLATE\> <DIRECTORY\> <MODE\>
# EX) python s8_find_and_fix.py merged_ID.xlsx personal_fake_info separate

import os
import pyexcel as px
import sys

def main(template, directory, mode):
    input_files = os.listdir(directory)
    # ���� ���ø� ���ϸ� �����Ͽ� ����� ������.
    standard_header=px.get_array(file_name=template)[0]

    if mode.lower()=="delete":
        count=0
    elif mode.lower()=="report":
        report_file=open('report.txt','w')
    elif mode.lower()=="separate":
        # ������ ����ߴ� os.mkdir�� �޸� ���� ���丮 ��������
        # + �ɼ� �������� ������ �̹� ������ ��� �Ѿ�� ������ ����.
        os.makedirs("wrong_files", exist_ok=True)
        import shutil # �� ��� ���� �̵��� �����ϱ� ���� ���̺귯�� ȣ��
    else:
        sys.argv[0.1] # ���Ƿ� ���� �߻����� ���� ���.

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



