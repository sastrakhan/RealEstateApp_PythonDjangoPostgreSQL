
# Overview
A realestate client needed an application to list his available properties and allow prospects to inquire about them.  
There needed to be an admin interface to allow realtors to create user accounts.  We leveraged  the out of the box Django admin 
interface and standard CRUD operations to create the POC and used PostgreSQL for the data layer.  

In the end we ended up using a WordPress theme to limit developer invovlement for ongoing maintainence.  I thoroughly enjoyed learning about Django from this project and followed a SafariBooksOnline [course](https://learning.oreilly.com/videos/python-django-dev) for the initial 
boilerplate.   


## Initialization:
In Root
```
source venv/bin/activate
pip install django
python3 manage.py runserver
```