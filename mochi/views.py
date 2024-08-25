from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Register
from .serializers import RegisterSerializer
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.http import HttpResponse

def home_view(request):
    return HttpResponse("Welcome to the API! Go to /api/registers/ to manage registers.")

def register_create_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register_success')  # Redirect to a success page or list view
    else:
        form = RegisterForm()
    return render(request, 'mochi/register_form.html', {'form': form})


class RegisterViewSet(viewsets.ModelViewSet):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    search_fields = ['name', 'email']
    ordering_fields = ['name', 'email', 'passing_year']
    ordering = ['name']
