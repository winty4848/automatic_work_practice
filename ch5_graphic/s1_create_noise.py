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
    Xdim, Ydim = np.random.randint(100, 400, size=2) # ��°� [X, Y]��
    # �� �Ʒ� �ּ� ����
    # uint8�� ��ȣ���� ������ ��� + PIL ���̺귯������ ����ϴ� ����
    image = np.random.randint(256, size=(Xdim, Ydim, 3)).astype('uint8')
    # numpy �迭�� �̹��� ���·� �ٲٱ�
    result = Image.fromarray(image)

    result.save(out_dir + "/" +name)
    result.close()

print("Process Done.")
end_time = time.time()
print("The Job Took " + str(end_time - start_time) + " seconds.")

'''
�÷��������� ������ ��� RGB���� ���ԵǾ�� ��
np.random.randint(256, size=(2,4,3)) �̶��
[[[202  10   3]
[206  35  80]
[224 114 108]
[ 26   1 255]]

[[ 25 186  12]
[129 206  70]
[100 181   5]
[157  14  58]]]
�̷� ���·� ��µ�.
[0][0]�� ���� ������ 1�� 1���� ����ϰ�
[0][0][0] �� R
[0][0][1] �� G
[0][0][2] �� B
'''