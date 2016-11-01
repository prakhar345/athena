from django.conf.urls import url
from django.conf.urls.static import static
from . import views
from django.conf import settings

urlpatterns=[
    # url(r'^static/$',views.index,name="home"),
    url(r'^$',views.index,name="home"),
    url(r'^search$',views.searchReq,name="search"),
    
]