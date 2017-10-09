from django.conf.urls import url
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r'^$', views.index, name='index'),
<<<<<<< HEAD
=======
	url(r'^servicos$', views.service, name='service'),
	url(r'^contato$', views.contact, name='contact'),
>>>>>>> origin/master
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)