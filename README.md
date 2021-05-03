# Tech Sense Blog

**About**
This is a demo project for practicing Django. The idea was to build some basic blogging platform.

It was made using Python 3.6 + Django and database is SQLite. Bootstrap was used for styling. Testing is done using untitest module.

There is a login and registration functionality included.

User has his own blog page, where he can add new blog posts. Every authenticated user can comment on posts made by other users. Home page is paginated list of all posts. Non-authenticated users can see all blog posts, but cannot add new posts or comment.

App is covered with tests.

Prerequisites
[Optional] Install virtual environment:

```
$ python -m virtualenv env
```
[Optional] Activate virtual environment:

On macOS and Linux:
```
$ source env/bin/activate
```
On Windows:
```
$ .\env\Scripts\activate
```
Install dependencies:
```
$ pip install -r requirements.txt
```
## How to run
Default
You can run the application from the command line with manage.py. Go to the root folder of the application.

Creating Super User:
```
$ python manage.py createsuperuser
```

Run migrations:
```
$ python manage.py migrate
```

Initialize data:
```
$ python manage.py loaddata users posts comments
```
Run server on port 8000:
```
$ python manage.py runserver 8000
```

## Post Installation
Go to the web browser and visit http://localhost:8000/home

Admin username: admin

Admin password: adminpassword

User username: dusan

User password: dusanpassword

Helper Tools
Django Admin
It is possible to add additional admin user who can login to the admin site. Run the following command:

$ python manage.py createsuperuser
Enter your desired username and press enter.

Username: admin_username
You will then be prompted for your desired email address:

Email address: admin@example.com
The final step is to enter your password. You will be asked to enter your password twice, the second time as a confirmation of the first.

Password: **********
Password (again): *********
Superuser created successfully.
Go to the web browser and visit http://localhost:8000/admin

Tests
Default
Activate virtual environment:

On macOS and Linux:

$ source env/bin/activate
On Windows:

$ .\env\Scripts\activate
Running tests:

$ python manage.py test blog

**[Visit Website](https://techsenseblog.herokuapp.com)**
