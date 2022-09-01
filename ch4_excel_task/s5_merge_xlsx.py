#-*-coding:euc-kr

import os
import pyexcel as px
import sys

# python s5_merge_xlsx.py personal_fake_info
directory = sys.argv[1]

output_name = "merged_ID.xlsx"
input_files = os.listdir(directory)

# �̹����� ��� xlsx ������ ������ �� ��(list)�� ������ ���� �� ����Ʈ�� �ٽ� xlsx�� ��ȯ���ִ� �۾�
total_content=[]

for filename in input_files:
    if ".xlsx" not in filename:
        continue

    # ���������� list ���·� ��ȯ�ϴ� �Լ�
    # �ึ�� ��� �迭 ����. �� print(data_array)�ϸ� ���߹迭�÷� ��Ÿ��.
    data_array = px.get_array(file_name=directory + "/" + filename)

    # �� ���ϸ��� ����� ������ ����� ������ �и�
    # ����� ���� �����̽� -> ��� �� ����Ʈ�� ��� ��� �״�� ���
    # ������ ��̴� ���� �����̽� -> ��� �� ����Ʈ�� ��� ���
    header = data_array[0]
    data_array = data_array[1:]

    # ��� �Է�
    # ���� ����� ����Ʈ �����̹Ƿ� append �Լ� �̿�
    if len(total_content) == 0:
        total_content.append(header)

    # ���� data_array�� ���߹迭 ��
    # append�� �ϸ� total_content����Ʈ �ȿ� ���߹迭�� ���� ��
    # ���� ����Ʈ�� ��Ҹ� �����ֱ� ���� + ���
    total_content += data_array

px.save_as(array=total_content, dest_file_name=output_name)
