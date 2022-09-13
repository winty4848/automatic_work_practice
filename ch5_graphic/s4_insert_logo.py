#-*-coding:euc-kr
"""
100~400 사이의 사이즈를 가지는 사진을 대상으로 로고를 넣기에 너무 작은 그림 파일은 사이즈 변경 시 문제 생길 것 같음
+ pillow의 투명도 개념이 나오기에 png 파일 필요
-> 마침 저자가 '적절한' 그림파일을 준비해놨기에 그대로 활용하기로 했다.
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

    # 로고파일을 이미지에 맞게 적당히 확대/축소
    if logo_x / Xdim > logo_y / Ydim:
        # 저자는 단순히 1/5배로 조절했다만
        # 상황에 따라서는 Xdim과 Ydim에 비례해서 조절하는 방법도 고려할 수 있겠다
        new_logo_x = int(Xdim/5)
        # new_logo_y : logo_y = new_logo_x : logo_x
        new_logo_y = int(logo_y * (new_logo_x / logo_x))
    else:
        new_logo_y = int(Ydim / 5)
        new_logo_x = int(logo_x * (new_logo_y / logo_y))

    resized_logo = logo.resize((new_logo_x, new_logo_y))

    # 입력받은 사진에 로고를 삽입합니다. 적당한 위치에 말이죠.
    # 대충 여백을 2%정도 주면 적당하겠죠? 이건 여러분의 취향에 달려 있습니다.
    image.paste(resized_logo, (int(Xdim/50), int(Ydim/50)), resized_logo)

    image.save(out_dir + "/" + filename)
    image.close()

print("Process Done.")
end_time = time.time()
print("The Job Took " + str(end_time - start_time) + " seconds.")
