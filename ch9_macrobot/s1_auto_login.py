#-*-coding:euc-kr

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# ���̹��� �������� �־ �׷��� �ȵȴ�. ���߿� �ٸ� ����� ã�ƺ���
# Ʈ���� �α��� â ������ �ٲ� ���ڰ� ������ �ڵ�δ� �ȵȴ�
# find_element ����ؼ� �ٲ��ֱ�� ����

class LoginBot:
    def __init__(self):
        # ������ ������̹��� �Է��� �ɼ��� �����մϴ�.
        self.options = Options()
        # �ɼǿ� �ػ󵵸� �Է��մϴ�.
        self.options.add_argument("--window-size=1600,900")

    def go_to_tw(self):
        # �ɼ��� �Է��ؼ� ũ�� ������̹��� �ҷ��ɴϴ�.
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=self.options)
        # Ʈ���͸� �����ϱ�� ��.
        self.driver.get("https://twitter.com/i/flow/login")
        time.sleep(3)


    # ũ�ѷ��� �����ϴ� �޼����Դϴ�.
    # ���� ����¥�� �ڵ带 �Լ��� ���� ������ ���� ������ �ֽ��ϴٸ�,
    # ���� �������ڸ� Ŭ���� �ܺο��� Ŭ���� ���� �ڷῡ �ʹ� ��� �����ϴ� ��Ȳ�� ������ �ʱ� �����Դϴ�.
    def kill(self):
        self.driver.quit()

    # �α����� �����ϴ� �޼����Դϴ�.
    def login(self, id, pw):
        # �̻��ϰ� id,pw �Է�ĭ�� xpath�δ� ��� element ã�� �� ���ٴ� ���� �߻���... �� name�±׷� ��������
        self.driver.find_element(By.NAME, "text").send_keys(id)
        next_button_xpath='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]'
        self.driver.find_element(By.XPATH,next_button_xpath).click()
        time.sleep(3)
        self.driver.find_element(By.NAME, "password").send_keys(pw)
        login_button_xpath='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div'
        self.driver.find_element(By.XPATH, login_button_xpath).click()

    def save_screenshot(self):
        self.driver.save_screenshot("test.png")
