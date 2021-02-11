# Stocks App

This is a Django app that provides stock information on the companies listed in the S&P500. You can sort tickers by most gains/losses over various time periods. 

This app uses the IEX Cloud API to fill in the varying stock information. However, the key I'm using is for the sandbox mode, so the numbers are not accurate to real market prices!

This django project was inspired by this youtube video: https://www.youtube.com/watch?reload=9&v=xfzGZB4HhEE

## Getting Started

This app was written with Django 3.1.2. 

First, you'll need to create a **private_settings.py** file in the main directory. In it, you'll need to input the API key, otherwise the app won't work. 

Second, it's recommended to use python's **virtualenv** tool if building locally:

> $ mkvirtualenv *django_env*
> $ python manage.py runserver

Then visit http://localhost:8000 in your web browser to view the app. 

## Screenshots

![ss1](/screenshots/1.png?raw=true)
![ss2](/screenshots/2.png?raw=true)