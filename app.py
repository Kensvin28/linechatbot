# Flask
import os
from flask import Flask, request, abort

# Line Bot
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
from linebot.exceptions import LineBotApiError

from requests.api import get

# Web Scraping
from bs4 import BeautifulSoup
from datetime import *
import requests
import re

# Automation
import time
import threading

# Content Web Scraping


def getDate():
    today = date.today()
    formattedDate = today.strftime("%Y/%m/%d/")
    return formattedDate


def getURL(date):
    tempURL = "https://www.sabda.org/publikasi/e-sh/"
    pageURL = tempURL + date
    return pageURL


def getContent(pageURL):
    # Initialise requests and BeautifulSoup
    page = requests.get(pageURL)
    soup = BeautifulSoup(page.content, 'html.parser')
    # Get Chapter and Title
    for element in soup.select('h1'):
        chapter = element.find('center').text
        title = element.contents[0].contents[1]
    # Get content
    searchTag = soup.find_all('aside', attrs={"class": "w"})
    # Add break
    for string in searchTag[1].find_all("p"):
        string.append("\n")
    # Convert to text
    rawDevotionList = searchTag[1].text
    # Clean content
    regex1 = re.sub(r'(\d\. )', r'\n\1', rawDevotionList)
    regex2 = re.compile(
        '(\nMari memberkati para hamba Tuhan dan narapidana.*?Yay Pancar Pijar Alkitab.)')
    cleanDevotionText = re.sub(regex2, "", regex1)
    resultString = "Santapan Harian\n" + chapter + \
        "\n" + title + "\n" + cleanDevotionText
    return resultString


def renungan():
    date = getDate()
    URL = getURL(date)
    result = getContent(URL)
    return result


lastDate = 0


def checkDate(dateToday):
    global lastDate
    if dateToday != lastDate:
        lastDate = dateToday
        return True
    return False

def checkDate2(dateToday, idFile):
    lastDate = idFile[0].strip()
    if dateToday != lastDate:
        return True
    return False

# App
app = Flask(__name__)

# Channel Access Token (From Line Developer)
line_bot_api = LineBotApi(
    'PUT YOUR OWN ACCESS TOKEN HERE')
# Channel Secret (From Line Developer)
handler = WebhookHandler('PUT YOUR OWN SECRET TOKEN HERE')

# Callback Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# Message Handler
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text = event.message.text
    try:
      id = event.source.user_id
      group_id = event.source.group_id
    except:
      id = event.source.user_id

    wholeMessage = text
    text = text.split(" ")
    text = [element.lower() for element in text]

    try:
        if "@axel" in text:
            if "renungan" in text:
                if checkDate(getDate()) == True:
                    renunganHarian = renungan()
                    line_bot_api.reply_message(
                        event.reply_token, TextSendMessage(text=renunganHarian))
                elif checkDate(getDate()) == False:
                    line_bot_api.reply_message(event.reply_token, TextSendMessage(
                        text="Renungan hari ini sudah dikirim. Silakan cek kembali."))
        elif "/restart" in text:
            global lastDate
            lastDate = 0
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text="Berhasil disetel ulang."))
        elif "/renungan" in text:
            if checkDate(getDate()) == True:
                renunganHarian = renungan()
                line_bot_api.reply_message(
                    event.reply_token, TextSendMessage(text=renunganHarian))
            elif checkDate(getDate()) == False:
                line_bot_api.reply_message(event.reply_token, TextSendMessage(
                    text="Renungan hari ini sudah dikirim. Silakan cek kembali."))
        elif "renungan" in text:
            if "harian" in text:
                try:
                    # Add to subscription file
                    flag = 0
                    with open("id.txt", "r") as f:
                        idFile = f.readlines()
                        for line in idFile:
                            if line[-1] == '\n':
                                idToMatch = line[:-1]
                            if id == idToMatch:
                                flag += 1

                    if flag == 0:
                        with open("id.txt", "a") as f:
                            f.write(id + "\n")
                        line_bot_api.reply_message(event.reply_token, TextSendMessage(
                            text="Renungan harian otomatis berhasil diaktifkan."))
                    else:
                        line_bot_api.reply_message(event.reply_token, TextSendMessage(
                            text="Renungan harian otomatis sudah diaktifkan."))
                except LineBotApiError as e:
                    line_bot_api.reply_message(
                        event.reply_token, TextSendMessage(text=e))
        elif "jangan" in text:
            if "kirim" in text:
                try:
                    deleteIdFromFile(id)
                    line_bot_api.reply_message(event.reply_token, TextSendMessage(
                        text="Renungan harian otomatis berhasil dinonaktifkan."))
                except LineBotApiError as e:
                    line_bot_api.reply_message(
                        event.reply_token, TextSendMessage(text=e))
        elif "group" in text:
            if "id" in text:
                message = TextSendMessage(text="Group ID: " + group_id)
                line_bot_api.reply_message(event.reply_token, message)
        elif "/kirim" in text:
            regex1 = wholeMessage
            regex2 = "/kirim "
            realMessage = re.sub(regex2, "", regex1)
            message = TextSendMessage(text=realMessage)
            line_bot_api.push_message("PUT YOUR ID HERE", message)

    except LineBotApiError as e:
        # error
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=e))

#Thread Runner
@app.before_first_request
def runThread():
    event_obj = threading.Event()
    thread1 = threading.Thread(target=time_check, args=(event_obj,))
    thread1.start()

#Renungan Harian Automation
def time_check(event):
    while not event.is_set():
        sendTime = 7
        sendMinute = 0
        sleepDuration = 60*60*24
        date_time = datetime.now(timezone(timedelta(hours=7)))
        count = 0
        if date_time.hour == sendTime and date_time.minute == sendMinute:
            with open("id.txt", "r") as f:
                idFile = f.readlines()

            if(checkDate2(getDate(), idFile) == True):
                idFile[0] = getDate() + "\n"
                with open("id.txt", "w") as f:
                    f.writelines(idFile)
                result = renungan()
                idList = getId()
                for id in range(1, len(idList)):
                    line_bot_api.push_message(idList[id], TextSendMessage(text=result))
            time.sleep(sleepDuration)
        elif count == 0:
            firstSleep = 60 - date_time.minute
            time.sleep(firstSleep*60)
            count += 1
        else:
            time.sleep(60*60)

def getId():
    idList = []
    with open("id.txt", "r") as f:
        idFile = f.readlines()
        for id in idFile:
            id = id.strip()
            idList.append(id)
    return idList


def deleteIdFromFile(id):
    try:
        with open("id.txt", "r") as f:
            idFile = f.readlines()
            for line in idFile:
                if line[-1] == '\n':
                    idToMatch = line[:-1]
                if id == idToMatch:
                    idFile.remove(line)
                    newFile = idFile

        with open("id.txt", "w") as f:
            for id in newFile:
                f.write(id)
    except IOError as e:
        print(e)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)