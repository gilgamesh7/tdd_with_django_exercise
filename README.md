# tdd_with_django_exrecise

# Links
[Test Driven Development with Python](https://www.obeythetestinggoat.com/book/chapter_01.html)
[How to setup and teardown using pytest](https://www.youtube.com/watch?v=JJmTO95AoqE)
[pytest-django documentation](https://pytest-django.readthedocs.io/en/latest/)
[Real Python pytes-django fixtures](https://realpython.com/django-pytest-fixtures/)


# Pre-requisites
- [Prerequisites and Assumptions](https://www.obeythetestinggoat.com/book/pre-requisite-installations.html)
- Install geckodriver on mac : brew install geckodriver
- pytest-django

# Learning
## Setting up
- Install & activate venv (python3 -m venv venv --upgrade-deps)
- See pre-requisites section above
- Generate project : ./venv/bin/django-admin startproject superlists .
- Generat app : python manage.py startapp lists
- Run pytest : pytest -v -s

## Migrations
- python manage.py makemigrations
- python manage.py migrate