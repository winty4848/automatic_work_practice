#-*-coding:euc-kr

import os
import pyexcel.cookbook as PC
import sys

# python s6_txt_via_csv_to_xlsx.py personal_fake_info
directory = sys.argv[1]

# �ӽ÷� ������ csv����. �Ϸ� �� ���� ����
temp_file_name = "temp.csv"
output_name = "merged_ID.xlsx"

# ���� ������ ���ڵ� �̸� ����
temp_file = open(temp_file_name, 'w', encoding="utf-8")

input_files = os.listdir(directory)

# ���� ��� ���� ���� ���� (Į����) ���� s4�� ���� ����
headers=[]
output_header = False # �ʱⰪ F ����

for filename in input_files:
    if ".txt" not in filename:
        continue
    file = open(directory + "/" + filename)

    # ������ ���빰�� ������ ����Ʈ�� �����մϴ�.
    contents = []

    # ���� �ึ�� �����Ͱ� �������� ������ �� �پ� ������ ����
    for line in file:
        # ���� �ؽ�Ʈ������ ����ǥ�� �������� �ǵ����Ͱ� ���ԵǾ� �ִٴ� �� ����
        if ":" in line:
            # split ���� �� ['age', '43'] ��µ�. �� ����Ʈ�� ������ �ε����� �ǵ�����
            splits = line.split(":")
            # strip()�� ���ڿ����� ������ ���� ����. �� �ٸ������� ���������� �۵� ����.
            contents.append(splits[-1].strip())

            # ��� ����. ���� 1ȸ�� ����
            if len(contents) > len(headers):
                headers.append(splits[0].strip())

    # ��� ���Ͽ� �Է�. ���� 1ȸ�� ����
    if not output_header:
        header = ",".join(headers)
        temp_file.write(header)
        output_header = True

    # �ӽ� csv ���Ͽ� ���� ���
    new_line = ",".join(contents)
    temp_file.write("\n" + new_line)

    file.close()

temp_file.close()

# �ӽ� csv ������ ������ ��ȯ
PC.merge_all_to_a_book([temp_file_name], output_name)

# �ӽ÷� ����� ������� �����մϴ�.
os.remove(temp_file_name)