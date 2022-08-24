#-*-coding:euc-kr
import time
import os

print("작업시작")
start_time=time.time()

# 합칠 파일들이 저장된 폴더명
directory="personal_fake_info"

output_name="merge_ID.csv"

# 결과물 파일 생성
output=open(output_name, 'w')

input_files=os.listdir(directory)

# 엑셀 헤더 관련 변수 정의 (칼럼명)
headers=[]
output_header = False # 초기값 F 지정

for filename in input_files:
    if ".txt" not in filename:
        continue
    file = open(directory + "/" + filename)

    # 파일의 내용물을 저장할 리스트를 정의합니다.
    contents = []

    # 현재 행마다 데이터가 나뉘어져 있으니 한 줄씩 데이터 리딩
    for line in file:
        # 현재 텍스트파일은 따옴표를 기점으로 실데이터가 삽입되어 있다는 점 착안
        if ":" in line:
            # split 수행 시 ['age', '43'] 출력됨. 즉 리스트의 마지막 인덱스에 실데이터
            splits = line.split(":")
            # strip()은 문자열에서 양쪽의 공백 제거. 즉 다른데이터 유형에서는 작동 안함.
            contents.append(splits[-1].strip())

            # 헤더를 정리합니다. 최초 1회만 실행됩니다.
            if len(contents) > len(headers):
                headers.append(splits[0].strip())

    # 헤더를 파일에 입력합니다. 최초 1회만 실행됩니다.
    if not output_header:
        header = ",".join(headers)
        output.write(header)
        output_header = True

    # 결과물 파일에 내용물을 입력합니다.
    # 저자 깃허브에는 ', ' 으로 제시되어 있으나 이렇게하면 결과물 파일에 두번째 열부터 문자앞에 공백이 한칸 생김.
    new_line = ",".join(contents)
    print(new_line)
    output.write("\n" + new_line)

    # 읽어온 파일을 종료합니다.
    file.close()

output.close()

print("작업종료")

end_time=time.time()
print("소요시간 : " + str(end_time - start_time) + " 초")