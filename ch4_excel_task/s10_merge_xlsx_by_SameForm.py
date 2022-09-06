#-*-coding:euc-kr

import os
import pyexcel as px
import sys

# python s10_merge_xlsx_by_SameForm.py personal_fake_info
directory = sys.argv[1]
result_folder="merged_"+directory
os.makedirs(result_folder, exist_ok=True)
# ���� �ڵ忡�� �Ʒ��� ���� �Ǿ������� �� ������ �� ���� �� ����
'''
if out_dir not in os.listdir():
    os.mkdir(out_dir)
'''

input_files = os.listdir(directory)

merge_header=[]
merge_content=[]

'''
��ü ��� ����Ʈ�� ����� �߰ߵ� ������ ����. ���������� ��ü ������ ����Ʈ�� ����.
if ������ �ִ� ����� ������ �ִٸ�
    1. �ش� ����� �ε��� ����
    2. ������[�� �ε���] �� ������ �־��� -> �� ���Ϸ� �̾����� �ϱ� ������ + ������
else
    1. ��ü ��� ����Ʈ�� ����
    2. ��ü ������ ����Ʈ�� ���� -> ���� ���Ϸ� �и��Ǿ�� �ϱ� ������ append() �� print�غ��� 3�� ����Ʈ�� ���� ����.
'''

for filename in input_files:
    if ".xlsx" not in filename:
        continue

    file = px.get_array(file_name=directory + "/" + filename)


    header = file[0]
    content = file[1:]

    # �ҷ��� ������ ����� �̹� �о�Դ� ���ϰ� ��ġ�ϴ��� �м��մϴ�.
    # �Ʒ� �ڵ�� ���ο� ����� �߰ߵ� ������ �۵��մϴ�.
    if header not in merge_header:
        # ó�� �߰ߵ� ������ ����� �Ӵϴ�.
        merge_header.append(header)
        # ����� ���� ���ø� ����Ʈ�� �����Ͽ� ������ �Ӵϴ�.
        merge_content.append([header])

    # ������ ���� ����Ʈ�� �ҷ��ɴϴ�.
    index = merge_header.index(header)

    # ����Ʈ�� ������ ���� �Է��մϴ�.
    merge_content[index] += content

# ������ �����͵��� ���� ���� ���Ϸ� �����մϴ�.
for i in range(len(merge_content)):
    px.save_as(array=merge_content[i], dest_file_name=result_folder + "/" + str(i) + "_merged_File.xlsx")
