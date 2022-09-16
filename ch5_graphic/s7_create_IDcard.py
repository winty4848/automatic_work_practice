#-*-coding:euc-kr

import time
import os
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import sys


print("Process Start.")
start_time = time.time()

# python s7_create_IDcard.py augmentation merged_ID.csv sample_logo.PNG template.jpg
member_photo = sys.argv[1] # s6에서 작업한 사진 사용하면 됨
personal_IDs = sys.argv[2] # ch3에서 작업한거 사용하면 됨
logo_filename = sys.argv[3] # s4 로고 사용
template_filename = sys.argv[4] # 저자가 준비해둔 걸 쓰자

try:
    template = Image.open(template_filename)
except:
    template = Image.new("RGBA", (800, 1268), 'white')

Xdim, Ydim = template.size


url = "https://bit.ly/2FqKtba"


out_dir ="idcards"
'''
if out_dir not in os.listdir():
    os.mkdir(out_dir)
'''
os.makedirs(out_dir, exist_ok=True)



logo = Image.open(logo_filename)
logo_x, logo_y = logo.size


photos = os.listdir(member_photo)
PHOTOS = []
for el in photos:
    if el.strip().split(".")[-1] not in "PNG png JPG jpg BMP bmp JPEG jpeg":
        continue
    PHOTOS.append(el)
'''
위에서 사용한 파일명에서 숫자 따오는 방식 말고 s6처럼 %05d를 이용해도 되긴 한다
오히려 이 코드에서는 변수명이 햇갈려서 %05d를 사용하는게 좋아보임.
다만 일반적인 경우에는 사진에 사원코드 같은 key값를 사용하여 이름을 짓기 때문에 리스트 이용한 방법도 알아둬야 할 것 같다.
'''

# 지금까지 제작한 명함 개수
COUNT = 0

# 로고 크기를 삽입하기 좋게 편집합니다. 사원증은 가로가 짧으니 가로 길이를 기준으로 작업합니다.
# 로고의 너비를 사원증 너비의 20%로 조절합니다.
new_logo_x = int(Xdim * 0.2)
# new_logo_y : logo_y = new_logo_x : logo_x
new_logo_y = int(logo_y * (new_logo_x / logo_x))
resized_logo = logo.resize((new_logo_x, new_logo_y))
logo.close()


# csv 파일 리딩
IDs = open(personal_IDs)
header = IDs.readline()

# 빈 사원증 좌하단에 로고를 삽입하겠습니다.
# 대충 여백을 10%, 5%정도 주면 적당하겠죠? 이건 여러분의 취향에 달려 있습니다.
template.paste(resized_logo, (int(Xdim * 0.1), int(Ydim * 0.95 - new_logo_y)))
resized_logo.close()

MainFont = ImageFont.truetype("font/gulim.ttc", 0)
nameFont = ImageFont.truetype("font/gulim.ttc", 100)
smallFont = ImageFont.truetype("font/gulim.ttc", 40)

# 사원증 우측 최상단에 URL을 삽입합니다.
# 좌우 여백은 맨 우측 5%를 띄울겁니다.
x_offset = int(Xdim * 0.95 - smallFont.getsize(url)[0])
# 상단 여백은 2%정도면 충분할 것 같습니다.
y_offset = int(Ydim * 0.02)
# 사원증에 홈페이지 주소를 삽입합니다.
ImageDraw.Draw(template).text(xy=(x_offset, y_offset), text=url, font=smallFont, fill="black")


for line in IDs:
    splt = line.strip().split(",")
    name = splt[0] # 사원증에 들어갈 정보들만 추출

    idcard = template.copy() # 템플릿 복제
    photo_for_id = Image.open(member_photo + "/" + PHOTOS[COUNT]) # 사진 리딩
    # 사진의 너비를 사원증 너비의 50% 크기로 조정합니다.
    photo_for_id = photo_for_id.resize((int(Xdim/2), int(Xdim/2 * (4/3))))
    # 사진을 사원증 정 중앙에 삽입합시다.
    idcard.paste(photo_for_id, (int(Xdim/4), int(Ydim/2 - Xdim/2*(4/3)/2)))

    temp_name = ""
    for el in name:
        temp_name += el + " "
    name = temp_name[:-1] #s5 주석

    # 이름은 좌우 가운데정렬할겁니다.
    x_offset = int(Xdim * 0.5 - nameFont.getsize(name)[0]/2)
    # 상하 여백은 20%쯤 줍시다.
    y_offset = int(Ydim * 0.8 - nameFont.getsize(name)[1])
    # 명함에 이름을 삽입합니다.
    ImageDraw.Draw(idcard).text(xy=(x_offset, y_offset), text=name, font=nameFont, fill="black")

    idcard.save(out_dir + "/" + PHOTOS[COUNT])
    idcard.close()
    COUNT += 1

template.close()


print("Process Done.")
end_time = time.time()
print("The Job Took " + str(end_time - start_time) + " seconds.")
