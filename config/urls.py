from django.contrib import admin
from django.urls import path, include
from blog.views.home import home





urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('account.urls', namespace="account")),
    path('blog/', include('blog.urls', namespace='blog'))
]
