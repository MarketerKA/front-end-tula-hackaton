from django.db.models.signals import post_save
from django.dispatch import receiver
from models import Bid

@receiver(post_save, sender=Bid)
def notify_user_on_bid_status_change(sender, instance, **kwargs):
    if instance.status == 'accepted':
        print(f'Notify {instance.user.username}: Your bid for {instance.trash_can} has been accepted.')
    elif instance.status == 'rejected':
        print(f'Notify {instance.user.username}: Your bid for {instance.trash_can} has been rejected.')
