import time
import requests
from linebot import LineBotApi
from linebot.models import TextSendMessage, URIAction, ButtonsTemplate, MessageTemplateAction, TemplateSendMessage
from linebot.exceptions import LineBotApiError
from bs4 import BeautifulSoup

# 設定你的 Channel Access Token
line_bot_api = LineBotApi('IU9rIPMkgLuuNRN8W4SxB8IPLu4Ag4A0/fvRWwMIhzTlqGx9vyzX5CHWcledrqZ4tVCHVQsZWPdPxpHX+kQsnxHLjjl89qIQciIAmx6Z3vWXZWPbFOmESQPV+/YgxEYrWvw5KxP1/JBgECD2sWtChwdB04t89/1O/w1cDnyilFU=')

def send_to_line_bot(messages):
    try:
        # 設定你的 LINE BOT 的聊天室 ID
        chat_id = '2002180798'
        
        # 每次最多發送 5 條消息
        chunk_size = 5
        chunks = [messages[i:i + chunk_size] for i in range(0, len(messages), chunk_size)]

        for chunk in chunks:
            # 將消息轉換為合適的字典形式
            message_dict = chunk

            # 傳送訊息到 LINE BOT
            line_bot_api.broadcast(messages=message_dict)


    except LineBotApiError as e:
        print(e)

'''def crawl_tech_news1(url, css_selector):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        news_titles = soup.select(css_selector)

        # 提取新聞標題和連結
        news_list = [{"title": title.text.strip(), "url": title.a['href']} for title in news_titles if title.a]
        messages = []

        for news in news_list:
            title = news["title"]
            url = news["url"]
            print(news_list)

            if title and url:
                # 創建包含文字和網址的 TextSendMessage
                message = TextSendMessage(text=f"每日最新的科技新知來囉~\n\n{title}\n\n{url}")
                messages.append(message)
                send_to_line_bot(messages)

            else:
                print("Can't get news title or URL.")

        
    else:
        print(f"訪問網站 {url} 失敗")'''

def crawl_tech_news2(url, css_selector):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        news_titles = soup.select(css_selector)

        # 提取新聞標題和連結
        news_list = [{"title": title.text.strip(), "url": title.a['href']} for title in news_titles if title.a]
        messages = []

        for news in news_list:
            title2 = news["title"]
            url = news["url"]

            try:
                # 將標題轉換為 ASCII 字符串，忽略錯誤的方式處理非 ASCII 字符
                title2 = title2.encode('ascii', 'ignore').decode('utf-8')
            except Exception as e:
                print(f"Error converting title to ASCII: {e}")

            if title2 and url:
                # 創建包含文字和網址的 TextSendMessage
                message = TextSendMessage(text=f"每日最新的科技新知來囉~\n\n{title2}\n\n{url}")
                messages.append(message)
            else:
                print("Can't get news title or URL.")

        send_to_line_bot(messages)
    else:
        print(f"訪問網站 {url} 失敗")

# 呼叫函數，分別爬取兩個網站的標題
crawl_tech_news2('https://www.wired.com/', 'h2.SummaryItemHedBase-hiFYpQ.jmLbfd.summary-item__hed[data-testid="SummaryItemHed"]')
#crawl_tech_news1('https://techcrunch.com/', '.fi-main-block__title')


