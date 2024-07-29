#!/usr/bin/env python
# coding: utf-8

# In[5]:


#!/usr/bin/env python
# coding: utf-8

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from IPython.display import display

chrome_driver_path = './ChromeDriver/chromedriver.exe'

def fetch_nba_data(base_url):
    num_periods = input("'ALL', 1, 2, 3, 4, '1stHalf', '2ndHalf' 중 하나를 입력해주세요: ")
    if num_periods not in ['1', '2', '3', '4', 'ALL', '1stHalf', '2ndHalf']:
        num_periods = 'ALL'
    
    # ChromeDriver 설정
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service)

    df_dict = {}
    
    # URL 접속
    url = f'{base_url}?period=Q{num_periods}' if num_periods in ['1', '2', '3', '4'] else base_url
    driver.get(url)
    
    # 페이지 로드 대기
    wait = WebDriverWait(driver, 10)
    tables = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'StatsTable_table__Ejk5X')))
    
    # BeautifulSoup으로 페이지 파싱
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    # h2 태그에서 팀 이름 추출
    h2_tags = soup.find_all('h2', class_='GameBoxscoreTeamHeader_gbt__b9B6g')
    if len(h2_tags) >= 2:
        team1 = h2_tags[0].get_text(strip=True)
        team2 = h2_tags[1].get_text(strip=True)
    else:
        team1 = "Team 1"
        team2 = "Team 2"
    
    # 테이블을 저장할 리스트 초기화
    period_tables = []
    
    # 각 테이블에 대해 데이터 추출
    for idx, table in enumerate(tables):
        # 테이블 HTML 추출
        html = table.get_attribute('outerHTML')
        
        # BeautifulSoup으로 테이블 파싱
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find('table')
        
        # 헤더 추출
        thead = table.find('thead')
        headers = [th.get_text(strip=True) for th in thead.find_all('th')]
        
        # 데이터 추출
        rows = []
        tbody = table.find('tbody')
        for tr in tbody.find_all('tr'):
            cells = tr.find_all(['th', 'td'])
            row = [cell.get_text(strip=True) for cell in cells]
            rows.append(row)
            
        # 데이터프레임 생성
        period_table_df = pd.DataFrame(rows, columns=headers)
        period_tables.append((team1 if idx == 0 else team2, period_table_df))
    
    # 결과 출력 (Jupyter Notebook에서 보기 쉽게)
    print(f"DataFrames for Q{num_periods}:")
    for team_name, df in period_tables:
        print(f"Team: {team_name}")
        display(df)
    
    # 각 쿼터의 테이블을 딕셔너리에 저장
    df_dict[num_periods] = period_tables
    
    driver.quit()
    return df_dict

# 함수 호출 예시
# chrome_driver_path = 'C:/Users/USER/Downloads/chromedriver-win64 (2)/chromedriver-win64/chromedriver.exe'
# base_url = 'https://www.nba.com/game/gsw-vs-mia-1322200005/box-score'

# nba_data = fetch_nba_data(base_url)

