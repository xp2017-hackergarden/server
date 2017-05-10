xp2017 Hackergarden / Server
==
Join the team
-
Paragraph about joining the hackergarden team

Setup working environment
-
* Clone xp2017 Hackergarden server project
```
$ git clone git@github.com:xp2017-hackergarden/server.git
```
* [Install virtual environment](https://virtualenv.pypa.io/en/stable/installation/) so you would be able to run project locally.
* Create virtual environment for project
```
$ virtualenv --python=python3 venv
```

* Activate virtual environment and navigate to project root folder
```
$ . venv/bin/activate
$ cd server
```
* Export django secret key to environment
```
$ export DJANGO_SECRET_KEY=whatever
```
* Install requirements
```
$ pip install -r requirements.txt
```
* Start migrations
```
$ python manage.py migrate
```

Run tests
-
* Run tests from project root folder using pytest
```
$ py.test
```

Run application
-

* run server locally
```
$ python manage.py runserver
```

### That's it - you are ready to roll