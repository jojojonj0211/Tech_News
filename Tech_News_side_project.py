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
        
        # 將消息轉換為合適的字典形式
        message_dict = messages

        # 傳送訊息到 LINE BOT
        line_bot_api.broadcast(messages=message_dict)
    except LineBotApiError as e:
        print(e)

def crawl_tech_news(url, css_selector):
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        news_titles = soup.select(css_selector)
        
        # 提取新聞標題和連結
        #news_list = [{"title": title.text.strip(), "url": title.a['href']} for title in news_titles if title.a]
        headlines = [title.text.strip() for title in news_titles]

        for headline in headlines:
            if headline:
                # 將每條新聞標題單獨發送到 LINE BOT
                send_to_line_bot([TextSendMessage(text=headline)])
            else:
                print("Can't get news title.")
    else:
        print(f"訪問網站 {url} 失敗")

# 呼叫函數，分別爬取兩個網站的標題
crawl_tech_news('https://techcrunch.com/', '.fi-main-block__title')
crawl_tech_news('https://www.wired.com/', 'h2.SummaryItemHedBase-hiFYpQ.jmLbfd.summary-item__hed')

