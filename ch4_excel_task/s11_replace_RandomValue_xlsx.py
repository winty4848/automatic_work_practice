#-*-coding:euc-kr
# 실무에서 실제 실행시킬 일은 없겠지만 저자는 파일 삭제용으로 활용해보라고 함
# 삭제 유틸리티가 안깔려있다면 생각해볼만한 솔루션이 될 지도

import time
import os
import pyexcel as px
import sys
import random


directory = sys.argv[1]
percent = float(sys.argv[2])/100
input_files = os.listdir(directory)

terror_value = ["고양이", "야옹", "야옹이", "미야옹", "팀장님사랑해요"]

for filename in input_files:
    if ".xlsx" not in filename:
        continue
    data = px.get_array(file_name=directory + "/" + filename)

    os.remove(directory + "/" + filename)

    for i in range(len(data)):
        for j in range(len(data[i])):
            # 확률상 당첨이 되었다면 데이터를 파괴
            if random.random() < percent:
                if int(str(time.time())[-1])>5:
                    data[i][j] = random.choice(terror_value)
                else:
                    data[i][j] = random.uniform(1,1000)

    px.save_as(array=data, dest_file_name=directory + "/" + filename)