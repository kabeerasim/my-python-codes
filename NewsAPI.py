# Akhbaar parh ke sunao

import requests
import json

Api_Key = "ee13c25407284ff28dbca11c03fd13fb"
def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == '__main__':
    speak("News for today")
    url = ('https://newsapi.org/v2/top-headlines?country=in&apiKey='+Api_Key)
    news = requests.get(url).text
    news = json.loads(news)
    articles = news["articles"]
    for arts in articles:
        speak(arts['title'])
        speak("Moving on to the next news..")