from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # url(r'^$', views.home, name='home'),
    url(r'^guestbook/', include('guestbook.urls'), namespace='guestbook'),
    )