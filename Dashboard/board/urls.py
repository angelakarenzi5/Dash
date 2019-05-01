from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    url(r'^$',views.board,name='board'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^view/profile/(\d+)', views.view_profile, name='view-profile'),
    url(r'^dashboard/', views.dashboard, name='dashboard'),
    url(r'^new/dashboard', views.new_dashboard, name='new_dashboard'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)