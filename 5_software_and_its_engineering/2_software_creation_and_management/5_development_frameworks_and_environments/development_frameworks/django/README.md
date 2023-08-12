# Django Project Quick Setup

# usage
## install Django
```shell
# from root directory
./setup.sh
```
## activate a shell within virtual environment
```shell
# from root directory
pipenv shell
```

## create project:
   * this creates does the following:
      * a Django project folder called my_project.
      * installs two scripts:
         - create_app.sh : a shorthand to create a Django app for your project
         - run_project.sh : a shorthand to run your Django project
```shell
# from root directory
./create_project.sh my_project
```

## create app
```shell
# from project root directory
cd my_project
./create_app.sh my_app
```

## apply all migrations to project:
```shell
# from project root directory
python manage.py migrate
```

## run project:
```shell
# from project root directory
./run_project.sh 
```

# Django explanation
The store_front project has comments with prefix 'user added:'.
These comments in each file, explains how everything fits together.
search for these in explorer.


NB: substitute "my_project" and "my_app" with your actual names.