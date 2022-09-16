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
member_photo = sys.argv[1] # s6���� �۾��� ���� ����ϸ� ��
personal_IDs = sys.argv[2] # ch3���� �۾��Ѱ� ����ϸ� ��
logo_filename = sys.argv[3] # s4 �ΰ� ���
template_filename = sys.argv[4] # ���ڰ� �غ��ص� �� ����

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
������ ����� ���ϸ��� ���� ������ ��� ���� s6ó�� %05d�� �̿��ص� �Ǳ� �Ѵ�
������ �� �ڵ忡���� �������� �ް����� %05d�� ����ϴ°� ���ƺ���.
�ٸ� �Ϲ����� ��쿡�� ������ ����ڵ� ���� key���� ����Ͽ� �̸��� ���� ������ ����Ʈ �̿��� ����� �˾Ƶ־� �� �� ����.
'''

# ���ݱ��� ������ ���� ����
COUNT = 0

# �ΰ� ũ�⸦ �����ϱ� ���� �����մϴ�. ������� ���ΰ� ª���� ���� ���̸� �������� �۾��մϴ�.
# �ΰ��� �ʺ� ����� �ʺ��� 20%�� �����մϴ�.
new_logo_x = int(Xdim * 0.2)
# new_logo_y : logo_y = new_logo_x : logo_x
new_logo_y = int(logo_y * (new_logo_x / logo_x))
resized_logo = logo.resize((new_logo_x, new_logo_y))
logo.close()


# csv ���� ����
IDs = open(personal_IDs)
header = IDs.readline()

# �� ����� ���ϴܿ� �ΰ� �����ϰڽ��ϴ�.
# ���� ������ 10%, 5%���� �ָ� �����ϰ���? �̰� �������� ���⿡ �޷� �ֽ��ϴ�.
template.paste(resized_logo, (int(Xdim * 0.1), int(Ydim * 0.95 - new_logo_y)))
resized_logo.close()

MainFont = ImageFont.truetype("font/gulim.ttc", 0)
nameFont = ImageFont.truetype("font/gulim.ttc", 100)
smallFont = ImageFont.truetype("font/gulim.ttc", 40)

# ����� ���� �ֻ�ܿ� URL�� �����մϴ�.
# �¿� ������ �� ���� 5%�� ���̴ϴ�.
x_offset = int(Xdim * 0.95 - smallFont.getsize(url)[0])
# ��� ������ 2%������ ����� �� �����ϴ�.
y_offset = int(Ydim * 0.02)
# ������� Ȩ������ �ּҸ� �����մϴ�.
ImageDraw.Draw(template).text(xy=(x_offset, y_offset), text=url, font=smallFont, fill="black")


for line in IDs:
    splt = line.strip().split(",")
    name = splt[0] # ������� �� �����鸸 ����

    idcard = template.copy() # ���ø� ����
    photo_for_id = Image.open(member_photo + "/" + PHOTOS[COUNT]) # ���� ����
    # ������ �ʺ� ����� �ʺ��� 50% ũ��� �����մϴ�.
    photo_for_id = photo_for_id.resize((int(Xdim/2), int(Xdim/2 * (4/3))))
    # ������ ����� �� �߾ӿ� �����սô�.
    idcard.paste(photo_for_id, (int(Xdim/4), int(Ydim/2 - Xdim/2*(4/3)/2)))

    temp_name = ""
    for el in name:
        temp_name += el + " "
    name = temp_name[:-1] #s5 �ּ�

    # �̸��� �¿� ��������Ұ̴ϴ�.
    x_offset = int(Xdim * 0.5 - nameFont.getsize(name)[0]/2)
    # ���� ������ 20%�� �ݽô�.
    y_offset = int(Ydim * 0.8 - nameFont.getsize(name)[1])
    # ���Կ� �̸��� �����մϴ�.
    ImageDraw.Draw(idcard).text(xy=(x_offset, y_offset), text=name, font=nameFont, fill="black")

    idcard.save(out_dir + "/" + PHOTOS[COUNT])
    idcard.close()
    COUNT += 1

template.close()


print("Process Done.")
end_time = time.time()
print("The Job Took " + str(end_time - start_time) + " seconds.")
