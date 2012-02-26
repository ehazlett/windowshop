from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('products.views',
    url(r'^$', 'index'),
)

