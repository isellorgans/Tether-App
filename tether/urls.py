from django.conf.urls import url
from tether import views

urlpatterns = [
    url(r'^$', views.intro, name='intro'),
    url(r'^index/$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^publicleague/(?P<league_name_slug>[\w\-]+)/$', views.public_leagues, name='public_league'),
    url(r'^match/(?P<match_id>[0-9]+)/$', views.matches, name='match'),
    url(r'^join_public/$', views.join_public, name='join_public'),
    url(r'^add_league/?$', views.add_league, name='add_league'),
    url(r'^user_profile/?$', views.profile, name='profile')
]
handler404 = 'tether.views.handler404'