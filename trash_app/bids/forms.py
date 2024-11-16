from django import forms
from ..models import Bid, Worker, User

class BidForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ['type', 'address', 'image', 'description', 'status', 'assigned_worker']



class WorkerCreationForm(forms.ModelForm):
    user = forms.ModelChoiceField(
        queryset=User.objects.all(),
        required=True,
        label="Select User"
    )

    class Meta:
        model = Worker
        fields = ['user', 'image_before', 'image_after']

