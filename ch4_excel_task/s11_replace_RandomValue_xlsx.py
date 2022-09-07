#-*-coding:euc-kr
# �ǹ����� ���� �����ų ���� �������� ���ڴ� ���� ���������� Ȱ���غ���� ��
# ���� ��ƿ��Ƽ�� �ȱ���ִٸ� �����غ����� �ַ���� �� ����

import time
import os
import pyexcel as px
import sys
import random


directory = sys.argv[1]
percent = float(sys.argv[2])/100
input_files = os.listdir(directory)

terror_value = ["�����", "�߿�", "�߿���", "�̾߿�", "����Ի���ؿ�"]

for filename in input_files:
    if ".xlsx" not in filename:
        continue
    data = px.get_array(file_name=directory + "/" + filename)

    os.remove(directory + "/" + filename)

    for i in range(len(data)):
        for j in range(len(data[i])):
            # Ȯ���� ��÷�� �Ǿ��ٸ� �����͸� �ı�
            if random.random() < percent:
                if int(str(time.time())[-1])>5:
                    data[i][j] = random.choice(terror_value)
                else:
                    data[i][j] = random.uniform(1,1000)

    px.save_as(array=data, dest_file_name=directory + "/" + filename)