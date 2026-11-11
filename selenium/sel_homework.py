
"""
연습 사이트: https://quotes.toscrape.com/
"""

from selenium import webdriver
from selenium.webdriver.common.by import By


# -------------------------------------------------
# 공통: 드라이버 실행 및 1페이지 접속
# -------------------------------------------------
driver = webdriver.Chrome()
driver.get("https://quotes.toscrape.com/")

'''
# =================================================
# 문제 1 (기초)
# =================================================
"""
[문제 1]
1페이지에서 모든 명언(text)과 저자(author)를 출력하세요.

출력 형식:
명언 - 저자

조건:
- find_elements()를 사용하세요.
- 각 quote 블록 안에서 다시 요소를 찾으세요.
"""
results = []

quote_blocks = driver.find_elements(By.CLASS_NAME, 'quote')

for block in quote_blocks:
    quote_text = block.find_element(By.CLASS_NAME, 'text').text
    author = block.find_element(By.CLASS_NAME, 'author').text
    results.append({
           'quote': quote_text,
           'author':author
       })

for line in results:
    print(f"{line['quote']} - {line['author']}")





# =================================================
# 문제 2 (중급)
# =================================================
"""
[문제 2]
1페이지에서 각 명언의 태그 개수를 함께 출력하세요.

출력 형식 예:
명언 - 저자 (태그 3개)

조건:
- 태그는 class="tag" 입니다.
- 태그는 여러 개일 수 있습니다.
- len()을 활용하세요.
"""
results = []

quote_blocks = driver.find_elements(By.CLASS_NAME, 'quote')

for block in quote_blocks:
    quote_text = block.find_element(By.CLASS_NAME, 'text').text
    author = block.find_element(By.CLASS_NAME, 'author').text
    tags = block.find_elements(By.CLASS_NAME, 'tag')
    results.append({
        'quote': quote_text,
        'author':author,
        'tag_count':len(tags)
    })

for line in results:
    print(f"{line['quote']} - {line['author']} (태그 {line['tag_count']}개)")

# =================================================
# 문제 3 (중상)
# =================================================
"""
[문제 3]
2페이지까지 이동하여 총 몇 개의 명언을 수집했는지 출력하세요.

조건:
- Next 버튼을 클릭하세요.
- 반복문을 사용하세요.
- 페이지 이동 후 다시 요소를 수집하세요.
"""
# 최대 몇 페이지까지 수집할 지 제한하는 상수
MAX_PAGES = 2

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


# =================================================
# 문제 4 (활용)
# =================================================
"""
[문제 4]
3페이지까지 수집하면서, 태그에 "love"가 포함된 명언만 출력하세요.

출력 형식:
[LOVE] 명언 - 저자

조건:
- 태그 목록(tags) 안에 "love"가 있으면 출력합니다.
"""
# 최대 몇 페이지까지 수집할 지 제한하는 상수
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

for result in results:
    if 'love' in result['tags']:
        print(f"[LOVE] {result['quote']} - {result['author']}")
'''

# =================================================
# 문제 5 (도전)
# =================================================
"""
[문제 5]
3페이지까지 수집한 뒤, 저자별로 명언이 몇 개 있는지 출력하세요.

출력 예:
Albert Einstein : 2개
Mark Twain : 3개

조건:
- 딕셔너리를 사용하세요.
- key = author, value = 개수
"""
# 최대 몇 페이지까지 수집할 지 제한하는 상수
MAX_PAGES = 3

#현재 페이지 번호를 추적하기 위한 변수
current_page = 1

#수집한 데이터를 담을 리스트
collected = []

while current_page <= MAX_PAGES:
    print(f'======{current_page}페이지 수집 중 =====')
    quote_blocks = driver.find_elements(By.CLASS_NAME, 'quote')

    for block in quote_blocks:
        quote_text = block.find_element(By.CLASS_NAME, 'text').text
        author = block.find_element(By.CLASS_NAME, 'author').text
       
        collected.append({
                       'author': author
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

results = {}
for data in collected:
    if data['author'] in results:
        results[data['author']] = results[data['author']] + 1
    else:     
        results[data['author']] = 1

for key, value in results.items():
    print(f"{key} : {value}개")

# -------------------------------------------------
# 브라우저 종료
# -------------------------------------------------
driver.quit()