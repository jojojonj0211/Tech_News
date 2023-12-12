import requests
from bs4 import BeautifulSoup

def crawl_tech_news1():
    url = 'https://techcrunch.com/'  # 替換成實際的科技新聞網站
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        news_titles = soup.find_all(class_='fi-main-block__title')  # 替換成實際的標題元素和類別
        
        
        # 提取新聞標題
        headlines = [title.text.strip() for title in news_titles]

        for headline in headlines:
            if headline:
                print(headline)
            else:
                print("Can't get news title.")
    else:
        print("訪問網站失敗")
#--------------------------我是分隔線------------------------------#
def crawl_tech_news2():
    url = 'https://www.wired.com/'  # 替換成實際的科技新聞網站
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        news_titles = soup.find_all('h2', class_='SummaryItemHedBase-hiFYpQ jmLbfd summary-item__hed')  # 替換成實際的標題元素和類別
        
        
        # 提取新聞標題
        headlines = [title.text.strip() for title in news_titles]

        for headline in headlines:
            if headline:
                print(headline)
            else:
                print("Can't get news title.")
    else:
        print("訪問網站失敗")

# 呼叫函數
crawl_tech_news1()
crawl_tech_news2()


# 在這裡添加整合 Lone Bot 和 Line Bot API 的程式碼

# 設定每天定時執行的任務，這裡使用 schedule
'''import schedule
import time

def job():
    tech_news = crawl_tech_news()
    
    if tech_news:
        # 在這裡添加將新聞發送到 Line Bot 的程式碼
        pass
    else:
        print("Failed to retrieve tech news.")

# 設定每天定時執行的時間
schedule.every().day.at("08:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)'''