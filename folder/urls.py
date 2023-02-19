from django.urls import path

from .views import Folder_detail

urlpatterns = [

    path('detail/<uuid:id>', Folder_detail.as_view(), name = 'folder_detail'),

]