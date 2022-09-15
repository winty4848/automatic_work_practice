#-*-coding:euc-kr

import time
import os
from PIL import Image
import sys

print("Process Start.")
start_time = time.time()

image_filename = sys.argv[1]

out_dir ="augmentation"
'''
if out_dir not in os.listdir():
    os.mkdir(out_dir)
'''
os.makedirs(out_dir, exist_ok=True)

image = Image.open(image_filename)
Xdim, Ydim = image.size

# 저장된 파일 개수를 저장해 둘 카운터를 생성합니다.
COUNT = 1

# 일단 원본을 저장합니다. 2의 0승
# 저장할 파일의 이름을 입력합니다.
temp_new_file_name = "%05d.png" %COUNT
# 카운트를 1 증가시킵니다.
COUNT += 1
# 원본 이미지를 저장합니다.
image.save(out_dir + "/" + temp_new_file_name)
image.close()

# 출력 파일명을 저장할 리스트를 만듭니다.
FILELIST = [temp_new_file_name]


# 폴더 내의 이미지를 모두 읽어와 좌우대칭을 저장합니다. 2의 1승
for i in range(len(FILELIST)):
    # 파일을 불러옵니다.
    image = Image.open(out_dir + "/" + FILELIST[i])
    '''
    # %05d 의미
    뒤에있는 변수 가져와서 5자리 숫자로 작성하고 빈자리는 0으로 채워줘
    만약 5자리를 초과하면 그냥 있는 그대로 표시해주면 됨
    '''
    new_temp_name = "%05d.png" %COUNT
    COUNT += 1

    image = image.transpose(Image.FLIP_LEFT_RIGHT)
    image.save(out_dir + "/" + new_temp_name)
    image.close()

    FILELIST.append(new_temp_name)


# 리스트 안의 이미지를 모두 읽어와 상하대칭을 저장합니다. 2의 2승
for i in range(len(FILELIST)):
    image = Image.open(out_dir + "/" + FILELIST[i])
    new_temp_name = "%05d.png" % COUNT
    COUNT += 1

    # 이미지를 상하 반전합니다.
    image = image.transpose(Image.FLIP_TOP_BOTTOM)
    image.save(out_dir + "/" + new_temp_name)
    image.close()

    FILELIST.append(new_temp_name)


# 리스트 안의 이미지를 모두 읽어와 흑백버전을 저장합니다. 2의 3승
for i in range(len(FILELIST)):
    image = Image.open(out_dir + "/" + FILELIST[i])
    new_temp_name = "%05d.png" % COUNT
    COUNT += 1

    image = image.convert('1')
    image.save(out_dir + "/" + new_temp_name)
    image.close()

    FILELIST.append(new_temp_name)


# 리스트 안의 이미지(원본, 좌우, 상하, 흑백)를 모두 읽어와 1도씩 회전합니다. 2의 3승 * 180
for el in FILELIST:
    for i in range(180):
        # 깔끔하게 1,000장만 만듭시다.
        # 결과물이 1000개를 넘어서면 코드를 종료합니다.
        if COUNT > 1000:
            break
        image = Image.open(out_dir + "/" + el)
        new_temp_name = "%05d.png" % COUNT
        COUNT += 1

        # 사진을 회전시킵니다.
        image = image.rotate(i+1)
        # 간혹 이미지 크기가 변경된다는 이야기가 있어 resize()를 실행합니다.
        image = image.resize((Xdim, Ydim))

        image.save(out_dir + "/" + new_temp_name)
        image.close()


print("Process Done.")
end_time = time.time()
print("The Job Took " + str(end_time - start_time) + " seconds.")
