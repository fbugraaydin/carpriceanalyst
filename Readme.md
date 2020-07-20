## Car Price Analyst
Car Price Analyst provides you the analysis of the car market according to your criteria.

I developed project because loving and following cars.
People says that The most powerful therapy of man is that browsing on the car selling sites :)

Just click to look at: http://car-price-analyst.herokuapp.com/

## Tech / Framework
- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Selenium](https://selenium-python.readthedocs.io/)
- [Bootstrap](https://getbootstrap.com/)
- [SQLite](https://www.sqlite.org/index.html)
- [APScheduler](https://apscheduler.readthedocs.io/en/stable/)

## Features

Project supports FromOwnerDotCom & MyCarDotCom.

When you enter the Car Price Analyst from 2 web site(fromownerdotcom & mycardotcom). You have 2 functionality:
- Analyze: You enter car search link & select how many pages do you want to analyze.
- History: Lists search links that analyzed until now. When you select can see its history.

Your criteria link that you analyzed runs on every morning. Thus, you can follow changes from past to present day by day.

## Prerequisites

- Must install required libraries:

```bash
pip install -r requirements.txt
```

- Selenium & Requests are used to get web page source. Default is Requests. (util.py -> crawler()) <br/>
If want to use selenium, you must download chrome or firefox driver as your os and move to **driver** folder.<br/>

## Deployment

Project deployed to heroku.(https://car-price-analyst.herokuapp.com/). You can follow steps : [Deploying Python and Django Apps on Heroku](https://devcenter.heroku.com/articles/deploying-python)

When project deployed to heroku, scheduler worked just once. Because heroku doesn't trigger APScheduler in Django.<br/>
When you want to define pure scheduler in heroku you must define clock in Procfile. You can read [Scheduled Jobs with APScheduler](https://devcenter.heroku.com/articles/clock-processes-python#apscheduler) <br/>

But our scheduler belongs to Django and needs objects in project. <br/>
Because of that it defined custom command (**schedule_analyzer**) to provide scheduling job by Heroku.<br/>

**Heroku Scheduler** add-on added to heroku project and triggers custom command on every morning. Heroku scheduler job command:

```bash
$ python manage.py schedule_analyzer
```

## Coding Standards

PEP 8 -- Style Guide for Python Code

## Screenshots

- Analyze
![Analyze](screenshots/screen1.png?raw=true)
<br/>
- History
![History](screenshots/screen2.png?raw=true)


## Licence

This project was developed as a hobby. It has no commercial purpose.

Developed by © [Fuat Buğra AYDIN](https://www.linkedin.com/in/fuatbugraaydin/)