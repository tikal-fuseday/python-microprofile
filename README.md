# python-microprofile
Implement microprofile for python language

## overview
So what are microframeworks
------
So what are microframeworks? Usually, they are a bare framework for a rest server, according to Wikipedia: minimalistic web application frameworks. Each one has its own flavor: some have a reactive patterns for defining endpoints, some added integrated metrics.
Microservice Architecture has become very common in most companies. The big question is of course what is a microservice. 
From the site microservices.io, this is the summary:
 * Microservices - also known as the microservice architecture - is an architectural style that structures an application as a collection of services that are
 * Highly maintainable and testable
 * Loosely coupled
 * Independently deployable
 * Organized around business capabilities
 * Owned by a small team

The main issue is that up till now, all the discussions of microservices were about the size and the independence of the service (deployment and development). 
What was not covered well is the minimum requirement of the service for monitoring and orchestration. Kubernetis gave to docker a standard way of distributed deployment and scale. 
A similar framework for viewing all services via a single lense was missing.

![](https://chaimturkel.files.wordpress.com/2019/12/screen-shot-2019-11-12-at-13.06.41.png?w=816&h=314&zoom=2)

## goal
In this project we try to collect into one place the best practices and implementations of microprofiles for python.
You can see in each spec what we have found to be the best packages that come closest to the microprofile standard.
In cases that there is nothing we try to implement them ourselfs.

## setup env

[How to install python3 on OSX](https://gist.github.com/alfasin/bc88d4eb0217f13cbc7ccef53e8eadb3)

### setup env

```buildoutcfg
python3 -m pip install --user --upgrade pip
python3 -m pip --version # (test install)
python3 -m pip install --user virtualenv
python3 -m venv env
source env/bin/activate
which python # (test env)
```
