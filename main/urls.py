from django.urls import path
from . import views


app_name = 'main'  # here for namespacing of urls.

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("contact/", views.contact, name="contact"),
    path("wd/", views.webdesign, name="webdesign"),
    path("graphics/", views.graphicsdesign, name="graphicsdesign"),
]
