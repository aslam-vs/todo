ToDo List
=========

Application for manage ToDos. We can Create, read, edit, delete ToDo  by using this App .


Getting Up and Running Locally
---------------------

The steps below will get you up and running with a local development environment. Assume you have the following installed:-

	pip
	virtualenv

Activate virtualenv and install the requirements for your local development:-

	pip install -r requirements/local.txt

Django migration done by using below commands:

	python manage.py makemigrations
	python manage.py migrate

* Created an **superuser account**, by using use below command:
    $ python manage.py createsuperuser

    username : admin
    password : admin

Command for running django project:
	python manage.py runserver


URL Documentation
-----------------

1. Documentation available in http://127.0.0.1:8000/ 

2. To Do List view : http://127.0.0.1:8000/todos/
	
	In Action read, update, delete buttons are available

3. Create new To Do : http://127.0.0.1:8000/todos/add/

4. Update To Do : http://127.0.0.1:8000/todos/add/1/
	
	In this url 1 shows pk for updating To Do

5. Detail view for To Do : http://127.0.0.1:8000/todos/1/

	In this url 1 shows pk for reading To Do

6. Admin Panel : http://127.0.0.1:8000/admin/

	username : admin
	password : admin

	Search, Filtering and csv download implimented in admin panel

7. API for To Do

	To Do List API : app/v1/todos/
	Individual API View (for pk=1) : app/v1/todos/1
