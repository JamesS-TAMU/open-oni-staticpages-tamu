from django.conf.urls import url, include
from onisite.plugins.staticpages import views

urlpatterns = [
    url(r'^(?P<pagename>\w+)$', views.page, name="static_pages_page"),
]
