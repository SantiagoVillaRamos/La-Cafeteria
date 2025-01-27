from django.urls import path, include
from . import views
urlpatterns = [
    path('<int:page_id>/', views.page, name='page'),
]