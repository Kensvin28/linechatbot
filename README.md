This is a project I made to help my community get a daily devotion everyday.
If there are any questions regarding LINE API, feel free to contact me at Instagram: [@kens.vin](https://instagram.com/kens.vin) 😊.

[Explanation about the web scraping technique in this project](https://medium.com/@kevinma28/daily-devotion-web-scraping-using-python-f6d6431af167)

[Quick reference for Line Chatbot](https://youtube.com/watch?v=TzZM1BtGPtM)

[Line Developers](https://developers.line.biz)

[Messaging API reference](https://developers.line.biz/en/reference/messaging-api)

[Line API Documentation for Python](https://github.com/line/line-bot-sdk-python)

# Steps to launch your LINE chatbot:

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
### 5. Create your own bot or use a template
You can clone this repository, get a simple [Python bot template](https://github.com/abhishtagatya/pyline-bot) from Abhista Gatya, or use your own code.

If you're still new to Github, you can find out how to clone a Github repository [here](https://www.howtogeek.com/451360/how-to-clone-a-github-repository/).

### 6. Obtain your channel secret and channel access token
Select a Messaging API channel from the Channels in the LINE Developers Console and issue the channel secret from the basic settings tab.
![Channel Secret](https://user-images.githubusercontent.com/63847755/154473468-619d885b-7f76-4b30-8d59-d5b0b3315424.png)
Select the Messaging API tab and issue a long-lived channel access token.
![Channel Access](https://user-images.githubusercontent.com/63847755/154473486-3a3b6655-e9a3-46fb-8660-97102cd0e9a9.png)

### 7. Put your channel secret and channel access token into your app
Copy them from the LINE Developers Console and paste them in the designated variables.
![image](https://user-images.githubusercontent.com/63847755/154639992-973a2ee2-5881-408c-a874-a9f1f268e89c.png)

## Deploy app to a server
You can use Heroku to deploy the app because it lets us to host our app for free up to 550 dyno hours per month.

### 8. Create a Heroku Account and Download the Heroku CLI
Create a free Heroku account [here](https://signup.heroku.com/)
![image](https://user-images.githubusercontent.com/63847755/154642750-50a4c374-02d2-40cf-b085-9226a298651f.png)

Download the Heroku CLI and follow the installation instructions [here](https://devcenter.heroku.com/articles/heroku-cli)
More CLI reference: [Heroku Command Line](https://devcenter.heroku.com/categories/command-line)

### 9. [Deploy your app to Heroku](https://devcenter.heroku.com/articles/getting-started-with-python?singlepage=true)
Login to your account in Heroku CLI using your terminal (Windows Terminal/Command Prompt/Terminal)
```
heroku login
```
Move to the directory where you cloned/downloaded your app in the CLI using the ```cd``` command and create the app using this code
```
cd .\Downloads\linechatbot
git commit -a -m "Any message"
heroku create [YOUR-APP-NAME]
git push heroku master
```

### 10. Configure the Webhook
Once the deploy is successful, open up your Heroku dashboard in your web browser and click 'Open app'.
![image](https://user-images.githubusercontent.com/63847755/154648974-8cb2030f-fe37-46d6-8296-8f929dec77a3.png)

Don't worry if the page looks like this:
![image](https://user-images.githubusercontent.com/63847755/154650926-31ce2fff-5396-4957-b558-5cc0f446aef3.png)

Add ```callback``` to the end of the URL so that it will look like this: ```https://yourbotname.herokuapp.com/callback``` and copy the URL.

Open your LINE Developers Console, select the Messaging API tab and click Edit under Webhook URL, paste the URL, and then click Update. Additionally, enable Use webhook.

![image](https://user-images.githubusercontent.com/63847755/154474387-5763e035-9457-4ce7-b881-f354df5cdb16.png)

### 11. Add your LINE bot as a new friend by using the QR code
Add the LINE Official Account associated with the channel for your bot as a friend on LINE. To do so, scan the QR code on the Messaging API tab in the LINE Developers Console.
![image](https://user-images.githubusercontent.com/63847755/154650320-2234b961-4beb-4c43-a082-c7413785f979.png)

### 12. [Register your app in Kaffeine](http://kaffeine.herokuapp.com/) (Optional)
Kaffeine lets our app which is hosted in Heroku to become active up to 18 hours a day by pinging them every 30 minutes.
You can set your app's active time according to your preference. By using their service, the deployed bot in Heroku can send automated messages at a certain time daily.
![image](https://user-images.githubusercontent.com/63847755/154643001-1ec5f65c-87e3-4c74-9f11-b725e58edefa.png)
