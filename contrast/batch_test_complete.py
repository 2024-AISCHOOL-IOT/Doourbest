#!/usr/bin/env python
# coding: utf-8

# In[5]:


# 1. 로그인 유지법
#   >> options.add_argument("user-data-dir=c:\\user_data\\YC") 
#   >> 셀레니움 사용시 항상 로그인이 풀린다. 
#   >> 그래서 로그인 데이터를 저장해서 로그인 풀림을 방지한다.
#   >> 폴더명 YC부분을 원하는 폴더명으로 바꾼다

# 2. 작업 스케줄러 등록
#   >> 파일을 Executable Script로 저장
#   >> 윈도우 검색창 '스케줄' 입력 및 실행
#   >> 작업 만들기 
#   >> 트리거: 원하는 시간 설정
#   >> 동작:
#   >> 프로그램/스크립트: python.exe 경로 찾아서 입력
#   >> 인수 추가(옵션): 파일명
#   >> 시작 위치(옵션): 파일 경로

from selenium import webdriver # webdriver 시작
from selenium.webdriver.common.by import By # By.XPATH, BY.NAME ...
from selenium.webdriver.chrome.options import Options # 옵션들 설정
from selenium.webdriver.common.keys import Keys # click()??
from datetime import datetime # 현재시간(년, 월, 일) 가져오기
import time # 대기 시간 설정해주기
import pyautogui as pag  # 키보드 입력한 것처럼 속이기

options = Options()
options.add_argument("user-data-dir=c:\\user_data\\YC")  # 경로지정 YC 이부분만 원하는 이름으로 변경, 로그인을 유지시켜주는 옵션, 첫 로그인 후 화면 닫고 재시작
options.add_argument("--start-maximized") # 창 최대화
options.add_experimental_option("detach",True) # 이렇게 하면 화면이 안꺼진다합니다

driver = webdriver.Chrome(options=options)  # options=options, 위에 옵션들을 적용 해준다

url = "https://2024aischool.elice.io/my" # url 주소
driver.get(url) # url 열기

# 로그인 창에서 로그인하는 방법:(이제 미사용!) 
# 엘리스 홈페이지 로그인창 (아이디, 비번, 로그인 버튼)
# if driver.current_url == "https://accounts.elice.io/accounts/signin/me?continue_to=https%3A%2F%2F2024aischool.elice.io%2Fmy&lang=ko&org=2024aischool":
#     driver.find_element(By.NAME,"loginId").send_keys("아이디")         # <--------------- 아이디 입력 따옴표
#     driver.find_element(By.NAME,"password").send_keys("비밀번호")      # <--------------- 비밀번호 입력 따옴표
#     driver.find_element(By.ID,"mui-3").send_keys(Keys.ENTER)

pag.press('esc')  # 주소창에서 탈출
pag.press('esc')  # 팝업창 닫기
driver.implicitly_wait(10)

# Implicitly wait을 10초로 설정하면 페이지가 로딩되는데 10초까지 기다립니다. 
# 만약 페이지 로딩이 2초에 완료되었다면 더 기다리지 않고 다음 코드를 수행합니다. 
# 기본 설정은 0초로 되어있고, 한번만 설정하면 driver를 사용하는 모든 코드에 적용이 됩니다.



# 버튼 테스트
# 퇴실 버튼: "//*[@id='root']/div[1]/div/main/div[2]/div/div/div[2]/section[2]/div[2]/div/div[2]/button"
# 출석 버튼: "//*[@id='root']/div[1]/div/main/div[2]/div/div/div[2]/section[2]/div[2]/div/div[2]/div/button"
# 테스트 버튼: "//*[@id='root']/div[1]/div/main/div[1]/div/div/div[2]/ul/a[2]/div[2]/p"
             

try:
    if datetime.now().hour >= 17:
        driver.find_element(By.XPATH, "//*[@id='root']/div[1]/div/main/div[2]/div/div/div[2]/section[2]/div[2]/div/div[2]/button").click()
        print("퇴실이 완료되었습니다.")
        
    else:
        driver.find_element(By.XPATH, "//*[@id='root']/div[1]/div/main/div[2]/div/div/div[2]/section[2]/div[2]/div/div[2]/div/button").click()
        print("출석이 완료되었습니다.")
        
except:
    print("!!!!!!!!!!출퇴실 버튼이 활성화가 안됬습니다.!!!!!!!!!!")

# driver.find_element(By.CSS_SELECTOR, "#search-btn").click()

# 스크린샷 코드
# driver.save_screenshot("naver_인공지능.png")


# 크롬브라우저 닫기
# driver.quit()


# In[5]:





# In[3]:




