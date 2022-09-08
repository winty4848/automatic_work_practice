#-*-coding:euc-kr

import time
import os
import numpy as np
from PIL import Image

print("Process Start.")
start_time = time.time()

NUM_SAMPLES = 1000

out_dir ="random_image"
if out_dir not in os.listdir():
    os.mkdir(out_dir)


for i in range(NUM_SAMPLES):
    name = str(time.time())[-7:] + ".png"
    Xdim, Ydim = np.random.randint(100, 400, size=2) # 출력값 [X, Y]꼴
    # 맨 아래 주석 참고
    # uint8은 부호없는 정수만 출력 + PIL 라이브러리에서 사용하는 포맷
    image = np.random.randint(256, size=(Xdim, Ydim, 3)).astype('uint8')
    # numpy 배열을 이미지 형태로 바꾸기
    result = Image.fromarray(image)

    result.save(out_dir + "/" +name)
    result.close()

print("Process Done.")
end_time = time.time()
print("The Job Took " + str(end_time - start_time) + " seconds.")

'''
컬러사진으로 구성할 경우 RGB값이 포함되어야 함
np.random.randint(256, size=(2,4,3)) 이라면
[[[202  10   3]
[206  35  80]
[224 114 108]
[ 26   1 255]]

[[ 25 186  12]
[129 206  70]
[100 181   5]
[157  14  58]]]
이런 형태로 출력됨.
[0][0]은 사진 파일의 1행 1열을 담당하고
[0][0][0] 은 R
[0][0][1] 은 G
[0][0][2] 은 B
'''