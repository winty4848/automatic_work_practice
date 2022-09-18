#-*-coding:euc-kr

import sys
import time
import s1_auto_login as al


# 작업 시작 메시지를 출력합니다.
print("Process Start.")

# 시작 시점의 시간을 기록합니다.
start_time = time.time()

# 아이디를 입력받습니다.
id = sys.argv[1]

# 패스워드를 입력받습니다.
ps = sys.argv[2]

# 크롤러를 불러옵니다.
crawler = al.LoginBot()

# 로그인을 시도합니다.
crawler.login(id, ps)

# 로그인에 성공했으니 스크린샷이나 한 번 찍어줍시다.
crawler.save_screenshot()

# 작업 종료 메세지를 출력합니다.
print("Process Done.")

# 작업에 총 몇 초가 걸렸는지 출력합니다.
end_time = time.time()
print("The Job Took " + str(end_time - start_time) + " seconds.")
