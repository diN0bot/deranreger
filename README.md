
## Goals

- Investigate technology new to me:
  - Google Closure Library, elastic search, cassandra
  - Create abstractions layers on top by scratch
- Make a cool system and app:
  1. Iterate on visualization
  1. Once using for real, iterate on data analysis.

## The App: Event Analyzer

What are the connections between what I do and how I feel?

I'd like an app that helps me answer this question. Some of the required features:

- Easy to record what I do and how I feel.
- Sensible visualizations.
- Interesting analysis.

## ToDo

[ ] Setup EC2 and elastic search
[ ] With Django, create a generic elasticsearch-proxy API for GCL iterations. 
[ ] Learn GCL like whoa and iterate on viz
[ ] Once viz stabilizes, set up elastic search for real backed by Cassandra

## Technology

### Google Closure Library 

Source code - http://code.google.com/p/closure-library/source/checkout

Intro to Google Closure Library 1hr presentation - http://www.youtube.com/watch?v=yp_9q3tgDnQ

### Amazon Services

Setting up Django with Gunicorn on an EC2 instance - http://adrian.org.ar/python/django-nginx-green-unicorn-in-an-ubuntu-11-10-ec2-instance  

### Elastic Search

Putting elastic search on Ec2 - http://www.elasticsearch.org/tutorials/2011/08/22/elasticsearch-on-ec2.html

For reference - https://github.com/aparo/django-elasticsearch

###

For reference - https://github.com/vaterlaus/django_cassandra_backend
