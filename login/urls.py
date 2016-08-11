from django.conf.urls import url
from . import views
from blog import views as blog_views


urlpatterns = [
        url(r'^signup/$', views.signup, name='signup'),
        url(r'^login/$', views.my_view, name='login'),
        url(r'^profile/$',  blog_views.p_list),
        url(r'^logout/$', views.logout, name='home'),
]
