from django.urls import path,include
from . import views

urlpatterns = [
    path('test',views.FirstApiTestView.as_view(),name="test")

]
