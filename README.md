This is a project I made to help my community get a daily devotion everyday.
If there are any questions regarding LINE API, feel free to contact me 😊.

[Quick reference for Line Chatbot](youtube.com/watch?v=TzZM1BtGPtM)

[Line Developers](developers.line.biz)

[Messaging API reference](developers.line.biz/en/reference/messaging-api)

[Line API Documentation for Python](https://github.com/line/line-bot-sdk-python)

#Steps to launch your LINE chatbot:

### 1. [Create a LINE developer account](https://developers.line.biz/en/docs/line-developers-console/login-account/#register-as-developer)
![image](https://user-images.githubusercontent.com/63847755/154469496-14795cd8-26e1-4fa5-9f20-2fcd74d4440b.png)

### 2. [Log in to LINE Developers Console](https://developers.line.biz/console/)
![image](https://user-images.githubusercontent.com/63847755/154469652-f8485d1c-5467-4914-8b23-7d53c09ee5a1.png)

## [Getting started](https://developers.line.biz/en/docs/messaging-api/getting-started/)
### 3. Create a new provider: 
![image](https://user-images.githubusercontent.com/63847755/154469893-0132ba7a-6ac0-46d3-9c33-26e9f82ffab0.png)
![image](https://user-images.githubusercontent.com/63847755/154470062-d3e5214a-ab32-40c7-a0c0-801efd961260.png)

### 4. Create a channel
In the Channels tab of the provider page you created, click Create a Messaging API channel.
![image](https://user-images.githubusercontent.com/63847755/154470116-83baf40b-9cf2-4c71-8c63-d70e6da6d227.png)
Enter the required information for your channel. "LINE" or a similar string can't be included in the channel name.
![image](https://user-images.githubusercontent.com/63847755/154470493-03a15d8d-b65b-4c25-b885-181193948e3d.png)

## [Set up bot](https://developers.line.biz/en/docs/messaging-api/building-bot/#set-up-bot-on-line-developers-console)
### 5. Obtain your channel secret and channel access token
Select a Messaging API channel from the Channels in the LINE Developers Console and issue the channel secret from the basic settings tab.
![Channel Secret](https://user-images.githubusercontent.com/63847755/154473468-619d885b-7f76-4b30-8d59-d5b0b3315424.png)
Select the Messaging API tab and issue a long-lived channel access token.
![Channel Access](https://user-images.githubusercontent.com/63847755/154473486-3a3b6655-e9a3-46fb-8660-97102cd0e9a9.png)

### 6. Configure the Webhook
Select the Messaging API tab and click Edit under Webhook URL, enter the Webhook URL (your bot's server or Heroku app address e.g. https://yourbotname.herokuapp.com/callback), and then click Update. Enable Use webhook.
![image](https://user-images.githubusercontent.com/63847755/154474387-5763e035-9457-4ce7-b881-f354df5cdb16.png)

### 7. Add your LINE bot as a new friend by using the QR code
Add the LINE Official Account associated with the channel for your bot as a friend on LINE. To do so, scan the QR code on the Messaging API tab in the LINE Developers Console.
