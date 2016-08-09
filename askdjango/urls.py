"""askdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from blog import views
from pokemon import views as pokemon_views
from blog.models  import Comment



urlpatterns = [
      url(r'^$', views.post_list, name="home"),
      url(r'^admin/', admin.site.urls),
      url(r'^post_list$', views.p_list, name = "post_list"),
      url(r'^comment_list$', views.comment_list, name = "comment_list"),
      url(r'^post_list/detail/$', views.postd_list, name = "post_detail"),
      url(r'^test/$', views.comments, name = "test"),
      url(r'^post_list/detail/(?P<pk>\d+)/$', views.post_detail, name = "post_d"),
      url(r'^comments/(?P<pk>[0-9]\d+)/edit/$', views.comment_edit),

      url(r'^comments/new/$', views.comment_new, name="comment"),
      url(r'^comments1/new/$', views.comment_new1, name="test1"),
      url(r'^posts/new/$', views.post_new, name="post"),

      url(r'^rank/$', pokemon_views.pokemon_rank, name='rank'),

      url(r'^user/$', pokemon_views.user_list, name='user'),

      url(r'^location$', pokemon_views.location_list, name='location'),

      url(r'^pokemon/$', pokemon_views.pokemon_list, name='pokemon'),

      url(r'^capture$', pokemon_views.capture_list, name='capture'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


