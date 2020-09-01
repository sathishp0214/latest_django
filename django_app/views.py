from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm  #inbuilt signup form
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView, ListCreateAPIView
from django_filters.rest_framework import DjangoFilterBackend   #for API filtering
from rest_framework import filters    #for API searching and ordering
from .serializers import *
from .models import *

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()      #Save the username registration details in inbuilt auth users model
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            request.session['username'] = str(username)
            login(request, user)
            return redirect('home')   #Redirects into user's Welcome homepage.
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

from django.views.generic.edit import CreateView

class Create_model(CreateView):
    model = Drink
    fields = ['item','caffeine']
    template_name = 'create_data.html'
    success_url = "/"


class PersonView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Person.objects.all()
    serializer_class = PersonDetails


class PersonAll(ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonDetails
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['person_name', 'age']
    search_fields = ['person_name']
    ordering_fields = ['person_name']

    # def get_queryset(self):
    #     person_name = self.kwargs['person_name']
    #     print ("###",self.kwargs,"++++",self.request)
    #     return Person.objects.filter(person_name=person_name)


class Menu_View(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class Item_View(ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


