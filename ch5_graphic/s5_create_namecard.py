#-*-coding:euc-kr

import time
import os
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import sys

print("Process Start.")
start_time = time.time()

personal_IDs= sys.argv[1] # 개인정보가 저장된 CSV파일 / ch3 실습파일 사용
logo_filename = sys.argv[2] # 명함에 삽입할 로고 파일

location = "경기도 파주시 문발동 광인사길 143"
url = "https://bit.ly/2FqKtba" # 저자 유튜브 채널이 나온다

out_dir ="namecards"
'''
if out_dir not in os.listdir():
    os.mkdir(out_dir)
'''
os.makedirs(out_dir, exist_ok=True)

# 로고 파일을 불러옵니다.
logo = Image.open(logo_filename)
logo_x, logo_y = logo.size

# 명함의 해상도를 지정합니다. 구글링 해 보니 1039*697 사이즈가 좋대요.
Xdim = 1039
Ydim = 697

# 로고 크기를 명함에 삽입하기 좋게 편집합니다. 명함은 세로가 짧으니 세로 길이를 기준으로 작업합니다.
# # 로고의 높이를 명함 높이의 40%로 조절합니다.
new_logo_y = int(Ydim * 0.4)
# new_logo_y : logo_y = new_logo_x : logo_x
new_logo_x = int(logo_x * (new_logo_y / logo_y))

# 명함에 삽입하기 좋게 로고 크기를 수정합니다.
resized_logo = logo.resize((new_logo_x, new_logo_y))

logo.close()
##### 이상 로고 사이즈 수정 끝 #####

# ch3에서 실습했던 그 csv 파일 불러오기
IDs = open(personal_IDs)
header = IDs.readline()

# 명함을 저장할 새로운 이미지를 제작해 줍니다.
# 참고로 배경색은 일단 흰색으로 지정합시다.
# 명함을 천 장 씩이나 찍어야 될 회사면 임원진 취향이 보수적일 가능성이 높으며
# 흰 색이 아닌 다른 명함을 원한다 하더라도 흰색이 아닌 다른 색 종이에 인쇄하면 됩니다.
image = Image.new("RGBA", (Xdim, Ydim), "white")

# 빈 명함 좌상단에 로고를 삽입하겠습니다.
# 대충 여백을 10%정도 주면 적당하겠죠? 이건 여러분의 취향에 달려 있습니다.
# 참고로.. s4에서 썼던 png 파일을 그대로 쓰고 paste함수에서 저자의 원코드
# image.paste(resized_logo, (int(Xdim * 0.1), int(Ydim * 0.1)))
# 이걸 그대로 사용하면 투명 표시하는 그리드 격자가 함께 포함되어 나옴. 해당 실습용 png 파일을 쓰던가 코드를 수정하던가 하자.
image.paste(resized_logo, (int(Xdim * 0.1), int(Ydim * 0.1)), resized_logo)
resized_logo.close()
##### 이상 수정된 로고 삽입 끝 #####


# 명함에 삽입할 폰트들을 결정합니다.
# 폰트 이름을 변경하시면 바뀝니다. 기본은 굴림입니다. 컴퓨터를 막 굴리기 때문입니다.
# 이름은 큰 글자로 삽입합시다.
nameFont = ImageFont.truetype("font/gulim.ttc", 100)
# URL과 주소는 구석에 작게 삽입할겁니다.
smallFont = ImageFont.truetype("font/gulim.ttc", 40)
# 나머지 정보들은 적당한 크기로 작성합니다.
infoFont = ImageFont.truetype("font/gulim.ttc", 50)

# 명함 우측 최상단에 URL을 삽입합니다.
# 좌우 여백은 맨 우측 5%를 띄울겁니다.
x_offset = int(Xdim * 0.95 - smallFont.getsize(url)[0])
# 상단 여백은 5%정도면 충분할 것 같습니다.
y_offset = int(Ydim * 0.05)
# 글자 삽입 함수
ImageDraw.Draw(image).text(xy=(x_offset, y_offset), text=url, font=smallFont, fill="black")

# 명함 하단에 사무실 주소를 입력합니다.
# 좌우 여백은 우측 5%를 띄울겁니다.
x_offset = int(Xdim * 0.95 - smallFont.getsize(location)[0])
# 하단 여백도 마찬가지로 5%정도면 예쁠 것 같군요.
y_offset = int(Ydim * 0.95 - smallFont.getsize(location)[1])
# 글자 삽입 함수
ImageDraw.Draw(image).text(xy=(x_offset, y_offset), text=location, font=smallFont, fill="black")

for line in IDs:
    splt = line.strip().split(",")

    # 명함에 들어갈 정보들만 추출합니다.
    name = splt[0]
    e_mail = splt[2]
    telephone = splt[3]

    # 명함 템플릿을 복제합니다.
    namecard = image.copy()

    # 이름을 삽입할겁니다.
    # 이름 사이사이 공백을 삽입해서 더 잘 보이게 합니다.
    temp_name = ""
    for el in name:
        temp_name += el + " "
    name = temp_name[:-1] # 맨 뒤에 공백 한칸은 넣을 필요 없으니까

    # 이름은 우측 여백을 10% 줍시다.
    x_offset = int(Xdim * 0.9 - nameFont.getsize(name)[0])
    # 상하 여백은 60%쯤 줍시다.
    y_offset = int(Ydim * 0.4 - nameFont.getsize(name)[1])
    # 명함에 이름을 삽입합니다.
    ImageDraw.Draw(namecard).text(xy=(x_offset, y_offset), text=name, font=nameFont, fill="black")

    # 그 밑에 전화번호를 삽입할겁니다.
    # 우측 여백을 10% 줍시다.
    x_offset = int(Xdim * 0.9 - infoFont.getsize(telephone)[0])
    # 상하 여백은 35%쯤 줍시다.
    y_offset = int(Ydim * 0.65 - infoFont.getsize(telephone)[1])
    # 명함에 이름을 삽입합니다.
    ImageDraw.Draw(namecard).text(xy=(x_offset, y_offset), text=telephone, font=infoFont, fill="black")

    # 그 밑에 이메일을 삽입할겁니다.
    # 우측 여백을 10% 줍시다.
    x_offset = int(Xdim * 0.9 - infoFont.getsize(e_mail)[0])
    # 상하 여백은 25%쯤 줍시다.
    y_offset = int(Ydim * 0.75 - infoFont.getsize(e_mail)[1])
    # 명함에 이름을 삽입합니다.
    ImageDraw.Draw(namecard).text(xy=(x_offset, y_offset), text=e_mail, font=infoFont, fill="black")

    # 완성된 명함을 저장합니다.
    namecard.save(out_dir + "/" + name + "_" + telephone + ".png")
    namecard.close()
    ##### 이상 명함 1장 만들기 끝 #####

image.close()
##### 이상 명함 전체 작업 끝 #####

print("Process Done.")
end_time = time.time()
print("The Job Took " + str(end_time - start_time) + " seconds.")
