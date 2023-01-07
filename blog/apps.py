from django.apps import AppConfig

# 'python manage.py startapp blog' creates this
class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
