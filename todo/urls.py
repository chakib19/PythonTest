from django.conf.urls import url, include
from todo import views
from rest_framework.routers import DefaultRouter

#create 
router = DefaultRouter(trailing_slash=False)
router.register(r'todos', views.TodoItemViewSet)

# the api urls 
urlpatterns = [
    url(r'^', include(router.urls)),
]
