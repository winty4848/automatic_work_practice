#-*-coding:euc-kr
"""
��ǥ
���簢������ ��������
+ ���� ����ĭ�� ����ڰ� ������ ������ ��ĥ�ϱ�
"""
import time
import os
from PIL import Image
import sys

print("Process Start.")
start_time = time.time()

directory = sys.argv[1]
background_color = sys.argv[2]

out_dir ="insta image"
'''
if out_dir not in os.listdir():
    os.mkdir(out_dir)
'''
os.makedirs(out_dir, exist_ok=True)
input_files = os.listdir(directory)

for filename in input_files:
    exp = filename.strip().split('.')[-1]
    if exp not in "JPG jpg JPEG jpeg PNG png BMP bmp":
        continue

    image = Image.open(directory + "/" + filename)
    Xdim, Ydim = image.size

    # ���簢������ �����
    # offset�� ���� �̹����� ������ ��ǥ��� �����ϸ� ��.
    # �� �� ���� �������� 1/2�� ������ ��� �� ª�� ���� 1/2 �������� ª�� ���� �����ϸ� ��. �� �亯�� �����ϱ� 0�̰�
    # �װ� �������� �ű��
    if Xdim > Ydim:
        new_size = Xdim
        x_offset = 0
        y_offset = int((Xdim - Ydim) / 2)
    else:
        new_size = Ydim
        x_offset = int((Ydim - Xdim) / 2)
        y_offset = 0

    # ���ο� �̹����� ����. �� �� ���簢���̰� ������ background_color
    new_image = Image.new("RGBA", (new_size, new_size), background_color)

    # ���� �� �� ���(�׷��� ������ ������) ���� �̹��� + �Ʊ� ����� ��ǥ�࿡ ���
    new_image.paste(image, (x_offset, y_offset))
    new_image.save(out_dir + "/" + filename)

    image.close()
    new_image.close()

print("Process Done.")
end_time = time.time()
print("The Job Took " + str(end_time - start_time) + " seconds.")
