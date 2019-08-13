from django.conf.urls import url
from django.conf import settings
from django.contrib import admin
from rest_framework.authtoken import views


urlpatterns =
[
	path('admin/', admin.site.urls),
	path('v1/', include('testSite.urls', namespace='test')),
]