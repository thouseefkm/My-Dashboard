#contact/urls.py

from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'link'

urlpatterns = [
    path('', views.link_list, name='link_list'),
    path('create', views.link_new, name='link_new'),
    path('update/<int:pk>', views.link_edit, name='link_edit'),
    path('delete/<int:pk>', views.link_delete, name='link_delete'),
    # path('delete/<int:pk>', views.LinkDelete.as_view(), name='link_delete'),
    # path('contact_details/<int:pk>', views.contact_details, name='contact_details'),
    path('link/<int:pk>', views.LinkDetail.as_view(), name='link_detail'),
]

urlpatterns += staticfiles_urlpatterns()