# Emotional_Health_Expert

## Emotional Health Chatbot: Project Report

### Submitted in partial fulfilment of EBA5004 Practical Language Processing: Practice Project

### Team 5: Members
        - Ankeit Taksh           - Shivangi Verma
        - Prashant Chaudhary     - Anirban kar Chaudhari

## Youtube Link (Merged Videos for Business & System Architecture / Demos)
   - https://www.youtube.com/watch?v=2iqxXFh1QL4

## USER DEPLOYMENT GUIDE (refer to attached user deployment guide doc for screenshots guide)
### 1.	Hardware
a.	OS : Ubuntu Linux 18/20 or Centos 7/8 
b.	GPU : Nvidia graphics card with CUDA drivers
c.	Physical Server: Physical machine with GPU nvidia RTX 2000+ series
d.	Cloud VM: AWS G3 instances or Azure NCasT4_v3-series or higher
e.	Microphone for ASR

### 2.	Software :
a.	Python Version: 3.2 or higher
b.	Stream Lit 
c.	Keras , TensorFlow
d.	NLTK 
e.	Firefox
f.	VS code as needed
3.	Environment Setup for account access:
a.	Telegram Id
b.	Twitter dev account
c.	Reddit dev account 
d.	ASR handling 

### 4.	Project setup steps: 
a.	Enter command git clone https://github.com/PLPWork/Emotinal_Health_expert to download the entire code.
b.	Run the main file
c.	 Find the requirements.txt file and run the command ‘pip install -r requirements.txt’ to install all the packages that are required.

The implementation uses Tweepy and ngrok ,which require authentication tokens.The following steps explain how to get them
d.	Step 1: Apply for a Twitter Developer Account
e.	Step 2: Create an Application in TWITTER dev account
f.	Step 3: Create the Authentication Credentials
g.	Step 4: Setting up NGROK auth key token
h.	Step5: Thought analysis Pipeline
i.	Step 6: Deploy Emotional Health Expert Chatbot
j.	Step 7: Initiate Chat



 
### Step 5: Thought analysis Pipeline
1.	Clone Github
https://github.com/PLPWork/Sem4PLPPrj


Tweepy API Authentication credentials
We need to create the required authentication credentials to be able to to use the API
These credentials are four string :-
A.	1.Consumer key
B.	2.Consumer secret
C.	3.Access token
D.	4.Access secret
### Step 1: Apply for a Twitter Developer Account( for Tweepy tokens)

Go to the Twitter developer site to apply for a developer account. Here, you have to select the Twitter user responsible for this account. It should probably be you or your organization. Here’s what this page looks like:
 

Twitter then requests some information about how you plan to use the developer account, as showed below:

 
You have to specify the developer account name and whether you are planning to use it for personal purpose or for your organization.

### Step 2: Create an Application in TWITTER dev account
Twitter grants authentication credentials to apps, not accounts. An app can be any tool or bot that uses the Twitter API. So you need to register your an app to be able to make API calls.
To register your app, go to your Twitter apps page and select the Create an app option.
You need to provide the following information about your app and its purpose:
•	App name: a name to identify your application (such as examplebot)
•	Application description: the purpose of your application (such as An example bot for a Real Python article)
•	Your or your application’s website URL: required, but can be your personal site’s URL since bots don’t need a URL to work
•	Use of the app: how users will use your app (such as This app is a bot that will automatically respond to users)

### Step 3: Create the Authentication Credentials
•	To create the authentication credentials, go to your Twitter apps page. Here’s what the Apps page looks like:
•	 
•	Here you’ll find the Details button of your app. Clicking this button takes you to the next page, where you can generate the credentials.
•	By selecting the Keys and tokens tab, you can generate and copy the key, token, and secrets to use them in your code:


 

### Step 4: Setting up NGROK auth key token
o	.Go to ngrok https://dashboard.ngrok.com/get-started/setup
o	Login ,and get auth token
 

Copy this token and use it in Thought analysis pipeline
!ngrok authtoken <20thSMTKjBAdvRVmIPJ56Vc3Skj_6B3CoRe2da7YXe8SGUAc6>
!nohup streamlit run app.py --server.port 80 &
url = ngrok.connect(port=80)

The obtained url can then be used to launch the though analysis streamlit app

### Step 6: Deploy Emotional Health Expert Chatbot

	Now from github repo main folder
	Install all the requirements from environment file.
	And run the master.py file 
<add screenshot>
-	This will act as a server for EmotinalHealthExpert_bot.

### Step 7: Initiate Chat
-	In telegram please search for ,EmotionalHealthExpert_bot
-	You can start the conversation by using /start




