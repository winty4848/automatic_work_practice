import sys

def change_form(filename):
    in_file = open(filename, encoding="euc-kr")
    out_file = open("utf8_" + filename, 'w', encoding="utf-8")

    content = in_file.read()
    out_file.write(content)

    in_file.close()
    out_file.close()

# python euc_to_utf.py merge_ID.csv
filename = sys.argv[1]

# euc-kr로 인코딩된 파일을 실행
input = open(filename, encoding="euc-kr")

# utf-8로 저장할 파일을 실행
output = open("utf8_" + filename, 'w', encoding="utf-8")

content = in_file.read()

output.write(content)

input.close()
output.close()


