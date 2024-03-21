
# Multimedia Project in Django

The goal of this project is to provide a minimalistic Django project template that works out of the box and has a basic setup you can expand upon. It is written with Django 1.11 and Python 3 in mind.

## Main Features

- Separated development and production settings
- Example app with a custom user model
- Bootstrap static files included
- User registration and login demo
- Procfile for easy deployments
- Separated requirements files
- SQLite by default if no environment variable is set

## Usage

### Existing Virtualenv

1. If your project is already in an existing Python 3 virtualenv, first install Django by running:

    ```
    $ pip install django
    ```

2. Then run the following command to start the new project (replace `<project_name>` with your desired project name):

    ```
    $ django-admin.py startproject --template=https://github.com/nikolak/django-template/zipball/master --extension=py,md <project_name>
    ```

### No Virtualenv

1. If you don't have Django installed for Python 3, run:

    ```
    $ pip3 install django
    ```

2. Then create your project using:

    ```
    $ python3 -m django startproject --template=https://github.com/nikolak/django-template/zipball/master --extension=py,md <project_name>
    ```

3. Install local dependencies:

    ```
    $ pip install -r requirements/local.txt
    ```

4. Apply migrations:

    ```
    $ python manage.py migrate
    ```

5. Run the development server:

    ```
    $ python manage.py runserver
    ```

Remember to replace `<project_name>` with your actual project name.

---

Feel free to adapt this template to your specific needs. Good luck with your multimedia project! 🎥🎵📸

