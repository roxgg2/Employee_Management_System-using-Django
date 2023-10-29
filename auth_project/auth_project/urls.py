from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from auapp.views import uhome, create, remove

urlpatterns = [
    path('admin/', admin.site.urls),
    path("ulogin", ulogin, name="ulogin"),
    path("ulogout", ulogout, name="ulogin"),
    path("", uhome, name="home"),
    path("create/", create, name="create"),
    path("remove/<int:id>/", remove, name="remove"),
]
