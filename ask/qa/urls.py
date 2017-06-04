from django.conf.urls import url
from qa.views import test,q_main,q_detail,popular

urlpatterns = [
    url(r'^$', q_main, name='q_main'),
    url(r'^question/(?P<pk>\d+)/$', q_detail, name='q_detail'),
    url(r'^popular/', popular, name='popular'),
    url(r'^login/', test, name='login'),
    url(r'^signup/', test, name='signup'),
    url(r'^ask/', test, name='ask'),
    url(r'^new/', test, name='new'),
]
