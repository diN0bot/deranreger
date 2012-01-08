Demo
----

- Website: http://ec2-107-20-75-182.compute-1.amazonaws.com
- API: http://ec2-107-20-75-182.compute-1.amazonaws.com/a/data

Development Setup
-----------------

**Install dependencies: Django, pyes**

```bash
#install Python Package Installer
sudo apt-get install python-pip
#upgrade PIP itself
sudo pip install pip --upgrade
#installing Django
pip install django
#installing pyes
git clone https://github.com/aparo/pyes.git
cd pyes
python setup.py build
sudo python setup.py install
```

**Get code and run development web server**

```bash
git clone git@github.com:diN0bot/deranreger.git
cd deranreger
#python manage.py syncdb
python manage.py runserver
```

Visit `127.0.0.1:8000` and `127.0.0.1:8000/a/data` in a browser.


Goals
-----

- Investigate technology new to me:
  - Google Closure Library, elastic search, cassandra
  - Create abstractions layers on top by scratch
- Make a cool system and app:
  1. Iterate on visualization
  1. Once using for real, iterate on data analysis.


The App: Event Analyzer
-----------------------

What are the connections between what I do and how I feel?

I'd like an app that helps me answer this question. Some of the required features:

- Easy to record what I do and how I feel.
  - I liked inputting on a calendar view rather than forms, eg https://github.com/diN0bot/iCal-Analyzer
- Sensible visualizations.
  - Calendar view
  - [Beeminder charts](https://www.beeminder.com)
  - [Boolean charts](http://idonethis.com/)
- Interesting analysis.
  - Reminders
  - Randomness v correlations

ToDo
----

- [X] Setup EC2 and elastic search
- [\] Learn GCL like whoa and iterate on viz
- [\] With Django, create a generic elasticsearch-proxy API for GCL iterations. 
- [ ] Once viz stabilizes, set up elastic search for real backed by Cassandra


Technology
----------

**Google Closure Library**

Source code - http://code.google.com/p/closure-library/source/checkout

http://code.google.com/p/closure-library/wiki/IntroToComponents

http://code.google.com/intl/de-DE/closure/library/docs/overview.html

(not so good) Intro to Google Closure Library 1hr presentation - http://www.youtube.com/watch?v=yp_9q3tgDnQ

**Amazon Services**

Setting up Django with Gunicorn on an EC2 instance - http://adrian.org.ar/python/django-nginx-green-unicorn-in-an-ubuntu-11-10-ec2-instance  

**Elastic Search**

Putting elastic search on Ec2 - http://www.elasticsearch.org/tutorials/2011/08/22/elasticsearch-on-ec2.html

For reference - https://github.com/aparo/django-elasticsearch

Dev console - http://mobz.github.com/elasticsearch-head

**Cassandra**

For reference - https://github.com/vaterlaus/django_cassandra_backend

**Orthogonal Tools**

These don't have quite the same data goals or displays, but some data does fit more naturally into these tools---eg, recurring events---so think on this kind of extensibility.

- https://www.beeminder.com/meta/blog
- http://idonethis.com/
- http://www.joesgoals.com/
- http://daytum.com/
- http://itunes.apple.com/us/app/dayta/id354915346?mt=8
- http://your.flowingdata.com/
