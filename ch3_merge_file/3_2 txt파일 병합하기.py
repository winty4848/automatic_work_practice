#-*-coding:euc-kr

import time
import os

print("�����")

start_time=time.time()

# ��ĥ ���ϵ��� ����� ������
directory="personal_fake_info"

# ����ȭ�� ���� �̸� ����
output_name="merge_ID.txt"

# ����� ���� ����
output=open(output_name, 'w')

# ���� ���빰 ����Ʈ ����. ������ Ÿ�� ����غ��� ���ϸ��� list���� �־�������.
# �ٸ� ������ 1, 101, 102, ... �̷������� �ڹٲ������. 1,2,3, ... ������ ���Ѿ��Ѵٸ� ���� �����ܺ��� �ٲٴ��� �ؾ��ҵ�
input_files=os.listdir(directory)

for filename in input_files:
    # �ؽ�Ʈ���� �ƴѰ� ��ŵ
    if ".txt" not in filename:
        continue
    file=open(directory + "/" + filename)
    content=file.read()
    output.write(content + "\n\n")
    file.close()

output.close()

print("�۾�����")
end_time=time.time()
print("�ҿ�ð� : " + str(end_time - start_time) + " ��")