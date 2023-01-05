# Ranking App

## About Ranking App

The data available on the web is one of the most important sources for data analysis and data mining. Such analyzes are carried out for various purposes, among which we can mention opinion analysis and sentiment analysis. One of the best ways for collecting data available on the web is “Web Scraping” and it is possible to do it using various tools and programming languages. Among programming languages that can be used for web scraping is Python that can be used with scrappy or beautifulsoup libraries,
People are often able to access this data in CSV or using an API, however, there are times when the programmer needs only a part of a web page, in situations like these, the programmer can use a method called “Web Scrapping” to collect data from a web page in a suitable format to work on. In this case, we used Python and the beautifulsoup library.
Ranking App is a program that we can use for extracting, transforming, and loading specific data on a document then we can ask people to vote for our sorted results, the app extracts the content from <https://www.billboard.com/> (The collected data is five top ranks of the billboard of four previous weeks) then transform the data that collected (removes duplicated names if exist then sorts the names by alphabet) and the app by using google API uploads the data onto a google sheet, then by app script framework in google sheet the app create the form on google form, then the user can share the form for collecting votes for top ranks after submitting votes the form will save the results on the google sheet and calculate the average of every month.

## Files

The app contains four main files, Extracting.py, Loading.py, Main.py, and Appscript.gs, which are introduced in the following:

## Extracting.py

It is the file that works on collecting content from <https://www.billboard.com/charts/artist-100/> by using beautifullsoup library, it extracts the name of five top rank artists of four previous weeks, as we can see in the code, first we find the top 100 artists of each week by using beautifulsoup and targeting an HTML tag, then we can find five top rank artists by targeting an HTML tag of the webpage, removing duplicate names, and sorting names according to the alphabet.
![showing the code for extracting](Picture1.png)

## Loading.py

The file helps us to create a spreadsheet using the Google Sheets API, save the extraction results on the spreadsheet, or modify them each time the app runs and should be updated, the code has been written with the help of the examples on <https://developers.google.com/sheets/api/quickstart/python>
In the code, there is a function named “loading” and it has an attribute that is “values” when the authorization process completes for the first time and it checks that for an existing  file named “token.json” If it didn't exist or didn’t valid, it follows a process to create, open and write the credentials to the token file, you can see the code part below:
![showing the code for Loading](Picture2.png)
and if it existed then it goes to the next step which is checking for spreadsheet ID for creating a spreadsheet or update it, as you can see below a part of the code:
![showing the code for Loading](Picture3.png)

## Main.py

This file is the main file that runs the app, in this file the code imports loading and extracting files, it gets the function named “extracting” results from the Extracting.py and gives the results into an array named “values” which is the attribute of the “loading” function to run the app, you can see below:
![showing the code for running the App](Picture4.png)

## appscript.gs

If you use Google applications such as Google Sheets or Google Docs, you can do things with Google Script that are never possible with similar desktop applications.
It is an application development platform that enables the integration of Google Cloud services. Google has provided many APIs for each of its cloud services. By writing Google apps, you can access a whole different world of additional features for each of these different Google services.
The file is named “appscripts.gs” is a code to use in the app script editor which is an extension of the google sheet.
It has three functions for creating a form on the google doc, making an edit and submitting, and finally calculating the average of votes that have been submitted, it creates a form that name is “Billboard” and then the user can vote for the artists that their names mentioned on the form, and then the votes will save on the spreadsheet and calculates the average of the votes.

## How to install

Here you can see how to set up and use the app.

### Steps

Setting up the app takes five steps, therefore please follow the steps below.

#### Step1

Go to <https://console.cloud.google.com>, and log in with your Google account, if you didn’t create a project on Google cloud before please choose your country from the list, read the Google platform terms of service and check the box if you agree, and then on the top of the page click on the Select a project, and then you need to click on the NEW PROJECT on the top right and create a project. Go to the link below:
<https://console.cloud.google.com/apis/enableflow?apiid=sheets.googleapis.com&project=plated-life-369600>
And then select your project from the top, then click on the Enable button.

#### Step2

Go to the link below:
<https://console.cloud.google.com/apis/credentials?project=plated-life-369600>
Click on Create credentials, select OAuth client ID, and select application type as a desktop app, and then click on the create, now you can see your credentials, you can download the json file by clicking on “Download json”, copy the downloaded into the working folder and rename it as “creds.json”.

#### Step3

If you didn’t install Google client library for Python, use the command below in your terminal:
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

#### Step4

Go to main.py and run it.

#### Step5

Go to <https://drive.google.com/drive/my-drive> as you can see a spreadsheet has created that is name as “Billboard ranking list”, double click on it, and now you can see the artist names have been printed on the sheet in order to the ranking, on the top menu click on Extensions and select the App Script.

#### Step6

Go to your working folder, and open the appscript.gs, copy the code and paste it into the app script editor that you have opened in the previous step, save it, and click to run.

#### Step7

When you run the app script code, first it needs to review permissions, click on it, choose your account, click on “Advanced” then click on “Go to Untitled project (unsafe)”, and finally click on allow.

#### Step8

(This is the final step)
Now go again to the <https://drive.google.com/drive/my-drive> and you can see you have a form named “Billboard”, open the form and put it in preview style. And vote for artists and submit the form, now you can go to your sheet and see the votes.

## Scheduling

Cron abbreviation of the words Command Run On is also known as UNIX Scheduler. cron is actually a system that automatically performs specified tasks for you at certain time intervals. Cron is a feature in the Linux operating system that schedules a command or script on your server to run automatically at a specified time and date.

### Scheduling steps

1. On an ubuntu open the terminal and type "crontab -e"
2. You need to select the editor, press 1 to select nano.
3. You need to enter five integers in the following order: minute, hour, day, month, year, for running the app once a month you have to enter "0 0 1 * * /path/.py" you see the picture below:
![Calculating crontab for runnig time](Picture5.png)
4. Save the file and exit.

