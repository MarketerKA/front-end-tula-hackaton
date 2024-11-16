from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import TrashCan, Bid
from .forms import TrashCanForm, BidForm
from django.http import HttpResponse
from django.contrib.auth import login
from .forms import RegisterForm

def debug_user_info(request):
    if request.user.is_authenticated:
        return HttpResponse(f"Logged in as: {request.user.username}")
    else:
        return HttpResponse("Not logged in.")

@login_required
def create_trash_can(request):
    if request.method == 'POST':
        form = TrashCanForm(request.POST, request.FILES)
        if form.is_valid():
            trash_can = form.save(commit=False)
            trash_can.user = request.user
            trash_can.save()
            return redirect('list_trash_cans')  # Replace with your desired redirect
    else:
        form = TrashCanForm()
    return render(request, 'create_trash_can.html', {'form': form})

@login_required
def create_bid(request, trash_can_id):
    trash_can = get_object_or_404(TrashCan, id=trash_can_id)
    if request.method == 'POST':
        form = BidForm(request.POST)
        if form.is_valid():
            bid = form.save(commit=False)
            bid.user = request.user
            bid.trash_can = trash_can
            bid.save()
            return redirect('list_trash_cans')  # Replace with your desired redirect
    else:
        form = BidForm()
    return render(request, 'create_bid.html', {'form': form, 'trash_can': trash_can})

@login_required
def list_trash_cans(request):
    # trash_cans = TrashCan.objects.all()
    trash_cans = TrashCan.objects.order_by('-created_at')
    return render(request, 'list_trash_cans.html', {'trash_cans': trash_cans})

@login_required
def list_bids(request):
    bids = Bid.objects.order_by('-created_at')
    return render(request, 'list_bids.html', {'bids': bids})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user after registration
            return redirect('list_trash_cans')  # Redirect to a page after registration
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})
