from django.urls import path
from . import views
urlpatterns = [
    path('url/', views.show, name='show'),
    path('prashant/',views.sai, name='prashant'),
    path('pras/',views.abc, name='pras'),
    path('gsp/', views.duke, name='gsp'),
    path('sp/', views.dude, name='sp'),

]

