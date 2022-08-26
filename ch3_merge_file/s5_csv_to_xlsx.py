#-*-coding:euc-kr

import pyexcel.cookbook as pc
import sys
from euc_to_utf import change_form


# pip install pyexcel pyexcel-xlsx
# pyexcel�� utf8���ڵ� ���. ������� �ַ� euc-kr ���.

print("�۾� ����")

# sys.argv�� ���ڸ� �Է¹޾���. �Ʒ��� ���� ��ɾ�� ����
# python s3_csv_to_xlsx.py merge_ID.csv test.xlsx
input_file=sys.argv[1]
result_file=sys.argv[2]

print(input_file)
print(type(input_file))

# pyexcel�� �⺻������ �������ִ� �Լ�
# ���ڵ� ���� ���� �� ���⼭���� ����ó�� �ʿ�

try:
    pc.merge_all_to_a_book([input_file], result_file)
except UnicodeDecodeError:
    change_form(input_file)
    input_file="utf8_" + input_file
    pc.merge_all_to_a_book([input_file], result_file)

print("�۾� ����")