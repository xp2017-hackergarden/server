# XP 2017 Hackergarden server

[codecentric Digitization Labs](https://www.codecentric.de/dl) are hosting a Hackergarden at the [XP 2017](https://www.xp2017.org) conference in Cologne.
This is the GitHub repository for the server developed during the conference.

You are invited to join the team and hack away at the web app / backend or the [mobile app](https://github.com/xp2017-hackergarden/app).
We're located in the foyer of the conference venue.

In the following paragraphs, you should find all relevant information. If you don't have your own development machine with you, that's fine, too.
You can pair with one of us or just watch.

If you aren't a coder and still want to participate, feel free to practice your coaching skills on us or just put your feature ideas into the [inbox](https://trello.com/b/Etep7zB1/xp-2017-hackergarden).

# How to join

## Joining the Hackergarden team
* in order to join our github team please provide your github username to members of the team
* after that you'll be added to hackergarden github organisation and you will get access to the app repository
* in order to work on python/django part of the app you should clone following project - https://github.com/xp2017-hackergarden/server

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

## Starting to work on a feature
To start working on a feature checkout our [inbox on Trello](https://trello.com/b/Etep7zB1/xp-2017-hackergarden) for
feature ideas.
If you found an interesting one:

1. Decide if you want to pair up on it.
2. Pull it into *Development*.
3. Create a feature branch or introduce a feature toggle if you want to work from trunk.
4. Hack away at it.
5. Once you feel like it's finished, merge with or push to `develop`, which will trigger the CD pipeline and result in a
new release
if everything goes well.
6. Pull your card into *Done* or *Verification* (if you want to do the whole feedback cycle and talk to people about
whether the feature solves their problem).

If you don't pair when developing a new feature, you should probably ask for some kind of review.


## Triggering deployments
We have a continuous delivery pipeline set up that will automatically trigger new deployments whenever a
commit on `master` is detected.

Please **do not** push to master manually. [CircleCI](https://circleci.com/) is going to
do that for you whenever`develop` has successfully been build. That way, we won't waste time building the app on
[BuddyBuild](https://www.buddybuild.com/) when tests are still failing.

BuddyBuild is set up to automatically deploy each release to the alpha test group. Please note that it can take a while
for your release to actually show up as Play Store update.

People can join the test group by joining the
[XP 2017 Hackergarden Google+](https://plus.google.com/communities/113114317075009069296) community and activating the
app by opening the [activation link](https://play.google.com/apps/testing/com.xpapp).

# Important resources

## Web
* [Web app](https://app.xp2017.org)

## Services
* [CircleCI dashboard](https://circleci.com/gh/xp2017-hackergarden/server)

## Documentation
* [codecentric labs zero Team page](https://codecentric-labs-zero.github.io/)

### That's it - you are ready to roll