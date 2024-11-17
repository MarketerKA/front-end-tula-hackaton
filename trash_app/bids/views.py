from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import BidForm, WorkerCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ..models import Bid, Worker, User
from django.http import HttpResponse
from ..signals import notify_user

""" Заявки """
@login_required
def create_bid(request):
    if request.method == 'POST':
        form = BidForm(request.POST, request.FILES)
        if form.is_valid():
            bid = form.save(commit=False)
            bid.save()
            return JsonResponse({
                'id': bid.id,
                'type': bid.type,
                'coordinates': bid.coordinates,
                'description': bid.description,
                'status': bid.status,
                'created_at': bid.created_at.strftime('%Y-%m-%d %H:%M:%S')
            }, status=201)
            # return redirect('bid_list')
    else:
        form = BidForm()
    return render(request, 'create_bid.html', {'form': form})


from django.core.serializers import serialize
@login_required
def bid_list(request):
    bids = Bid.objects.all().values(
        'id', 'type', 'coordinates', 'description', 'status',
        'assigned_worker__user__username', 'created_at'
    )
    return JsonResponse(list(bids), safe=False)
    # return HttpResponse(bids)
    # if request.headers.get('Accept') == 'application/json' or request.GET.get('format') == 'json':
    #     return JsonResponse(list(bids), safe=False)

    # return render(request, 'bid_list.html', {'bids': bids})

@login_required
def bid_detail(request, bid_id):
    bid = get_object_or_404(Bid, id=bid_id)
    return JsonResponse({
        'id': bid.id,
        'type': bid.type,
        'coordinates': bid.coordinates,
        'description': bid.description,
        'status': bid.status,
        'assigned_worker': bid.assigned_worker.user.username if bid.assigned_worker else None,
        'created_at': bid.created_at.strftime('%Y-%m-%d %H:%M:%S'),
    })
    # return HttpResponse(bid)

    # return render(request, 'bid_detail.html', {'bid': bid})

@login_required
def update_bid(request, bid_id):
    bid = get_object_or_404(Bid, id=bid_id)
    if request.method == 'POST':
        form = BidForm(request.POST, request.FILES, instance=bid)
        if form.is_valid():
            bid = form.save()
            if bid.status == 'completed':
                notify_user(bid)

            bid.save()

            return HttpResponse(form)
            # return redirect('bid_list')
    else:
        form = BidForm(instance=bid)

    return render(request, 'update_bid.html', {'form': form, 'bid': bid})


@login_required
def delete_bid(request, bid_id):
    bid = get_object_or_404(Bid, id=bid_id)
    if request.method == 'POST':
        bid.delete()
        return HttpResponse({'message': f"Successfully deleted bid, {bid_id}"})
        # return redirect('bid_list')
    return render(request, 'delete_bid.html', {'bid': bid})



""" Работники """
@login_required
def create_worker_view(request):
    if request.method == 'POST':
        form = WorkerCreationForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']

            # Check if the user is already a worker
            if Worker.objects.filter(user=user).exists():
                messages.error(request, f"User {user.username} is already a worker.")
            else:
                # Create a Worker profile
                Worker.objects.create(user=user)
                messages.success(request, f"Worker profile created for {user.username}.")
                return HttpResponse(get_object_or_404(Worker, user=user))
    else:
        form = WorkerCreationForm()

    return render(request, 'create_worker.html', {'form': form})

@login_required
def worker_list(request):
    workers = Worker.objects.all()
    return HttpResponse(workers)
    # return render(request, 'worker_list.html', {'workers': workers})

@login_required
def worker_bids(request, worker_id):
    worker = get_object_or_404(Worker, id=worker_id)
    bids = Bid.objects.filter(assigned_worker=worker)
    return HttpResponse(bids)
    # return render(request, 'worker_bids.html', {'worker': worker, 'bids': bids})

from django.utils.timezone import now
@login_required
def complete_task(request, task_id):
    task = get_object_or_404(Worker, id=task_id, user=request.user)
    if request.method == 'POST':
        task.status = 'completed'
        task.completed_at = now()
        task.save()
        return redirect('worker_tasks')
    return render(request, 'complete_task.html', {'task': task})

@login_required
def assign_bid_to_worker(request, bid_id, worker_id):
    if request.method == "POST":
        try:
            # Call the function to assign the bid
            # Получаем заявку по ID
            bid = get_object_or_404(Bid, id=bid_id)

            # Получаем сотрудника по ID
            worker = get_object_or_404(Worker, id=worker_id)

            # Назначаем заявку сотруднику
            bid.assigned_worker = worker
            bid.status = 'in_progress'  # Меняем статус заявки на "В процессе"
            bid.save()  # Сохраняем изменения

            return HttpResponse(bid)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
