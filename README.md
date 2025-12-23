# Phone Specifications Django Project

## Description
Django project that runs a Selenium to collect phone specifications
and stores them in PostgreSQL.

## Tech stack
- Python
- Django
- Selenium
- PostgreSQL

## Setup
```bash
git clone <repo_url>
cd dataBaseproject
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
selenium install
python manage.py migrate
python manage.py runserver