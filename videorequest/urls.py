from django.urls import path,include

urlpatterns = [
    path('',view.index,name='index'),
    path('vform',view.vform,name='vform')
]