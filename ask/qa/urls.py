from qa.views import test

urlpatterns = patterns('qa.views',
    url(r'^$', test, name='qaroot'),
    url(r'^login/', test, name='login'),
    url(r'^question/(?P<id>\d+)/$', test, name='question-id'),
    url(r'^signup/', test, name='signup'),
    url(r'^ask/', test, name='ask'),
    url(r'^news/', test, name='news'),
    url(r'^popular/', test, name='popular'),
)

