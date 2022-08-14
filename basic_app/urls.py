from django.urls import path

from basic_app import views

urlpatterns = [

    path('disease/<int:pk>', views.Kasallik.as_view()),
    path('disease', views.Kasalliklar.as_view())
]
