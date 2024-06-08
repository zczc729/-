#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# search_kakao_map.py

from selenium import webdriver
import pandas as pd
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import sys

def search_kakao_map(keyword):
    # 웹 드라이버 설정
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    kakao_map_search_url = f"https://map.kakao.com/?q={keyword}"

    driver.get(kakao_map_search_url)

    # 현재 복사한 순서, 페이지 번호 설정
    ind = 1  # 현재 복사한 순서
    no = 1  # 1~5페이지 중 위치한 곳
    page = 1  # 현재 페이지 번호
    list1 = []  # 결과물이 저장되는 리스트

    # '인기도' 버튼 클릭하여 인기도 순으로 정렬
    driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH, '//a[contains(text(), "인기도순")]'))
    time.sleep(3)  # 페이지 로드를 기다리기 위해 3초 대기

    while True:
        try:
            # 업체명, 주소, 전화번호, 평점 추출
            title = driver.find_element(By.CSS_SELECTOR, f'#info\\.search\\.place\\.list > li:nth-child({ind}) > div.head_item.clickArea > strong.tit_name > a.link_name').text
            address = driver.find_element(By.CSS_SELECTOR, f'#info\\.search\\.place\\.list > li:nth-child({ind}) > div.info_item > div.addr > p[data-id="address"]').text
            phone = driver.find_element(By.CSS_SELECTOR, f'#info\\.search\\.place\\.list > li:nth-child({ind}) > div.info_item > div.contact.clickArea > span.phone').text
            rating_element = driver.find_element(By.CSS_SELECTOR, f'#info\\.search\\.place\\.list > li:nth-child({ind}) > div.rating.clickArea > span.score > em.num')
            rating = rating_element.text if rating_element.is_displayed() else None
            if rating is not None:
                list1.append([title, address, phone, float(rating)])
            ind += 1

        except NoSuchElementException:
            # 더보기 버튼 찾기
            try:
                if driver.find_element(By.CSS_SELECTOR, '#info\\.search\\.place\\.more').is_displayed():
                    driver.execute_script("arguments[0].click();", driver.find_element(By.CSS_SELECTOR, '#info\\.search\\.place\\.more'))
                    no = 1
                    ind = 1
                    page += 1
                    time.sleep(3)  # 페이지가 로드될 시간을 주기 위해 일시 중지
                    if page == 3:
                        break
                    continue
            except (NoSuchElementException, ElementClickInterceptedException):
                pass

            # 다음 페이지로 이동
            try:
                if no >= 5:
                    driver.find_element(By.CSS_SELECTOR, f'#info\\.search\\.page\\.next').click()
                    no = 1
                    ind = 1
                    page += 1
                    time.sleep(3)  # 페이지가 로드될 시간을 주기 위해 일시 중지
                    if page == 3:
                        break
                    continue
            except NoSuchElementException:
                pass

            # 5페이지 단위마다 다음 페이지 버튼 누르기
            try:
                if driver.find_element(By.CSS_SELECTOR, f'#info\\.search\\.page\\.no{no+1}').is_displayed():
                    no += 1
                    driver.execute_script("arguments[0].click();", driver.find_element(By.CSS_SELECTOR, f'#info\\.search\\.page\\.no{no}'))
                    ind = 1
                    page += 1
                    time.sleep(3)  # 페이지가 로드될 시간을 주기 위해 일시 중지
                    if page == 3:
                        break
                    continue
            except NoSuchElementException:
                break

    # 데이터 프레임으로 변환
    df = pd.DataFrame(list1, columns=['Title', 'Address', 'Phone', 'Rating'])

    # 평점이 없는 행 제거
    df = df.dropna()

    # 평점을 기준으로 내림차순 정렬
    df = df.sort_values(by='Rating', ascending=False)

    # 상위 10개 추출
    top_10 = df.head(10)

    # CSV 파일로 저장
    top_10.to_csv(f'./맛집_찾기_{keyword}.csv', index=False)

    # 드라이버 종료
    driver.quit()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python search_kakao_map.py [keyword]")
        sys.exit(1)
    keyword = " ".join(sys.argv[1:])
    search_kakao_map(keyword)

