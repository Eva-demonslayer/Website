Django Setup:
Step	Description	                        Command
1.	    Set up a virtual environment	    python -m venv env
2.	    Activate the virtual environment	source site_env/Scripts/activate 
                                            powershell: .\/site_env/Scripts/activate.ps1
3.	    Install Django	                    python -m pip install django
4.	    Pin your dependencies	            python -m pip freeze > requirements.txt
5.	    Set up a Django project	            django-admin startproject <projectname>
6.	    Start a Django app	                python manage.py startapp <appname>

Changes to Django models:
1. Change your models (in models.py).
2. Run python manage.py makemigrations to create migrations for those changes
3. Run python manage.py migrate to apply those changes to the database.

Interactive Console:
python manage.py shell
exit()

Server Initiate/Deactivate:
1. python manage.py runserver
2. Press Ctrl+C to stop the server