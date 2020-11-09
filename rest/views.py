from django.shortcuts import render 
from django.views import generic
from rest_framework import viewsets
from .models import Folder
from .serializers import FolderSerializer

# Create your views here.

def index(request):
    folder_list = Folder.objects.all()
    folder_dict = {'folders' : folder_list}
    return render(request, 'rest/index.html', folder_dict)

class FolderViewSet(viewsets.ModelViewSet):
    serializer_class = FolderSerializer
    queryset = Folder.objects.all()
