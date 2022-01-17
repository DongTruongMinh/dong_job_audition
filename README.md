# Code Structure

A simple web page using Django framework to create template and server side.
> Django with Model-View-Template(MVT) design pattern:
`Model:` src/service/models.py
`View:` src/service/views.py
`Template:` src/service/template

`Database:` src/db.sqlite3

# Installation

> ```pip install Django```

In src/ folder run:
> ```python manage.py runserver```


# CURL commands to test and verify API endpoints
Example: host = http://127.0.0.1:8000/
```List all service: http://127.0.0.1:8000/
```
```Show first service: http://127.0.0.1:8000/service/1/
```
```Show second service: http://127.0.0.1:8000/service/2/
```
```Search service: http://127.0.0.1:8000/service/?q=<query>
```
