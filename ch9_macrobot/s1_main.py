#-*-coding:euc-kr

import sys
import time
import s1_auto_login as al


# �۾� ���� �޽����� ����մϴ�.
print("Process Start.")

# ���� ������ �ð��� ����մϴ�.
start_time = time.time()

# ���̵� �Է¹޽��ϴ�.
id = sys.argv[1]

# �н����带 �Է¹޽��ϴ�.
ps = sys.argv[2]

# ũ�ѷ��� �ҷ��ɴϴ�.
crawler = al.LoginBot()

# �α����� �õ��մϴ�.
crawler.login(id, ps)

# �α��ο� ���������� ��ũ�����̳� �� �� ����ݽô�.
crawler.save_screenshot()

# �۾� ���� �޼����� ����մϴ�.
print("Process Done.")

# �۾��� �� �� �ʰ� �ɷȴ��� ����մϴ�.
end_time = time.time()
print("The Job Took " + str(end_time - start_time) + " seconds.")
