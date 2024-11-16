from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import login

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


# from django.shortcuts import render, redirect
# from django.contrib.auth.models import Group
# from django.contrib.auth import login
#
# def register(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         role = request.POST['role']
#
#         # Create the user
#         user = User.objects.create_user(username=username, password=password)
#         user.role = role
#         user.save()
#
#         # Assign the user to the correct group
#         if role == 'worker':
#             worker_group, _ = Group.objects.get_or_create(name='Workers')
#             user.groups.add(worker_group)
#         elif role == 'operator':
#             operator_group, _ = Group.objects.get_or_create(name='Operators')
#             user.groups.add(operator_group)
#
#         # Log the user in and redirect
#         login(request, user)
#         return redirect('/')  # Redirect to a common or role-specific dashboard
#
#     return render(request, 'register.html')
