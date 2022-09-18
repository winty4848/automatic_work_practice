#-*-coding:euc-kr

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# 네이버는 봇감지가 있어서 그런가 안된다. 나중에 다른 방법을 찾아보자
# 트위터 로그인 창 구성이 바뀌어서 저자가 제시한 코드로는 안된다
# find_element 사용해서 바꿔주기로 결정

class LoginBot:
    def __init__(self):
        # 셀레늄 웹드라이버에 입력할 옵션을 지정합니다.
        self.options = Options()
        # 옵션에 해상도를 입력합니다.
        self.options.add_argument("--window-size=1600,900")

    def go_to_tw(self):
        # 옵션을 입력해서 크롬 웹드라이버를 불러옵니다.
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=self.options)
        # 트위터만 진행하기로 함.
        self.driver.get("https://twitter.com/i/flow/login")
        time.sleep(3)


    # 크롤러를 종료하는 메서드입니다.
    # 굳이 한줄짜리 코드를 함수로 만든 데에는 여러 이유가 있습니다만,
    # 쉽게 설명하자면 클래스 외부에서 클래스 내부 자료에 너무 깊게 관여하는 상황을 원하지 않기 때문입니다.
    def kill(self):
        self.driver.quit()

    # 로그인을 수행하는 메서드입니다.
    def login(self, id, pw):
        # 이상하게 id,pw 입력칸의 xpath로는 계속 element 찾을 수 없다는 오류 발생함... ㅠ name태그로 진행하자
        self.driver.find_element(By.NAME, "text").send_keys(id)
        next_button_xpath='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]'
        self.driver.find_element(By.XPATH,next_button_xpath).click()
        time.sleep(3)
        self.driver.find_element(By.NAME, "password").send_keys(pw)
        login_button_xpath='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div'
        self.driver.find_element(By.XPATH, login_button_xpath).click()

    def save_screenshot(self):
        self.driver.save_screenshot("test.png")
