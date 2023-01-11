## Procedure to get this github stored django app to run locally
- I used this doc as a guide
  - https://www.makeuseof.com/django-project-clone-run-locally/
- I am using VENV to create python virtual environments. VENV is a python virtual enviroment creator that is installed by default with python when using the python version managagment tool, pyenv. 
- I am running a Mac, so some of this will be different on other OSs.
- Hope this will work for you or at least get you headed in the right direction in you troubleshooting journey.

- Create a virtual environment, name it something relevant.
  - 'python -m venv [my-virtual-env-name]'
- cd into the created virtual environment dir. 'ls' to see the files and dirs it created.
- to see if the virtual environment works, do this: 
  - '. ./bin/activate' or 'source ./bin/activate'
- to stop the virtual environment do this:
  - 'deactivate'

## Clone the github repository to your local machine
**NOTE** - The virtual environment does not have to be active to clone the github repository into the virtual environment's directory structure.
- My corys_blog app is on github as a Public Template, go here:
  - https://github.com/markboatman/django_blog_cory
- Click on 'Use This Template' and create a new repository from this repository Template.
- Go to your newly created repository, click on the green code button, get the https or ssh url for this new repository. You will need the url for the git clone command.
- From the virtual environment directory you created above do this
  - 'git clone [repository_url]
- You now have a dir named the same as the repository you cloned from github
- I renamed the created repository dir 'corys_blog' so this will match the child main app called 'corys_blog'.
- So now you have a virtual environment dir that was created using venv with  a /bin, /include, /lib, and a /[cloned-repository] directory. The directory structure should now be in place.

## Install required packages and init the database
- cd into corys_blog (cloned-repository-dir) and run:
  - 'pip install -r requirements.txt'
- Go up and over 'cd ../lib/python*/site-packages' and then 'ls' to look at the installed packages.
- go to corys_blog/corys_blog and create a runserver script with all the needed environment variables. See the README.md file for environment variable requirements. The run server script needs to be in the same directory as manage.py (that would be best). 
- Create and migrate objects to the default sqlite database.
  - from the directory with the manage.py file
    - 'python manage.py makemigrations' - this won't do anything but, just in case.
    - 'python manage.py migrate' - this creates the db objects
  - You should now have a db.sqlite* file (database) in the current dir.

## Start the app
- make sure you have a mechanism in place to define all the environment vars that the settings.py file will need.
- 'python manage.py runserver' - The app should be available on the designated port.
- Alternatively, run you runserver script that defines the needed environment vars and executes the runserver command.



