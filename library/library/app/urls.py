from django.urls import path
from . import views

urlpatterns = [
    path('',views.create),
    path('1',views.display , name="display"),
    path('single/<int:vk>',views.single, name="single"),
    path('4/<int:id>',views.update,name="update"),
    path('9/<int:pk>',views.delete , name="drop")


]