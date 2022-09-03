from django.contrib import admin
from django.urls import path

import pages.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', pages.views.HomeView.as_view())
]
