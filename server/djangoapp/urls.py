from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'

urlpatterns = [
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('register', views.registration, name='registration'),  # ← Make sure this is here
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)