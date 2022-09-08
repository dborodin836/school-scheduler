from django.contrib import admin
from django.urls import path

import pages.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', pages.views.HomeView.as_view()),
    path('full', pages.views.FullSchedule.as_view()),
    path('full/v2', pages.views.FullScheduleV2.as_view()),
    path('ha', pages.views.generate)
]
