# udemy_django3
learning progress from https://www.udemy.com/course/django-3-make-websites-with-python-tutorial-beginner-learn-bootstrap/

when pushing to git <br/>
`pip freeze > requirements.txt` <br/>
`git add .` <br/>
`git commit -m 'asdf'` <br/>
`git push` <br/>

when pulling from git <br/>
`git pull` <br/>
`pip install -r requirements.txt` <br/>
`python manage.py migrate` <br/>
`python manage.py collectstatic` <br/>

when creating new models/editing existing models <br/>
`python manage.py makemigrations` <br/>
`python manage.py migrate` <br/>

creating superuser so you can login into localhost:8000/admin  <br/>
`python manage.py createsuperuser` <br/>

get vs post <br/>
get request will show the username and password on URL on browser <br/>
post request will not show the username and password on URL on browser <br/>
