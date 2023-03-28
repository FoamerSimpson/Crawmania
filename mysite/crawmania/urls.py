from unicodedata import name
from django.urls import path

from . import views
from django.conf.urls.static import static
from mysite import settings
app_name = 'crawmania'

urlpatterns=[
    path('', views.crawmania, name='crawmania'),
    path('reservations/', views.reservations, name='reservations'),
    path('guestlist/', views.guestlist, name='guestlist'),
    path('guestlist/join/', views.join, name='join'),
    path('guestlist/join/addrecord/', views.addrecord, name='addrecord'),
    path('about/', views.about, name='about'),
    path('prize/', views.prizeview.as_view()),
    path('prize/<int:year>/', views.CrawmaniaYearArchiveView.as_view(), name="Crawmania_year_archive"),
]


