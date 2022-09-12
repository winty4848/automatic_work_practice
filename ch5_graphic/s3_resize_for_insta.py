#-*-coding:euc-kr
"""
목표
정사각형으로 리사이즈
+ 남은 여백칸은 사용자가 지정한 색으로 색칠하기
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

    # 정사각형으로 만들기
    # offset은 기존 이미지를 삽입할 좌표라고 생각하면 됨.
    # 더 긴 변을 기준으로 1/2을 기준점 삼아 더 짧은 변의 1/2 지점에서 짧은 변을 시작하면 됨. 더 긴변은 꽉차니까 0이고
    # 그걸 수식으로 옮긴거
    if Xdim > Ydim:
        new_size = Xdim
        x_offset = 0
        y_offset = int((Xdim - Ydim) / 2)
    else:
        new_size = Ydim
        x_offset = int((Ydim - Xdim) / 2)
        y_offset = 0

    # 새로운 이미지를 생성. 텅 빈 정사각형이고 색깔은 background_color
    new_image = Image.new("RGBA", (new_size, new_size), background_color)

    # 현재 텅 빈 배경(그러나 색깔은 지정된) 원본 이미지 + 아까 계산한 좌표축에 덮어씀
    new_image.paste(image, (x_offset, y_offset))
    new_image.save(out_dir + "/" + filename)

    image.close()
    new_image.close()

print("Process Done.")
end_time = time.time()
print("The Job Took " + str(end_time - start_time) + " seconds.")
