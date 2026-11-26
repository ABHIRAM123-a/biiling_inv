"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from invoices import views
from django.contrib.auth import views as auth_views
from accounts import views as accounts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.HomePageView.as_view(), name='home'),
    path('cust_name/',views.show_invoices, name='cust_name'),
    path('invoices/', views.InvoiceListView.as_view(), name='all-invoices'),
    path('create/', views.create_invoice, name='create_invoice'),
    path('invoice/add/', views.create_invoice, name='add-invoice'),
    path('invoice/old/', views.show_old_invoices, name='show-old-invoices'),
    path('invoice/<int:pk>/', views.InvoiceDetailView.as_view(), name='invoice-detail'),
    path('invoice/new/', views.InvoiceCreateView.as_view(), name='invoice-create'),
    path('invoice/<int:pk>/edit/', views.InvoiceUpdateView.as_view(), name='invoice-update'),
    path('invoice/<int:pk>/delete/', views.InvoiceDeleteView.as_view(), name='invoice-delete'),
    path('invoice//', views.add_invoice, name='add-invoice'),
    path('login/', 
         auth_views.LoginView.as_view(template_name = 'accounts/login.html'),
         name='login'),
    
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', accounts_views.signup, name='signup'),
]
