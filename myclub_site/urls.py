"""myclub_site URL Configuration

Examples:
Function views for apps
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views for apps
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf from app.urls.py
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from events.views import index
from . import contact

urlpatterns = [
    path('',index,name='default'),
    path('admin/', admin.site.urls),
    path('contact/', contact.contact, name='contact'),
    path(
        'admin/password_reset/',
        auth_views.PasswordResetView.as_view(),
        name = 'admin_password_reset',
    ),
    path(
        'admin/password_reset/done/',
        auth_views.PasswordResetDoneView.as_view(),
        name = 'password_reset_done'
    ),
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(),
        name = 'password_reset_confirm',
    ),
    path(
        'reset/done/',
        auth_views.PasswordResetCompleteView.as_view(),
        name  = 'password_reset_complete',
    ),
    path('', include('events.urls')),#this is what the url should start with then will come the year and month
]
