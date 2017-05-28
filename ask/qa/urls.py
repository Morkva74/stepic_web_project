from django.conf.urls import url
from qa.views import test

urlpatterns = [
    url(r'^$', test, name='home'),
    url(r'^login/', test, name='login'),
    url(r'^question/(?P<pk>\d+)/$', test, name='question-id'),
    url(r'^signup/', test, name='signup'),
    url(r'^ask/', test, name='ask'),
    url(r'^new/', test, name='new'),
    url(r'^popular/', test, name='popular'),
]
