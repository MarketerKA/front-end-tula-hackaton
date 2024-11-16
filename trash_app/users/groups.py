from django.contrib.auth.models import Group, User

# Создание групп
def create_groups():
    operator_group, _ = Group.objects.get_or_create(name='Operators')
    worker_group, _ = Group.objects.get_or_create(name='Workers')

def is_operator(user):
    return user.groups.filter(name='Operators').exists()

def is_worker(user):
    return user.groups.filter(name='Workers').exists()