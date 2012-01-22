Demo
----

- Website: http://ec2-107-20-75-182.compute-1.amazonaws.com
- API: http://ec2-107-20-75-182.compute-1.amazonaws.com/a/data

Development Setup
-----------------

**Get code**

```
git checkout git@github.com:diN0bot/deranreger.git
```

**Install dependencies: node.js, express, socket.io, jade, google closure library**

#Install Google Closure Library
```
svn checkout http://closure-library.googlecode.com/svn/trunk/ closure-library
ln -s closure-library deranreger/webapp/static/js/closure-library
```

#Install node.js
```
open https://sites.google.com/site/nodejsmacosx/
```

#Install socket.io, express, jade
```
npm install socket.io express jade
```

**Get code and run development web server**

```
git clone git@github.com:diN0bot/deranreger.git
cd deranreger/webapp
node app.js
```

Visit `http://localhost:3000/demos` in a browser.


Goals
-----

- Investigate technology new to me:
  - Google Closure Library, elastic search, socket.io, node.js, cassandra
- Make a useful app:
  1. Iterate on visualization
  1. Iterate on data analysis.


The App: Event Analyzer
-----------------------

What are the connections between what I do and how I feel?

I'd like an app that helps me answer this question. Some of the required features:

- Easy to record what I do and how I feel.
- Sensible visualizations.
- Interesting analysis.


Technology
----------

**Google Closure Library**

Source code - http://code.google.com/p/closure-library/source/checkout

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


**Ql.io**

http://ql.io/docs/build-an-app

**Hook.io**

https://github.com/hookio/hook.io