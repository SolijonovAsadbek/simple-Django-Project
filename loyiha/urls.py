from django.urls import path
from . import views

urlpatterns = [
    path("hel/", views.hello, name='hello'),  # finksiyalar uchun xarita
    path("", views.Dash.as_view(), name='dash'),  # class lar uchun xarita
    path("about/", views.About.as_view(), name='about'),  # class lar uchun xarita
    path("news/", views.News.as_view(), name='news'),  # class lar uchun xarita

]
