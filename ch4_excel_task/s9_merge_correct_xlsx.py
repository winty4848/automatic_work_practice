#-*-coding:euc-kr
# s5�� s8�� �ణ «���� ����

import os
import pyexcel as px
import sys

# python s9_merge_correct_xlsx.py <TEMPLATE\> <DIRECTORY\>
template = sys.argv[1]
directory = sys.argv[2]
input_files = os.listdir(directory)

standard_header = px.get_array(file_name=template)[0]

# ������ ������ ����Ʈ ����� ����� �̸� �־���.
total_content=[standard_header]

for filename in input_files:
    if ".xlsx" not in filename:
        continue

    file = px.get_array(file_name=directory + "/" + filename)

    header = file[0]
    # �˻����� ����� �������� ����� �ٸ��� ��Ȳ��
    if standard_header != header:
        continue

    # �ǽ� �����Ϳ����� ���������� ���+������ �� 2�������� ���� ���� Ȱ���� ���Ͽ� ���� �����̽� Ȱ��
    total_content += file[1:]

px.save_as(array=total_content, dest_file_name="merged_FILE.xlsx")
print("Total " + str(len(total_content) - 1) + " files were merged.")