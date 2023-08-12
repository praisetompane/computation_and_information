#!/bin/zsh
#
#    quick utility to create Django project.
#    accepts project name as parameter
#    Example:
#    $ ./create_project.sh my_project
#

project=$1

echo "creating project"
    django-admin startproject $project
echo "done"

cp run_project.sh ./$project
cp create_app.sh ./$project




