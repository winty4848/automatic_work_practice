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
personal_IDs = sys.argv[1] #ch3에서 만든 그거 쓰면 됨!
template_filename = sys.argv[2]


template = Image.open(template_filename)
Xdim, Ydim = template.size


out_dir ="suryojungs"
'''
if out_dir not in os.listdir():
    os.mkdir(out_dir)
'''
os.makedirs(out_dir, exist_ok=True)

# csv 리딩
IDs = open(personal_IDs)
header = IDs.readline()

nameFont = ImageFont.truetype("font/gulim.ttc", 30)
dateFont = ImageFont.truetype("font/gulim.ttc", 25)
smallFont = ImageFont.truetype("font/gulim.ttc", 18)

date = str(datetime.datetime.today().date()) # str로 안바꾸면 라이브러리 자체 자료형이 나와서 써먹을수가 없더라
date = date.split("-")
DATE = date[0] + "년 " + date[1] + "월 " + date[2] + "일"

# 수여날짜를 배경에 입력합니다.
# 좌우 여백은 가운데정렬입니다.
x_offset = int(Xdim / 2 - dateFont.getsize(DATE)[0]/2)
# 상하 여백은 대충 30% 가량 잡아봅니다.
y_offset = int(Ydim * .7)
# 배경에 수여날짜를 기재합니다.
ImageDraw.Draw(template).text(xy=(x_offset, y_offset), text=DATE, font=dateFont, fill="black")

# 지금까지 제작한 증서 개수를 저장하는 카운터를 만듭니다.
# 수료증서 시작번호를 적어주시면 됩니다. 예를들어 연번이 50번부터 시작하면 COUNT=50입니다.
COUNT = 0

for line in IDs:
    splt = line.strip().split(",")

    name = splt[0]
    phone = "전화번호 : " + splt[3]

    # 수료증(상장) 템플릿을 복제합니다.
    suryojung = template.copy()

    # 이름을 삽입할겁니다.
    # 이름 사이사이 공백을 삽입해서 더 잘 보이게 합니다.
    temp_name = ""
    for el in name:
        temp_name += el + " "
    # 이름을 수료증(상장)에 기재하기 좋게 양식으로 다듬어줍니다.
    name = "성      명 : " + temp_name[:-1]


    x_offset = int(Xdim * 0.15) # 이름과 대충 좌측으로부터 15% 떨어진 곳에 기재합시다.
    y_offset = int(Ydim * 0.35) # 이름은 대충 상단으로부터 35% 위치에 기재합시다.
    ImageDraw.Draw(suryojung).text(xy=(x_offset, y_offset), text=name, font=nameFont, fill="black")

    # 이름보다 좀 더 아래 삽입
    y_offset += nameFont.getsize(name)[1]*1.5
    ImageDraw.Draw(suryojung).text(xy=(x_offset, y_offset), text=phone, font=nameFont, fill="black")

    # 수여번호도 입력해야겠죠?
    suyeo = "수여번호 : %d-%06d" % (int(DATE[:4]),  COUNT)
    y_offset = int(Ydim * 0.12) # 수여번호는 상 12%지점쯤에 입력합시다.
    ImageDraw.Draw(suryojung).text(xy=(x_offset, y_offset), text=suyeo, font=smallFont, fill="black")

    suryojung.save(out_dir + "/" + str(COUNT) + ".png")
    suryojung.close()
    COUNT += 1


template.close()

print("Process Done.")
end_time = time.time()
print("The Job Took " + str(end_time - start_time) + " seconds.")
