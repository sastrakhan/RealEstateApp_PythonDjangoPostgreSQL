
# Overview
A realestate client needed an application to list his available properties and allow prospects to inquire about them.  
There needed to be an admin interface to run CRUD operations on home listings and a user registration system.  We leveraged the out of the box Django admin interface with additional Django libraries.  We used PostgreSQL for the data layer.  

In the end we ended up using a WordPress theme to limit developer invovlement for ongoing maintainence.  I have removed any sensitive client data hence some of the text contains lorum ipsum.  


## Initialization:
In Root
```
source venv/bin/activate
pip install django
python3 manage.py runserver
```