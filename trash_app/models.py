from django.contrib.auth.models import User
from django.db import models


class Worker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='worker_profile')  # Привязка к учетной записи
    # Фото до уборки
    image_before = models.ImageField(upload_to='before_after/', blank=True, null=True)
    datetime_image_before = models.DateTimeField(blank=True, null=True)
    location_image_before = models.CharField(max_length=255, blank=True, null=True)  # Координаты

    # Фото после уборки
    image_after = models.ImageField(upload_to='before_after/', blank=True, null=True)
    datetime_image_after = models.DateTimeField(blank=True, null=True)
    location_image_after = models.CharField(max_length=255, blank=True, null=True)  # Координаты

    def __str__(self):
        return f"{self.__dict__}"


class Bid(models.Model):
    TYPE_CHOICES = [
        ('trash', 'Свалка'),
        ('dirt', 'Не убрано'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Рассматривается'),
        ('in_progress', 'В процессе'),
        ('completed', 'Выполнено'),
        ('declined', 'Отклонено'),
    ]

    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bids')  # Гражданин
    username = models.CharField(max_length=20, null=True)
    chat_id = models.BigIntegerField(null=True)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    coordinates = models.TextField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='trash_cans/', default="trash_project/media/trash_cans/133500.jpg")
    description = models.TextField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    assigned_worker = models.ForeignKey(Worker, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_bids')  # Привязка заявки к сотруднику

    def __str__(self):
        import locale

        # Set the locale to Russian
        locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')  # Make sure this locale is installed on your system
        data = {
            **self.__dict__,
            'created_at': self.created_at.strftime('%d %B, %H:%M') if self.created_at else None,
        }
        return f"{data}"


from django.db import models

class Analytics(models.Model):
    total_bids = models.IntegerField(default=0)
    resolved_bids = models.IntegerField(default=0)
    active_bids = models.IntegerField(default=0)
    average_reaction_time = models.DurationField(null=True, blank=True)
    average_completion_time = models.DurationField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.__dict__}"


class Notifications(models.Model):
    choices = [
        ('check_by_human', 'Требуется ручная проверка'),
        ('check_by_ai', 'Обработаны ИИ'),
        ('no_trash_cans', 'На фото нет баков')
    ]

    user = models.OneToOneField(Bid, on_delete=models.CASCADE, related_name='notifications')
    message = models.CharField(max_length=100, choices=choices)

# class Worker(models.Model):
#     STATUS_CHOICES = [
#         ('in_progress', 'В процессе'),
#         ('completed', 'Выполнено'),
#         ('declined', 'Отклонено'),
#     ]
#
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')  # Работник
#     bid = models.OneToOneField('Bid', on_delete=models.CASCADE, related_name='task')  # Заявка
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='in_progress')
#     image_before = models.ImageField(upload_to='tasks/before/')
#     image_after = models.ImageField(upload_to='tasks/after/')
#     location_before = models.CharField(max_length=255, blank=True, null=True)
#     location_after = models.CharField(max_length=255, blank=True, null=True)
#     datetime_before = models.DateTimeField(blank=True)
#     datetime_after = models.DateTimeField(blank=True)
#
#     assigned_at = models.DateTimeField(auto_now_add=True)
#     completed_at = models.DateTimeField(blank=True, null=True)
#
#     def __str__(self):
#         return f"Task for Bid #{self.bid.id} - Worker: {self.user.username}"
#
# class Bid(models.Model):
#     TYPE_CHOICES = [
#         ('trash', 'Свалка'),
#         ('dirt', 'Не убрано'),
#     ]
#
#     STATUS_CHOICES = [
#         ('pending', 'Рассматривается'),
#         ('completed', 'Выполнено'),
#         ('declined', 'Отклонено'),
#     ]
#
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bids')  # Гражданин
#     type = models.CharField(max_length=20, choices=TYPE_CHOICES)
#     address = models.TextField(max_length=255, blank=True, null=True)
#     image = models.ImageField(upload_to='trash_cans/', default="trash_project/media/trash_cans/133500.jpg")
#     description = models.TextField(max_length=255, blank=True, null=True)
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f"Bid #{self.id} by {self.user.username} - {self.get_status_display()}"


