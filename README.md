# udemy_django3
learning progress from https://www.udemy.com/course/django-3-make-websites-with-python-tutorial-beginner-learn-bootstrap/

<h3>buzz words</h3> 
models = collection of databases or classes <br/>
database = class <br/>
rows = objects <br/>

<h3> when pushing to git</h3> 
`pip freeze > requirements.txt` <br/>
`git add .` <br/>
`git commit -m 'asdf'` <br/>
`git push` <br/>

<h3>when pulling from git</h3> 
`git pull` <br/>
`pip install -r requirements.txt` <br/>
`python manage.py migrate` <br/>
`python manage.py collectstatic` <br/>

<h3>when creating new models/editing existing models</h3> 
`python manage.py makemigrations` <br/>
`python manage.py migrate` <br/>

<h3>creating superuser so you can login into localhost:8000/admin</h3>  
`python manage.py createsuperuser` <br/>

<h3>get vs post</h3> 
get request will show the username and password on URL on browser <br/>
post request will not show the username and password on URL on browser <br/>

<h3>if i wanna change column name of a model</h3> 
`python manage.py makemigrations` <br/>
change the migration file from `migrations.RenameField` to `migrations.AlterField` <br/>
`python manage.py migrate` <br/>

