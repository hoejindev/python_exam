#======================================
# 0) 브라우저 실행 + 페이지 접속
#======================================
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://quotes.toscrape.com/')

#======================================
# 2) 다음 페이지 이동 + 반복 수집
#======================================

# 최대 몇 페이지까지 수집할 지 제한하는 상수
# 무한 크롤링을 방지하기 위한 안전 장치
MAX_PAGES = 3

#현재 페이지 번호를 추적하기 위한 변수
current_page = 1

#수집한 데이터를 담을 리스트
results = []

while current_page <= MAX_PAGES:
    print(f'======{current_page}페이지 수집 중 =====')
    quote_blocks = driver.find_elements(By.CLASS_NAME, 'quote')

    for block in quote_blocks:
        quote_text = block.find_element(By.CLASS_NAME, 'text').text
        author = block.find_element(By.CLASS_NAME, 'author').text
        
        tag_elements = block.find_elements(By.CLASS_NAME, 'tag')
        tags = [t.text for t in tag_elements]

        results.append({
                'page' : current_page,
                'quote': quote_text,
                'author': author,
                'tags': tags
            })
    # Next 버튼 찾기
    # 'li.next a'는 class='next'를 가진 li 태그 안에 있는 a 태그를 의미
    # CSS_SELECTOR : CSS문법을 이용해서 HTML 요소를 찾는 방법
    # Selenium에서 가장 많이 쓰는 방식 중 하나
    next_buttons = driver.find_elements(By.CSS_SELECTOR, 'li.next a')

    if not next_buttons:
        print('다음 페이지가 없어 종료합니다.')
        break

    #다음 페이지로 이동
    next_buttons[0].click()

    # 페이지 번호 1 증가
    current_page += 1

print('최종 수집 개수 :', len(results))

# 최종 수집된 결과에서 page 번호와 quote 텍스트만 출력함
for r in results:
    print(r['page'], r['quote'])

driver.quit()

