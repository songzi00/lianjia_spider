
from django.urls import path
from myapp import views
app_name = 'myapp'


urlpatterns = [
    path('',views.index,name = 'index'),    #主页
    path('search/',views.search,name = 'search'),    #主页
]


