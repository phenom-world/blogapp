from django.urls import path
from .views import BlogListView, BLogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('post/<int:pk>/', BLogDetailView.as_view(), name='post_detail'),
    path('post/new/', BlogCreateView.as_view(), name="post_new"),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name="post_edit"),
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name="post_delete"),
    path("acccounts/register/", views.register, name="register"),
    path("accounts/login/", views.loginPage, name="loginPage"),
    path("accounts/logout/", views.logoutPage, name="logoutPage"),
    path(
        "reset_password/",
        auth_views.PasswordResetView.as_view(
            template_name="accounts/form.html"),
        name="reset_password",
    ),
    path(
        "reset_password_sent/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="accounts/done.html"),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="accounts/confirm.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset_password_complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="accounts/complete.html"
        ),
        name="password_reset_complete",
    ),
]
