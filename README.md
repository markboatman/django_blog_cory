# Django Blog App
- This is a muti-user blog app written in Python using the Django framework.
- This README file assumes you KNOW HOW TO build and start a basic django application
  - Example here: https://www.djangoproject.com/start/
- This code is based on the code presented in this video series: https://www.youtube.com/watch?v=UmljXZIypDc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p

## Database backend
- The app is configured by default to create and use a sqlite database. If DATABASE_URL is defined in the app environment the app will use that database instead.

## External app requirements
- The app needs to have access to an Amazon S3 bucket for image file storage. https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html
- The app needs to have access to a gmail account for password reset/recovery 

## Required environment variables definitions
- SECRET_KEY"some_value" 
  - valid values for this key can be generated here:
    - https://miniwebtool.com/django-secret-key-generator/
- EMAIL_USER="some_value"
- EMAIL_PASS="some_value"
- AWS_ACCESS_KEY_ID="some_value"
- AWS_SECRET_ACCESS_KEY="some_value"
- AWS_STORAGE_BUCKET_NAME="some_value"

## Optional bash startup script 
- This script should be in the dir where manage.py is located

```
  #!/bin/bash

  # can generated a valid key here: https://miniwebtool.com/django-secret-key-generator/
  export SECRET_KEY="dev_key_blog_appXYZ"

  # django will use this gmail account, 
  export EMAIL_USER="some_value"
  export EMAIL_PASS="some_value"
  # the module we use for AWS S3 bucket access expects these vars to be defined.
  export AWS_ACCESS_KEY_ID="some_value"
  export AWS_SECRET_ACCESS_KEY="some_value"
  export AWS_STORAGE_BUCKET_NAME="some_value"

  python manage.py runserver
```

## This app needs to be executed in a python virtual enviroment
- Activate the python virtual enviroment from the viritual environments top level directory.
  - '$>. ./bin/activate'

## Start the app
- Do a standard django startup
  - '$>python manage.py runserver'
- Optionally you can run the start up script described above

## See the document RUN-APP-LOCALLY.md for more information