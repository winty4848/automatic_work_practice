#-*-coding:euc-kr
import time
import os

print("�۾�����")
start_time=time.time()

# ��ĥ ���ϵ��� ����� ������
directory="personal_fake_info"

output_name="merge_ID.csv"

# ����� ���� ����
output=open(output_name, 'w')

input_files=os.listdir(directory)

# ���� ��� ���� ���� ���� (Į����)
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

            # ����� �����մϴ�. ���� 1ȸ�� ����˴ϴ�.
            if len(contents) > len(headers):
                headers.append(splits[0].strip())

    # ����� ���Ͽ� �Է��մϴ�. ���� 1ȸ�� ����˴ϴ�.
    if not output_header:
        header = ",".join(headers)
        output.write(header)
        output_header = True

    # ����� ���Ͽ� ���빰�� �Է��մϴ�.
    # ���� ����꿡�� ', ' ���� ���õǾ� ������ �̷����ϸ� ����� ���Ͽ� �ι�° ������ ���ھտ� ������ ��ĭ ����.
    new_line = ",".join(contents)
    print(new_line)
    output.write("\n" + new_line)

    # �о�� ������ �����մϴ�.
    file.close()

output.close()

print("�۾�����")

end_time=time.time()
print("�ҿ�ð� : " + str(end_time - start_time) + " ��")