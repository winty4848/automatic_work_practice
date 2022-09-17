#-*-coding:euc-kr

import time
import os
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import sys
import datetime

print("Process Start.")
start_time = time.time()

# python s8_make_certification.py merged_ID.csv su_ryo_jung.png
personal_IDs = sys.argv[1] #ch3���� ���� �װ� ���� ��!
template_filename = sys.argv[2]


template = Image.open(template_filename)
Xdim, Ydim = template.size


out_dir ="suryojungs"
'''
if out_dir not in os.listdir():
    os.mkdir(out_dir)
'''
os.makedirs(out_dir, exist_ok=True)

# csv ����
IDs = open(personal_IDs)
header = IDs.readline()

nameFont = ImageFont.truetype("font/gulim.ttc", 30)
dateFont = ImageFont.truetype("font/gulim.ttc", 25)
smallFont = ImageFont.truetype("font/gulim.ttc", 18)

date = str(datetime.datetime.today().date()) # str�� �ȹٲٸ� ���̺귯�� ��ü �ڷ����� ���ͼ� ��������� ������
date = date.split("-")
DATE = date[0] + "�� " + date[1] + "�� " + date[2] + "��"

# ������¥�� ��濡 �Է��մϴ�.
# �¿� ������ ��������Դϴ�.
x_offset = int(Xdim / 2 - dateFont.getsize(DATE)[0]/2)
# ���� ������ ���� 30% ���� ��ƺ��ϴ�.
y_offset = int(Ydim * .7)
# ��濡 ������¥�� �����մϴ�.
ImageDraw.Draw(template).text(xy=(x_offset, y_offset), text=DATE, font=dateFont, fill="black")

# ���ݱ��� ������ ���� ������ �����ϴ� ī���͸� ����ϴ�.
# �������� ���۹�ȣ�� �����ֽø� �˴ϴ�. ������� ������ 50������ �����ϸ� COUNT=50�Դϴ�.
COUNT = 0

for line in IDs:
    splt = line.strip().split(",")

    name = splt[0]
    phone = "��ȭ��ȣ : " + splt[3]

    # ������(����) ���ø��� �����մϴ�.
    suryojung = template.copy()

    # �̸��� �����Ұ̴ϴ�.
    # �̸� ���̻��� ������ �����ؼ� �� �� ���̰� �մϴ�.
    temp_name = ""
    for el in name:
        temp_name += el + " "
    # �̸��� ������(����)�� �����ϱ� ���� ������� �ٵ���ݴϴ�.
    name = "��      �� : " + temp_name[:-1]


    x_offset = int(Xdim * 0.15) # �̸��� ���� �������κ��� 15% ������ ���� �����սô�.
    y_offset = int(Ydim * 0.35) # �̸��� ���� ������κ��� 35% ��ġ�� �����սô�.
    ImageDraw.Draw(suryojung).text(xy=(x_offset, y_offset), text=name, font=nameFont, fill="black")

    # �̸����� �� �� �Ʒ� ����
    y_offset += nameFont.getsize(name)[1]*1.5
    ImageDraw.Draw(suryojung).text(xy=(x_offset, y_offset), text=phone, font=nameFont, fill="black")

    # ������ȣ�� �Է��ؾ߰���?
    suyeo = "������ȣ : %d-%06d" % (int(DATE[:4]),  COUNT)
    y_offset = int(Ydim * 0.12) # ������ȣ�� �� 12%�����뿡 �Է��սô�.
    ImageDraw.Draw(suryojung).text(xy=(x_offset, y_offset), text=suyeo, font=smallFont, fill="black")

    suryojung.save(out_dir + "/" + str(COUNT) + ".png")
    suryojung.close()
    COUNT += 1


template.close()

print("Process Done.")
end_time = time.time()
print("The Job Took " + str(end_time - start_time) + " seconds.")
