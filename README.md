#URL SHORTENER, Django 3.2
##bit.ly, goo.gl, rb.gy and so forth.

Developed with:

`pipenv`,
`python 3.7`
`Django Framework 3.2`
`sqlite3`

##Dev Deployment:

### proj/settings.py
SHORTENED_HOST_NAME // <-- set         

## if db changed:

python manage.py migrate    

python manage.py loaddata user_url_status

python manage.py createsuperuser

## Admin site:

python manage.py runserver

http://127.0.0.1:8000/admin/    
#### boss:1234



