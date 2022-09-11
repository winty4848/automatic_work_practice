#-*-coding:euc-kr

import time
import os
from PIL import Image
import sys

print("Process Start.")
start_time = time.time()

# python s2_resize_image.py random_image 0~100 사이 수
directory = sys.argv[1]
# 몇 퍼센트 비율로 사이즈를 변경할지
percent = float(sys.argv[2])/100

out_dir ="resized_image"
'''
if out_dir not in os.listdir():
    os.mkdir(out_dir)
'''
os.makedirs(out_dir, exist_ok=True)

input_files = os.listdir(directory)
for filename in input_files:
    # 이미지 아닌 파일 걸러내기
    exp = filename.strip().split('.')[-1]
    if exp not in "JPG jpg JPEG jpeg PNG png BMP bmp":
        continue
    image = Image.open(directory + "/" + filename)
    Xdim, Ydim = image.size

    Xdim *= percent
    Ydim *= percent
    image = image.resize((int(Xdim), int(Ydim)))

    image.save(out_dir + "/" + filename)
    image.close()

print("Process Done.")
end_time = time.time()
print("The Job Took " + str(end_time - start_time) + " seconds.")
