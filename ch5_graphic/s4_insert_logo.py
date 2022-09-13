#-*-coding:euc-kr
"""
100~400 ������ ����� ������ ������ ������� �ΰ� �ֱ⿡ �ʹ� ���� �׸� ������ ������ ���� �� ���� ���� �� ����
+ pillow�� ���� ������ �����⿡ png ���� �ʿ�
-> ��ħ ���ڰ� '������' �׸������� �غ��س��⿡ �״�� Ȱ���ϱ�� �ߴ�.
"""
import time
import os
from PIL import Image
import sys

print("Process Start.")
start_time = time.time()

directory = sys.argv[1]
logo_filename = sys.argv[2]

out_dir ="images_with_logo"
'''
if out_dir not in os.listdir():
    os.mkdir(out_dir)
'''
os.makedirs(out_dir, exist_ok=True)
input_files = os.listdir(directory)

logo = Image.open(logo_filename)
logo_x, logo_y = logo.size

for filename in input_files:
    exp = filename.strip().split('.')[-1]
    if exp not in "JPG jpg JPEG jpeg PNG png BMP bmp":
        continue

    image = Image.open(directory + "/" + filename)
    Xdim, Ydim = image.size

    # �ΰ������� �̹����� �°� ������ Ȯ��/���
    if logo_x / Xdim > logo_y / Ydim:
        # ���ڴ� �ܼ��� 1/5��� �����ߴٸ�
        # ��Ȳ�� ���󼭴� Xdim�� Ydim�� ����ؼ� �����ϴ� ����� ����� �� �ְڴ�
        new_logo_x = int(Xdim/5)
        # new_logo_y : logo_y = new_logo_x : logo_x
        new_logo_y = int(logo_y * (new_logo_x / logo_x))
    else:
        new_logo_y = int(Ydim / 5)
        new_logo_x = int(logo_x * (new_logo_y / logo_y))

    resized_logo = logo.resize((new_logo_x, new_logo_y))

    # �Է¹��� ������ �ΰ� �����մϴ�. ������ ��ġ�� ������.
    # ���� ������ 2%���� �ָ� �����ϰ���? �̰� �������� ���⿡ �޷� �ֽ��ϴ�.
    image.paste(resized_logo, (int(Xdim/50), int(Ydim/50)), resized_logo)

    image.save(out_dir + "/" + filename)
    image.close()

print("Process Done.")
end_time = time.time()
print("The Job Took " + str(end_time - start_time) + " seconds.")
