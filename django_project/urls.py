"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include,re_path
from django_app import views
from django.views.generic.base import TemplateView
import debug_toolbar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls')),
    path('signup/', views.signup, name='signup'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('__debug__',include(debug_toolbar.urls)),
    path('create_data/',views.Create_model.as_view(),name='create'),
    path('api-auth/', include('rest_framework.urls')),   #api-auth/login  for rest api login page
    # path('person/<pk>',views.PersonView.as_view()),
    path('person/',views.PersonAll.as_view()),
    path('menu/',views.Menu_View.as_view()),
    # path('item-detail/',views.Item_View.as_view()),

]
