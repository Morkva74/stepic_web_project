from django.conf.urls import url
from qa.views import test,q_main,q_detail,popular,q_ask, q_answer

urlpatterns = [
    url(r'^$', q_main, name='q_main'),
    url(r'^question/(?P<pk>\d+)/$', q_detail, name='q_detail'),
    url(r'^popular/', popular, name='popular'),
    url(r'^login/', test, name='login'),
    url(r'^signup/', test, name='signup'),
    url(r'^ask/', q_ask, name='ask'),
    url(r'^answer/', q_answer, name='q_answer'),
    url(r'^new/', test, name='new'),
]
