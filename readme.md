# Stocks App

This is a Django app that provides stock information on the companies listed in the S&P500. You can sort tickers by most gains/losses over various time periods. 

This app uses the IEX Cloud API to fill in the varying stock information. However, the key I'm using is for the sandbox mode, so the numbers are not accurate to real market prices!

This django project was inspired by this youtube video: https://www.youtube.com/watch?reload=9&v=xfzGZB4HhEE

## Getting Started

This app was written with Django 3.1.2. Additional plugins/requirements are in requirements.txt.

I recommend using python's **virtualenv** tool if building locally:

> $ mkvirtualenv *django_env*
> $ python manage.py runserver

Then visit http://localhost:8000 in your web browser to view the app. 

### Settings

This app has two different settings; one for development and one for production. They're found in <em>stock_django/settings</em>. If you're developing, you'll have to edit <em>manage.py</em> and <em>stock_django/wsgi.py</em> accordingly to use the correct settings.py (either dev_settings.py or production_settings.py):

> <em>For Example: </em>os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stock_django.settings.production_settings')

If developing, you'll need to create a **private_settings.py** file in the main directory. In it, you'll need to list your own API key (CLOUD_API_KEY) and secret key (SECRET_KEY). 

If in production, you can assign the API key and secret key to environmental variables. (ex. os.environ['SECRET_KEY'])

## Screenshots

![ss1](/screenshots/1.png?raw=true)
![ss2](/screenshots/2.png?raw=true)