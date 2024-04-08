from django.contrib import admin 
from django.urls import path 
from django.urls import include
from .import views
from django.contrib.auth import views as auth_views

# Code Explanation:
# These are the names of the urls that we can access. If we try to access urls other than these, it will give an error.
# a. path(): It is used to route the url with the functions views in your app folder.
# b. include(): An element is returned by it, to include that element in urlpatterns.

urlpatterns = [
    path ('', views.home, name = 'home'),
    path ('index/', views.index, name = 'index'),
    path ('register/', views.admin.site.register, name='register'),
    path ('handeleSignup/', views.handleSignup, name='handleSignup'),
    path('handlelogin/', views.handlelogin, name='handlelogin'),
    path('handleLogout', views.handleLogout, name='handleLogout'),
    path('reset_password/', auth_views.PasswordResetView.as_view(temmplate_name="home/reset_password.html"), name='reset_password'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = "home/password_reset_form.html"), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="home/password_reset_done.html"), name='password_reset_complete'), 
    path('addmoney/', views.addmoney, name='addmoney'),
    path('addmoney_submission/', views.addmoney_submission, name='addmoney_submission'),
    path('charts/', views.charcts, name='charts'),
    path('tables/', views.tables, name='tables'),
    path('expense_edit/int:id', views.expense.edit, name='expense_edit'),
    path('<int:id>/addmoney_update/', views.addmoney_update, name='addmoney_update'),
    path('expense_delete/<int:id>', views.expense_delete, name='expense_delete'),
    path('profile/', views.profile, name='profile'),
    path('expense_month/', views.expense_month, name='expense_month'),
    path('stats/', views.stats, name='status'),
    path('expense_week', views.expense_week, name='expense_week'),
    path('weekly/', views.weekly, name='weekly'),
    path('check/', views.check, name="check"),
    path('search/', views.search, name="search"),
    path('<int:id>/profile_edit/', views.profile_edit, name="profile_edit"),
    path('<int:id>/profile_update/', views.profile_update, name="profile_update"),
    path('info/', views.info, name="info"),
    path('info_year/', views.info_year, name="info_year"),

]