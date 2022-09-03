#-*-coding:euc-kr
# ������ �ǹ����̺�
# ���� ��� �����ؼ� ��� ���Ŀ� ���� ī�����ϰ� ����

import time
import os
import pyexcel as px
import sys
import random

# python s7_count_header.py personal_fake_info count_header.txt
directory = sys.argv[1]
result_name = sys.argv[2]

input_files = os.listdir(directory)

# jsonó�� key : value ����
# ��� ����� key�� ���� ������ ī��Ʈ�ؼ� value�� �ְڴٴ� �ǹ���
total_header={}

for filename in input_files:
    if ".xlsx" not in filename:
        continue

    file=px.get_array(file_name=directory + "/" + filename)
    # ���� �����̽��̹Ƿ� ����Ʈ����. str ��ȯ�Ͽ� [~~~] �� ��ü�� ����ȭ��.
    temp_header=str(file[0])

    if temp_header in total_header:
        total_header[temp_header] += 1 # �̹� �ִ� ���̹Ƿ� value+=1
    else:
        total_header[temp_header] = 1 # ���ο� ���̹Ƿ� value �ʱ�ȭ

report=""

for key in total_header:
    report += "Header : "+key+"\n"
    report += "Count : "+str(total_header[key])+"\n\n"

print(report)

report_file=open(result_name, 'w')
report_file.write(report)
report_file.close()