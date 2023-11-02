from django.urls import path,include
from . import views

urlpatterns = [
    path('student/create',views.StudentCreateApiView.as_view(),)

]
