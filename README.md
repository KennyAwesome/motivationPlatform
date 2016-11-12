# motivationPlatform
"One's got motivation problem until one gets time problem". We solve both problems.

Status (by Kenny) at 7:14 Nov 12:
- registration works under "/user/register"
- login has form error, dunno how to fix
- to run:
1) git clone https://github.com/KennyAwesome/motivationPlatform.git
2) cd motivationPlatform/backend
3) python manage.py makemigration
4) python manage.py migrate
5) python manage.py createsuperuser
    -> to create database admin (email does not that matter)
    please keep it coherent:
        username: motivator
        password: awesomemotivationapp
6) python manage.py runserver
    -> python manage.py runserver PORT (is optional)
